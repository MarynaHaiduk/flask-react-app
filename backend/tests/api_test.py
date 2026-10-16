import unittest
import requests

class TestAPI(unittest.TestCase):
    url = "http://127.0.0.1:5000/"

    def test_hello(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status.code, 200)
        self.assertEqual((len(resp.json()), 4))
        print("Test completed")
