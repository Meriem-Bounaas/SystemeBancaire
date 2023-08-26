import unittest
from client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, 'bounaas', 'meriem')

    def test_creation_instance(self):
        self.assertIsInstance(self.client, Client)

    def test_client_str(self):
        oracle_test = f'id : 1\n first name : bounaas\n last name : meriem'
        resultat = self.client.__str__()
        self.assertEqual(resultat, oracle_test)

    def tearDown(self):
        pass
