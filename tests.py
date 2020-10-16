import unittest
from app import app
import json


class TestFlaskStarShip(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_index_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_content_type(self):
        response = self.client.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_get_starships(self):
        response = self.client.get("/starships")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")


if __name__ == '__main__':
    unittest.main()
