class Users:

    def __init__(self, id= 0, un ='', first_name="", last_name="", accounts=[]):
        self.id = id
        self.username = un
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = accounts

    def __repr__(self):
        return repr(dict(id=self.id, first_name=self.first_name, last_name=self.last_name, accts=self.accounts))

    @classmethod
    def get_all(cls):
        pass

    def json(self):
        return {
            "userID" :self.id,
            "username" : self.username,
            "First Name": self.first_name,
            "Last Name" : self.last_name,
            "accounts" : self.accounts
        }

    @staticmethod
    def json_parse(json):
        user = Users()
        user.id = json["user_id"] if "user_id" in json else 0
        user.username = json["username"]
        user.first_name = json["first_name"]
        user.last_name = json["last_name"]
        user.accounts = []

        return user

    def print_accts(self):
        return [self.accounts]


