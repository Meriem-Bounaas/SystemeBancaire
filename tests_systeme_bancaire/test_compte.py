import unittest
from compte import Compte
from client import Client


class TestCompte(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, 'meriem', 'bounaas')
        self.compte = Compte(self.client, 2000, 'meriembou', '12345')

    def test_create_compte_instance(self):
        self.assertIsInstance(self.compte, Compte)

    # @unittest.skip(" a tout a l'heure")
    def test_log_in(self):
        self.compte.log_in('meriembou', '12345')
        resultat = self.compte.is_authentified
        oracle_test = True
        self.assertEqual(resultat, oracle_test)

    def test_log_in_error(self):
        self.compte.log_in('meriembou', '125')
        resultat = self.compte.is_authentified
        oracle_test = False
        self.assertEqual(resultat, oracle_test)
