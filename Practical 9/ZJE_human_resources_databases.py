class Staff(object):
    def __init__(self,firstname,lastname,location,role):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.role = role
        self.fullname = self.firstname + ' ' + self.lastname

man = Staff('Yunshuo','Zhang','China','student')
print(man.fullname,man.location,man.role)