from banque import Banque
from client import Client


if __name__ == '__main__':
    banque = Banque('BNP')
    client1 = Client(1, 'lucy', 'tchiwawa')
    client2 = Client(2, 'mimi', 'bounaas')
    banque.creation_compte(client1, 2000, 'lucycli', 'pass1')
    banque.creation_compte(client2, 8900, 'mimibou', 'pass2')
    print(banque)
    print(client1)
    print(client2)
    banque.affichage_detail_client(1)
