class InscriptionOnLine:


    def inscription(self,name,firstname):
        self.name = name
        self.firstname = firstname


class PresenceRegistration:


    def registre(self,presence_name,presence_firstname):
        self.presence_name = presence_name
        self.presence_first = presence_firstname


class  PermissionEnterTournament(InscriptionOnLine,PresenceRegistration):


    def enter_confirmation(self,enter_confirmation_yes,enter_confirmation_no):
        self.enter_confirmation_yes = enter_confirmation_yes
        self.enter_confirmation_no = enter_confirmation_no


    def verification_enter(self,name,presence_name):
        self.name = name
        self.presence_name = presence_name
        if self.name == self.presence_name:
            print("verification: ok")
        else:
            print("not allow!")


class  GivePlayerNumbers:


    def my_number(self,my_number):
        self.my_number = my_number



