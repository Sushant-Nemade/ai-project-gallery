import copy
import json
import unittest

from tools.catalog import ROOT, render, validate


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.document = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))

    def test_snapshot_and_primary_categories(self):
        validate(self.document)
        self.assertEqual(len(self.document["projects"]), 14)
        references = {project["id"] for project in self.document["projects"] if project["status"] == "reference"}
        self.assertEqual(references, {"ai-blog-publisher", "gitpulse", "doclify", "market-insight", "travelbrain", "airbnb-prices"})
        airbnb = next(project for project in self.document["projects"] if project["id"] == "airbnb-prices")
        self.assertEqual(airbnb["implementation"], "original")
        self.assertFalse(airbnb["upstream_code_imported"])
        self.assertIn("Not a current quote", airbnb["verification"])
        self.assertIn("NYC2019", airbnb["verification"])
        travelbrain = next(project for project in self.document["projects"] if project["id"] == "travelbrain")
        self.assertEqual(travelbrain["license"], "GPL-3.0-only")
        self.assertIn("Groq inference remains unverified", travelbrain["verification"])
        self.assertIn("illustrative", travelbrain["verification"])
        doclify = next(project for project in self.document["projects"] if project["id"] == "doclify")
        self.assertEqual(doclify["license"], "AGPL-3.0-only")
        self.assertIn("live Groq inference unverified", doclify["verification"])
        self.assertIn("Download the reference CLI and source", render(self.document))
        self.assertIn("live AI/search/R2 integrations unverified", render(self.document))
        self.assertTrue((ROOT / "docs/PROJECT_STATUS_AND_PENDING_WORK.md").is_file())
        self.assertIn("[Project status and pending work](docs/PROJECT_STATUS_AND_PENDING_WORK.md)", render(self.document))

    def test_duplicate_rejected(self):
        self.document["projects"].append(copy.deepcopy(self.document["projects"][0]))
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_multiple_active_projects_rejected(self):
        for project in self.document["projects"][:2]:
            project["status"] = "in_progress"
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_unattributed_release_rejected(self):
        del self.document["projects"][0]["license"]
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_other_source_rejected(self):
        self.document["projects"][1]["source"] = "https://github.com/another-owner/project"
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_original_requires_no_import_disclosure(self):
        original = next(project for project in self.document["projects"] if project["id"] == "gitpulse")
        original["upstream_code_imported"] = True
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_release_from_other_repository_rejected(self):
        doclify = next(project for project in self.document["projects"] if project["id"] == "doclify")
        doclify["release"] = "https://github.com/another-owner/project/releases/tag/v1"
        with self.assertRaises(ValueError):
            validate(self.document)

    def test_demo_origins_and_paths_are_exact(self):
        project = self.document["projects"][0]
        self.assertIn("https://sushant-ai-demos.pages.dev/ai-blog-publisher/", render(self.document))
        for address in ("http://localhost:8886/", "https://sushant-ai-demos.pages.dev.evil.test/ai-blog-publisher/",
                        "https://sushant-ai-demos.pages.dev/other-project/",
                        "https://sushant-ai-demos.pages.dev/ai-blog-publisher/?token=value"):
            with self.subTest(address=address):
                project["demo"] = address
                with self.assertRaises(ValueError):
                    validate(self.document)