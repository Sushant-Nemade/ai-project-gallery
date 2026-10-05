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
        self.assertEqual(sum(project["status"] == "reference" for project in self.document["projects"]), 1)
        self.assertIn("live AI/search/R2 integrations unverified", render(self.document))

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