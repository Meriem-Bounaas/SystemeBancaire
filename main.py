from banque import Banque
from client import Client


if __name__ == '__main__':
    banque = Banque('BNP')
    client = Client(1, 'lucy', 'tchiwawa')
    banque.creation_compte(client, 2000, 'usernas', 'pass')
    print(banque)
    # print(client)
    banque.affichage_detail_client(1)
