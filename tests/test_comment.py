import unittest
from app.models import Case, Client, Comment

class TestCase(unittest.TestCase):
    
    def setUp(self):
        self.client_Stephen = Client(full_name = "Stephen Remmi",
                                username = "stephen_m",
                                password = "easy",
                                email = "remmi@mail.com")
        self.new_post = Case(post_title = "Sample Title",
                            case_content = "Hallo Welt! Ich bin hier",
                            client_id = self.client_Stephen.id)
        self.new_comment = Comment(comment = "Nice job",
                                    client_id = self.new_case.case_id,
                                    client_id = self.client_Stephen.id)

    def tearDown(self):
        Case.query.delete()
        Client.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.client_Stephen, Client))
        self.assertTrue(isinstance(self.new_case, Case))
        self.assertTrue(isinstance(self.new_comment, Comment))