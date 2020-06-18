import unittest
from app.models import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.new_client = Client(password = "rolex")

    def test_password_setter(self):
        self.assertTrue(self.new_client.password_hash is not None)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_client,Client))

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_client.password
    
    def test_password_verification(self):
        self.assertTrue(self.new_client.verify_password('rolex'))