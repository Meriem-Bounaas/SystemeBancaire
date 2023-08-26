class Client:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'id : {self.id}\n first name : {self.firstname}\n last name : {self.lastname}'
