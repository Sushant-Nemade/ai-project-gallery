import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import tarfile
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from tools.catalog import ROOT


DEMO_BUILDS = (
    {"id": "ai-blog-publisher", "repository": "Sushant-Nemade/ai-blog-publisher", "run": 37392334263,
     "prefix": "ai-blog-publisher", "label": "AI Blog Publisher", "mode": "Synthetic article reader"},
    {"id": "gitpulse", "repository": "Sushant-Nemade/gitpulse", "run": 37443114054,
     "prefix": "gitpulse", "label": "GitPulse", "mode": "Fictional audience workspace"},
    {"id": "market-insight", "repository": "Sushant-Nemade/MarketInsight", "run": 39066236450,
     "prefix": "MarketInsight", "label": "Market Insight", "mode": "Fictional financial research"},
    {"id": "travelbrain", "repository": "Sushant-Nemade/TravelBrain", "run": 39083633992,
     "prefix": "TravelBrain", "label": "TravelBrain", "mode": "Browser planner / illustrative budgets"},
)
ALLOWED = {".html", ".js", ".mjs", ".css", ".json", ".md", ".txt", ".woff", ".woff2",
           ".ttf", ".ico", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".xml", ".map"}
MAX_FILE = 25 * 1024 * 1024
MAX_TOTAL = 100 * 1024 * 1024
OMITTED_TEMPLATES = {"js/config.js.example"}


def extract_static(archive_path, destination):
    destination = Path(destination)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Use an empty extraction directory.")
    with tarfile.open(archive_path, "r:*") as archive:
        members = [member for member in archive.getmembers()
               if PurePosixPath(member.name).as_posix() not in OMITTED_TEMPLATES]
        if len(members) > 900 or sum(member.size for member in members) > MAX_TOTAL:
            raise ValueError("Static archive exceeds the upload limits.")
        names = set()
        for member in members:
            path = PurePosixPath(member.name)
            if (path.is_absolute() or ".." in path.parts or "\\" in member.name
                    or any(":" in part or any(ord(char) < 32 for char in part) for part in path.parts)
                    or not (member.isdir() or member.isfile()) or member.size > MAX_FILE):
                raise ValueError("Unsafe archive entry.")
            if member.isdir():
                continue
            if path.as_posix().casefold() in names:
                raise ValueError("Duplicate static path.")
            names.add(path.as_posix().casefold())
            legal_notice = re.search(r"(?:^|[._-])LICENSE(?:[-.][A-Za-z0-9._-]+)?$", path.name, re.IGNORECASE)
            if (any(part.startswith(".env") or part in {".git", "node_modules", "data", "functions"}
                    for part in path.parts)
                    or path.name == "_worker.js"
                    or (path.suffix.lower() not in ALLOWED and not legal_notice
                    and path.name not in {"NOTICE", "NOTICES", ".nojekyll"})):
                raise ValueError(f"Non-public or unsupported static archive entry: {path.as_posix()}")
        if "index.html" not in names:
            raise ValueError("Static archive has no root index.html.")
        destination.mkdir(parents=True, exist_ok=True)
        for member in members:
            if member.isfile():
                target = destination.joinpath(*PurePosixPath(member.name).parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open("xb") as output:
                    shutil.copyfileobj(source, output)


def gh_json(*arguments):
    result = subprocess.run(["gh", "api", *arguments], capture_output=True, text=True,
                            encoding="utf-8", timeout=45, check=True)
    return json.loads(result.stdout)


def build_bundle(output_directory=None):
    output_directory = Path(output_directory or ROOT / "build" / "cloudflare")
    output_directory.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="demo-", dir=output_directory) as directory:
        staging = Path(directory)
        site = staging / "site"
        site.mkdir()
        records = []
        for demo in DEMO_BUILDS:
            metadata = gh_json(f"repos/{demo['repository']}/actions/runs/{demo['run']}")
            if (metadata["status"] != "completed" or metadata["conclusion"] != "success"
                    or metadata["head_repository"]["full_name"] != demo["repository"]
                    or not re.fullmatch(r"[a-f0-9]{40}", metadata["head_sha"])):
                raise ValueError("Demo source is not a successful owner-repository deployment.")
            downloaded = staging / demo["prefix"]
            subprocess.run(["gh", "run", "download", str(demo["run"]), "--repo", demo["repository"],
                            "--name", "github-pages", "--dir", str(downloaded)], check=True, timeout=120)
            archives = list(downloaded.glob("*.tar"))
            if len(archives) != 1:
                raise ValueError("Expected exactly one Pages artifact archive.")
            extract_static(archives[0], site / demo["prefix"])
            digest = hashlib.file_digest(archives[0].open("rb"), "sha256").hexdigest()
            records.append({**demo, "commit": metadata["head_sha"], "artifact_sha256": digest,
                            "workflow_url": metadata["html_url"]})
            print(f"Verified {demo['label']}: {metadata['head_sha'][:12]}")
        render_directory(site, records)
        files = [path for path in site.rglob("*") if path.is_file()]
        if len(files) > 950 or sum(path.stat().st_size for path in files) > MAX_TOTAL:
            raise ValueError("Combined site exceeds the dashboard upload limits.")
        with zipfile.ZipFile(output_directory / "public-demos.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(files):
                archive.write(path, path.relative_to(site).as_posix())
        target = output_directory / "site"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(site, target)
    print(f"Public-only bundle: {len(files)} files at {output_directory / 'public-demos.zip'}")


def render_directory(site, records):
    (site / "deployment.json").write_text(json.dumps({"schema_version": 1, "mode": "public-static-reference",
        "projects": records, "private_backends": False,
        "omitted_development_templates": sorted(OMITTED_TEMPLATES)}, indent=2) + "\n", encoding="utf-8")
    rows = []
    for record in records:
        prefix = html.escape(record["prefix"], quote=True)
        repository = html.escape(record["repository"], quote=True)
        rows.append(f'<tr><th scope="row">{html.escape(record["label"])}</th>'
                    f'<td>{html.escape(record["mode"])}</td><td><a href="/{prefix}/">Open demo</a></td>'
                    f'<td><a href="https://github.com/{repository}">Source</a></td></tr>')
    font = next((site / "TravelBrain" / "assets").glob("dm-sans-latin-400-normal-*.woff2"), None)
    font_rule = (f"@font-face{{font-family:DemoSans;src:url('/{font.relative_to(site).as_posix()}') format('woff2');font-display:swap}}"
                 if font else "")
    css = font_rule + """
:root{font-family:DemoSans,Georgia,serif;color:#20352f;background:#f6f8f7;font-size:15px;letter-spacing:0}
*{box-sizing:border-box}body{margin:0}main{max-width:1100px;margin:auto;padding:48px 24px}header{border-bottom:1px solid #cbd9d2;padding-bottom:20px;margin-bottom:28px}h1{font-size:32px;margin:12px 0}p{line-height:1.6;color:#52665d}nav{display:flex;gap:22px;flex-wrap:wrap}a{color:#15664d;text-underline-offset:4px}a:focus-visible{outline:3px solid #bf8b22;outline-offset:4px}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:20px 12px;border-bottom:1px solid #d9e2dd;vertical-align:top}thead th{font-size:11px;text-transform:uppercase;color:#597164}tbody th{font-weight:400;color:#1c332a}td:nth-child(2){color:#5b6d64}section{padding:28px 0;border-bottom:1px solid #d9e2dd}h2{font-size:18px}footer{padding:24px 0;font-size:12px;color:#5b6d64}.directory-image{display:block;width:100%;height:130px;object-fit:cover;margin-bottom:24px}tbody a{white-space:nowrap}@media(max-width:650px){main{padding:25px 16px}h1{font-size:27px}table{font-size:12px}th,td{padding:16px 7px}th:first-child{width:25%}td:nth-child(2){width:32%}nav{font-size:12px;gap:14px}thead th{font-size:10px}.directory-image{height:105px}}@media(max-width:360px){table{font-size:11px}th,td{padding:14px 4px}}
"""
    (site / "directory.css").write_text(css, encoding="utf-8")
    body = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sushant Nemade | Public Project Demos</title><link rel="stylesheet" href="/directory.css"></head><body><main><header><nav><a href="https://sushant-nemade.github.io/">Portfolio</a><a href="https://github.com/Sushant-Nemade">GitHub</a><a href="/deployment.json">Build provenance</a></nav><h1>Sushant Nemade / Project Demos</h1><p>Public reference builds. Private owner APIs and model credentials are not published.</p></header><img class="directory-image" src="/TravelBrain/assets/paris.jpg" alt="Eiffel Tower in Paris, from the TravelBrain reference"><table><thead><tr><th>Project</th><th>Reference data</th><th>Demo</th><th>Code</th></tr></thead><tbody>""" + "".join(rows) + """</tbody></table><section><h2>Doclify</h2><p>Installable documentation CLI, not a hosted upload service.</p><a href="https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference">Download CLI and source</a></section><footer>Project licenses and credits remain inside each reference build. <a href="/TravelBrain/licenses.json">Directory photo/font credits</a>. Hosting does not certify live AI, market prices or production readiness.</footer></main></body></html>"""
    (site / "index.html").write_text(body, encoding="utf-8")
    (site / "404.html").write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Not found</title><h1>Not found</h1><a href="/">Project demos</a></html>', encoding="utf-8")
    (site / "_headers").write_text("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  X-Frame-Options: DENY\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Cache-Control: public, max-age=0, must-revalidate\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    build_bundle(options.output)


if __name__ == "__main__":
    main()