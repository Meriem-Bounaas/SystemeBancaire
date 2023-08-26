import unittest
from banque import Banque
from client import Client


class TestBanque(unittest.TestCase):

    def setUp(self):
        self.banque = Banque('Bnp Paribas')
        self.client = Client(1, 'bounaas', 'meriem')

    def test_creation_banque(self):
        self.assertIsInstance(self.banque, Banque)

    def test_creation_compte(self):
        self.banque.creation_compte(self.client, 2000, 'meriembou', '12345')
        self.assertEqual(len(self.banque.liste_des_comptes), 1)
        self.assertEqual(
            self.banque.liste_des_comptes[0].username, 'meriembou')

    def test_affichage_detail_client(self):
        self.banque.creation_compte(self.client, 2000, 'meriembou', '12345')
        resultat = self.banque.affichage_detail_client(1).__str__()
        oracle_test = f'id : 1\n first name : bounaas\n last name : meriem'
        self.assertEqual(resultat, oracle_test)

    def test_consultation_compte(self):
        compte = self.banque.creation_compte(
            self.client, 2000, 'meriembou', '12345')
        resultat = self.banque.consultation_compte(compte.account_number)
        oracle_test = 'votre solde est : 2000 euros'
        self.assertEqual(resultat, oracle_test)

    def test_authentification_not_login(self):
        self.banque.creation_compte(self.client, 2000, 'meriembou', '12345')
        self.banque.authentification('meriembou', '12345')
        resultat = self.banque.liste_des_comptes[0].is_authentified
        oracle_test = True
        self.assertEqual(resultat, oracle_test)

    def test_deconnexion(self):
        self.banque.creation_compte(self.client, 2000, 'meriembou', '12345')
        self.banque.authentification('meriembou', '12345')
        self.banque.deconexion('meriembou')
        resultat = self.banque.liste_des_comptes[0].is_authentified
        oracle_test = False
        self.assertEqual(resultat, oracle_test)

    def test_cloture(self):
        compte = self.banque.creation_compte(
            self.client, 2000, 'meriembou', '12345')
        self.banque.cloture_compte(compte.account_number)
        resultat = self.banque.consultation_compte(compte.account_number)
        oracle_test = None
        self.assertEqual(resultat, oracle_test)

    def test_virement_compte_a_compte(self):
        compte_1 = self.banque.creation_compte(
            self.client, 100, 'lucy_99', '87870')
        compte_2 = self.banque.creation_compte(
            self.client, 2000, 'meriembou', '12345')
        self.banque.authentification('lucy_99', '87870')
        self.banque.virement_compte_a_compte(
            compte_1.account_number, compte_2.account_number, 50)
        oracle_test = 50
        self.assertEqual(compte_1.balance, oracle_test)
        self.assertEqual(compte_2.balance, 2050)

    def test_retrait_argent(self):
        compte = self.banque.creation_compte(
            self.client, 2000, 'meriembou', '12345')
        self.banque.authentification('meriembou', '12345')
        self.banque.retrait_argent(compte.account_number, 100)
        self.assertEqual(compte.balance, 1900)

    def test_deposer_argent(self):
        compte = self.banque.creation_compte(
            self.client, 2000, 'meriembou', '12345')
        self.banque.authentification('meriembou', '12345')
        self.banque.deposer_argent(compte.account_number, 1000)
        self.assertEqual(compte.balance, 3000)
