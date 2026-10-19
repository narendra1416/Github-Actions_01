import unittest

from app import create_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_home_returns_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello from Flask on Minikube!"})

    def test_health_returns_ok(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
