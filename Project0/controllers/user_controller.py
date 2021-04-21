from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.users import Users
from services.user_services import UserService


def route(app):
    @app.route("/users", methods=['GET'])
    def get_all_users():
        return jsonify(UserService.all_users()), 200

    @app.route("/users/<user_id>", methods=['GET'])
    def get_user(user_id):
        try:
            user = UserService.get_by_uid(int(user_id))
            return jsonify(user.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/users", methods=["POST"])
    def post_user():
        user = Users.json_parse(request.json)
        user = UserService.create_user(user)
        return jsonify(user.json()), 201

    @app.route("/users/<user_id>", methods=["PUT"])
    def put_user(user_id):
        user = Users.json_parse(request.json)
        user.id = int(user_id)
        UserService.update_user(user)
        # print("-------Debug Lines controller-----")
        # print (user)
        return user.json(), 200

    @app.route("/users/<user_id>", methods=["DELETE"])
    def del_user(user_id):
        UserService.delete_user(int(user_id))
        return '', 204
