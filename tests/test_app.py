"""Smoke tests using the stdlib unittest module."""

import unittest

from app import create_app
from app import routes


class TestIndex(unittest.TestCase):
    def setUp(self):
        routes._notes.clear()
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def test_index_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"notes-cicd-app", response.data)

    def test_post_adds_note(self):
        self.client.post("/", data={"note": "  Hello  "}, follow_redirects=True)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello", response.data)


if __name__ == "__main__":
    unittest.main()
