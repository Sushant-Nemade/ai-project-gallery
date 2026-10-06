import argparse
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://github.com/KalyanM45/AI-Project-Gallery"
STATES = {"planned", "in_progress", "reference", "blocked"}


def github_url(value, owners):
    parsed = urlparse(value)
    parts = parsed.path.strip("/").split("/")
    return (parsed.scheme == "https" and parsed.netloc == "github.com" and not parsed.query
            and not parsed.fragment and len(parts) == 2 and parts[0] in owners and bool(parts[1]))


def validate(document):
    if document.get("schema_version") != 1 or document.get("source_gallery") != SOURCE:
        raise ValueError("unsupported schema or source gallery")
    date.fromisoformat(document["eligibility_reviewed_on"])
    categories = document["categories"]
    if not isinstance(categories, dict) or not categories:
        raise ValueError("categories required")
    identifiers = set()
    active = 0
    for project in document["projects"]:
        identifier = project["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier) or identifier in identifiers:
            raise ValueError("invalid or duplicate project id")
        identifiers.add(identifier)
        if project["category"] not in categories or project["status"] not in STATES:
            raise ValueError("unknown primary category or status")
        if not github_url(project["source"], {"KalyanM45", "KalyanMurapaka45"}):
            raise ValueError("project source must come from the gallery author")
        active += project["status"] == "in_progress"
        if project.get("implementation") == "original" and (
                project.get("upstream_code_imported") is not False or not project.get("source_license")):
            raise ValueError("original implementation requires explicit no-import and source-license disclosure")
        if project["status"] == "reference":
            if (not project.get("license") or not re.fullmatch(r"[a-f0-9]{40}", project.get("source_commit", ""))
                    or not github_url(project.get("repository", ""), {"Sushant-Nemade"})
                    or not project.get("verification")):
                raise ValueError("published reference requires attribution and verification evidence")
            if project.get("demo") and not project["demo"].startswith("https://sushant-nemade.github.io/"):
                raise ValueError("demo must belong to the destination portfolio")
    if active > 1:
        raise ValueError("only one project may be in progress")
    return document


def render(document):
    validate(document)
    lines = ["# Projects", "", "Sushant Nemade's categorized AI project portfolio.", "",
             f"Discovery source: [{SOURCE}]({SOURCE}). Eligibility snapshot: {document['eligibility_reviewed_on']}.", "",
             "One project is implemented at a time. Source-gallery end-to-end checkmarks are eligibility signals, not production certification.",
             "Planned entries are links only: their code, data, model licenses and runtime still require audit.", "",
             "## Published Reference Implementations", ""]
    for project in document["projects"]:
        if project["status"] != "reference":
            continue
        source_notice = (f"Concept reference: [{project['source']}]({project['source']}); source license: {project['source_license']}. "
                 f"No upstream code imported; original implementation license: {project['license']}; specification revision: `{project['source_commit']}`."
                 if project.get("implementation") == "original" else
                 f"Source: [{project['source']}]({project['source']}); license: {project['license']}; upstream revision: `{project['source_commit']}`.")
        lines += [f"### [{project['name']}]({project['repository']})", "",
                  f"Primary category: **{document['categories'][project['category']]}**. Portfolio placement: **{project['portfolio_category']}**.",
              source_notice,
                  f"Verification: {project['verification']}"]
        if project.get("demo"):
            lines.append(f"[Synthetic reference demo]({project['demo']})")
        lines.append("")
    lines += ["## Categorized Backlog", ""]
    for category, label in document["categories"].items():
        lines += [f"### {label}", ""]
        for project in document["projects"]:
            if project["category"] == category:
                lines.append(f"- [{project['name']}]({project.get('repository', project['source'])}) - {project['status']}")
        lines.append("")
    active_name = next((project["name"] for project in document["projects"] if project["status"] == "in_progress"), None)
    pending_name = next((project["name"] for project in document["projects"] if project["status"] == "planned"), "None")
    lines += ["## Delivery Policy", "", f"Active implementation: {active_name or 'none'}. Next pending candidate: {pending_name}, subject to fresh license and runnable-path audits.",
              "No automatic daily imports or unattended publishing. Return in a later session to request the next project.",
              "Healthcare and financial examples remain educational until separately validated for any proposed real use.", "",
              "[Release checklist](docs/RELEASE_CHECKLIST.md) | [Portfolio](https://sushant-nemade.github.io/)", "",
              "## Maintain the Catalog", "", "```text", "python -m tools.catalog", "python -m tools.catalog --check",
              "python -m unittest discover -s tests -v", "```", "",
              "Edit projects.json, then regenerate this README. Preserve source attribution and distinguish local tests from live integration evidence.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    document = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    expected = render(document)
    readme = ROOT / "README.md"
    if args.check:
        if not readme.is_file() or readme.read_text(encoding="utf-8") != expected:
            raise ValueError("README does not match projects.json; regenerate the catalog")
    else:
        readme.write_text(expected, encoding="utf-8", newline="\n")
    references = sum(project["status"] == "reference" for project in document["projects"])
    print(f"Catalog verified: {len(document['projects'])} candidates, {references} reference implementation(s)")


if __name__ == "__main__":
    main()