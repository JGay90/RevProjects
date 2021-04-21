from dao.account_dao import AccountDAO

class AccountService:

    acct_dao = AccountDAO

    @classmethod
    def create_acct(cls, acct):
        return cls.acct_dao.create_acct(acct)

    @classmethod
    def all_accts(cls):
        return AccountDAO.all_accts()

    @classmethod
    def get_by_aid(cls, acct_id):
        return cls.acct_dao.get_account(acct_id)

    @staticmethod
    def update_acct(acct):
        return AccountDAO.update_acct(acct)

    @staticmethod
    def delete_acct(acct_id):
        return AccountDAO.delete_acct(int(acct_id))

    @staticmethod
    def get_by_uid(uid):
        return AccountDAO.get_account_userid(uid)
    @staticmethod
    def get_by_uid_range(uid,high,low):
        return AccountDAO.get_account_userid_rng(int(uid),int(high),int(low))
    @staticmethod
    def withdrawl(aid,amount):
        return AccountDAO.withdrawl(aid,amount)
    @staticmethod
    def deposit(aid,amount):
        return AccountDAO.deposit(int(aid),amount)
