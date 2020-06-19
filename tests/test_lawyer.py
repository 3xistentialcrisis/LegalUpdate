import unittest
from app .models import Lawyers
class LawyerModelTest(unittest.TestCase):
    def setUp(self):
        self.new_lawyer = Lawyers(password = 'pass')
    def test_password_setter(self):
        self.assertTrue(self.new_lawyer.hash_pass is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_lawyer.password
    def test_password_verification(self):
        self.assertTrue(self.new_lawyer.verify_password('pass'))