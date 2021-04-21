from exceptions.resource_not_found import ResourceNotFound
from exceptions.nsf import NonSufficientFunds
from models.accounts import Accounts
from util.db_connection import connection
from random import randint as ri

class AccountDAO:

    @staticmethod
    def create_acct(account):
        sql = "Insert into banking.accounts values (default,%s,%s,%s) returning *"
        cursor = connection.cursor()
        cursor.execute(sql,(account.acct_num, account.balance, account.userid))
        connection.commit()
        record = cursor.fetchone()
        new_acct = Accounts(record[0], record[1], record[2], record[3])
        return new_acct

    @staticmethod
    def get_account(acct_id):
        try:
            sql = "SELECT * FROM banking.accounts where acctid = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [acct_id])
            records = cursor.fetchall()
            for record in records:
                acct1 = Accounts(int(record[0]), int(record[1]), int(record[2]), int(record[3]))
            return acct1
        except KeyError:
            raise ResourceNotFound(f"Account with id: {acct_id} - NOT FOUND")

    @staticmethod
    def all_accts():
        sql = "SELECT * FROM banking.accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        acct_list = []

        for record in records:
            acct = Accounts(record[0], record[1], record[2], record[3])
            acct_list.append(acct.json())

        return acct_list

    @staticmethod
    def update_acct(acct):
        sql = "UPDATE banking.accounts SET acctnum = %s,balance= %s, userid = %s WHERE acctid = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (acct.acct_num,acct.balance,acct.userid, acct.acct_id))
        connection.commit()

        record = cursor.fetchone()
        acct1 = Accounts(int(record[0]), int(record[1]), int(record[2]),int(record[3]))
        return acct1


    @staticmethod
    def delete_acct(acct_id):
        sql = "DELETE FROM banking.accounts WHERE acctid = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [acct_id])
        connection.commit()

    @staticmethod
    def get_account_userid(userid):
        sql = "SELECT * FROM banking.accounts where userid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [userid])
        records = cursor.fetchall()
        acct_list = []

        for record in records:
            acct = Accounts(record[0], record[1], record[2], record[3])
            acct_list.append(acct.json())

        return acct_list

    @staticmethod
    def get_account_userid_rng(userid,high,low):
        sql = "SELECT * FROM banking.accounts where userid = %s and balance <= %s and balance >=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [userid],[high],[low])
        records = cursor.fetchall()
        acct_list = []
        for record in records:
            acct = Accounts(record[0], record[1], record[2], record[3])
            if float(acct.balance) <int(high) and float(acct.balance) > int(low):
                acct_list.append(acct.json())
            else:
                acct_list.clear()
        return acct_list

    @staticmethod
    def withdrawl(aid,amount):
        acct = AccountDAO.get_account(aid)
        try:
            if float(amount) <= float(acct.balance) and float(amount)>= 0:
                acct.balance = float(acct.balance) - float(amount)
                AccountDAO.update_acct(acct)
                return acct

        except KeyError :
             raise NonSufficientFunds("Not enough funds for Transaction")


    @staticmethod
    def deposit(aid,amount):
        try:
            if float(amount) >= 0:
                acct = AccountDAO.get_account(aid)
                acct.balance = float(acct.balance) + float(amount)
                AccountDAO.update_acct(acct)
                return acct
        except KeyError:
            raise NonSufficientFunds("Not enough funds for Transaction")


def _test():
    adao = AccountDAO()

    accounts = adao.all_accts()
    print(accounts)

if __name__ == '__main__':
    _test()