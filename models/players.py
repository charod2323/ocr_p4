class Player:
    def __init__(self, lastname, firstname, age, birth_date, sex):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.birth_date = birth_date
        self.sex = sex


    def getusername(self):
        return self.lastname