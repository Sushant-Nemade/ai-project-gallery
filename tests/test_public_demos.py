import io
from pathlib import Path
import tarfile
import tempfile
import unittest

from tools.public_demos import extract_static


class StaticBundleTests(unittest.TestCase):
    def archive(self, root, extra=None):
        path = Path(root) / "artifact.tar"
        with tarfile.open(path, "w") as archive:
            payload = b"<html>Reference</html>"
            member = tarfile.TarInfo("./index.html")
            member.size = len(payload)
            archive.addfile(member, io.BytesIO(payload))
            if extra:
                member = tarfile.TarInfo(extra)
                member.size = 4
                archive.addfile(member, io.BytesIO(b"data"))
        return path

    def test_extracts_only_static_content(self):
        for name in ("assets/app.js", "js/vendor/dompurify.LICENSE-MPL", "licenses/zod-LICENSE"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                target = Path(directory) / "site"
                extract_static(self.archive(directory, name), target)
                self.assertEqual((target / name).read_bytes(), b"data")

    def test_rejects_private_paths_and_server_code(self):
        for name in ("../escape.js", "/absolute.js", "C:/escape.js", "assets\\escape.js",
                     ".env", "nested/.env.production", "trips.sqlite", "data/report.json",
                     "app.py", "_worker.js", "functions/api.js"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    extract_static(self.archive(directory, name), Path(directory) / "site")

    def test_omits_only_known_development_template(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "site"
            extract_static(self.archive(directory, "js/config.js.example"), target)
            self.assertTrue((target / "index.html").is_file())
            self.assertFalse((target / "js/config.js.example").exists())

    def test_rejects_links_and_duplicates(self):
        for duplicate in (False, True):
            with tempfile.TemporaryDirectory() as directory:
                path = self.archive(directory)
                with tarfile.open(path, "a") as archive:
                    member = tarfile.TarInfo("INDEX.html" if duplicate else "linked.js")
                    if not duplicate:
                        member.type = tarfile.SYMTYPE
                        member.linkname = "../../outside"
                    archive.addfile(member)
                with self.assertRaises(ValueError):
                    extract_static(path, Path(directory) / "site")


if __name__ == "__main__":
    unittest.main()