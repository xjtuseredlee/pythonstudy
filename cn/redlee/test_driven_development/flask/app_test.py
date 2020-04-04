from cn.redlee.test_driven_development.flask.app import app
import json
import unittest

"""
this is my first app
"""


class AppTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.application = app.test_client()
        self.data = {"username": "redlee", "email": "email@gmail.com", "password": "12345", "address": "xi'an"}

    def test_login(self):
        response = self.application.get("/api/v1/login")
        result = json.loads(response.data.decode())
        self.assertEqual(result['status'], "ok")
        self.assertEqual(result['message'], "you are logined in.")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.application.post("/api/v1/register", data=json.dumps(self.data),
                                         content_type="application/json")
        result = json.loads(response.data.decode())
        self.assertEqual(result['username'], "redlee")
        self.assertEqual(result['email'], "email@gmail.com")
        self.assertEqual(result['password'], "12345")
        self.assertEqual(result['address'], "xi'an")
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
