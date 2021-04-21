class Accounts:
    def __init__(self, acct_id = 0, acct_num = 0, balance=0, userid = 0):
        self.acct_id = acct_id
        self.acct_num = acct_num
        self.userid = userid
        self.balance = balance


    def __repr__(self):
        return repr(dict(acct_num=self.acct_num, userid=self.userid, balance=self.balance))

    def json(self):
        return {
            "acct_id" : self.acct_id,
            "acct_num" : self.acct_num,
            "balance" : self.balance,
            "user_id": self.userid
        }

    @staticmethod
    def json_parse(json):
        acct = Accounts()
        acct.acct_id = json["acct_id"] if "acct_id" in json else 0
        acct.acct_num = json["acct_num"]
        acct.balance = json["balance"]
        acct.userid = json["user_id"]

        return acct

