from flask import jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from models.accounts import Accounts
from services.account_services import AccountService
from dao.user_dao import UserDAO


def route(app):

    @app.route("/users/<userid>/accounts", methods=['GET'])
    def all_accts_by_uid(userid):
        try:
            acct_list = AccountService.get_by_uid(int(userid))
            user = UserDAO.get_user(userid)
            for accts in acct_list:
                user.accounts.append(accts)
            return user.accounts.__str__(),200
        except ValueError as e:
            return "No valid Accounts", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/users/<user_id>/account", methods=['POST'])
    def new_acct_uid(user_id):
        acct = Accounts.json_parse(request.json)
        acct = AccountService.create_acct(acct)
        return jsonify(acct.json()), 201

    @app.route("/users/<user_id>/accounts/<acct_id>",methods=['Delete'])
    def delete_acct_uid(user_id,acct_id):
        for user_id in UserDAO.get_all_users():
            AccountService.delete_acct(int(acct_id))
            return '', 204
        else:
            raise ResourceNotFound(f"User with ID {user_id} - Not Found")

    @app.route("/users/<user_id>/accounts/<acct_id>", methods=['GET'])
    def get_acct_aid(user_id,acct_id):
        acct = AccountService.get_by_aid(acct_id)
        return acct.__str__(),200

    @app.route("/user/<user_id>/accounts/<acct_id>", methods=['PUT'])
    def put_acct(user_id,acct_id):
        acct = Accounts.json_parse(request.json)
        acct.userid = int(user_id)
        acct.acct_id = int(acct_id)

        AccountService.update_acct(acct)
        return acct.json(), 200

    @app.route("/users/<user_id>/accounts/<acct_id>", methods=['PATCH'])
    def patch_acct(user_id,acct_id):
        acct = AccountService.get_by_aid(acct_id)
        action = request.json['action']
        if action == 'withdrawl' or action == 'deposit':
            try:
                amount = request.json['amount']
                if action == 'withdrawl':

                    acct = AccountService.withdrawl(acct_id,amount)
                    return acct.__str__(),200
                elif action == 'deposit':
                    acct = AccountService.deposit(acct_id,amount)
                    return acct.__str__(),200
            except ValueError as e:
                return "No valid Accounts", 400  # Bad Request
            except ResourceNotFound as r:
                return r.message, 404
    @app.route("/users/<user_id>/accounts?amountLessThan=<high>&amountGreaterThan<low>", methods=['GET'])
    def get_acct_range(user_id,high,low):
        try:
            acct_list = AccountService.get_by_uid_range(int(user_id),high,low)
            user = UserDAO.get_user(user_id)
            for accts in acct_list:
                user.accounts.append(accts)
            return user.accounts.__str__(), 200
        except ValueError as e:
            return "No valid Accounts", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404