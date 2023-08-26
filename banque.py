from compte import Compte


class Banque:
    def __init__(self, nom_du_banque):
        self.nom_du_banque = nom_du_banque
        self.liste_des_comptes = []

    def creation_compte(self, client, balance, username, password):
        compte = Compte(client, balance, username, password)
        self.liste_des_comptes.append(compte)
        return compte

    def affichage_detail_client(self, id_client):
        for compte in self.liste_des_comptes:
            if compte.client.id == id_client:
                print(compte.client)
                return compte.client

    def consultation_compte(self, account_number):
        for compte in self.liste_des_comptes:
            if account_number == compte.account_number:
                print(f'votre solde est : {compte.balance} euros')
                return f'votre solde est : {compte.balance} euros'

    def authentification(self, username, password):
        for compte in self.liste_des_comptes:
            if compte.username == username:
                compte.log_in(username, password)
                break

    def deconexion(self, username):
        for compte in self.liste_des_comptes:
            if compte.username == username:
                compte.log_out()
                break

    def get_compte_by_account_number(self, account_number):
        for compte in self.liste_des_comptes:
            if compte.account_number == account_number:
                return compte
        return None

    def virement_compte_a_compte(self, from_account_number, to_account_number, amount):
        from_account = self.get_compte_by_account_number(from_account_number)
        to_account = self.get_compte_by_account_number(to_account_number)
        if from_account.is_authentified:
            if (from_account is not None) and (to_account is not None):
                if from_account.balance >= amount:
                    to_account.balance += amount
                    from_account.balance -= amount
                else:
                    raise Exception(
                        'votre solde ne suffit pas pour un transfere')
            else:
                raise Exception('un compte n\'exist pas dans ce transfer')
        else:
            raise Exception('voulez vous connecter au systeme')

    def cloture_compte(self, account_number):
        compte_trouve = None
        for compte in self.liste_des_comptes:
            if compte.account_number == account_number:
                compte_trouve = compte
                break
        if compte_trouve is not None:
            self.liste_des_comptes.remove(compte_trouve)

    def retrait_argent(self, account_number, amount):
        compte = self.get_compte_by_account_number(account_number)
        compte.retrait_argent(amount)

    def deposer_argent(self, account_number, amount):
        compte = self.get_compte_by_account_number(account_number)
        compte.deposer_argent(amount)

    def __str__(self):
        return f'La Banque {self.nom_du_banque} : {len(self.liste_des_comptes)} comptes'
