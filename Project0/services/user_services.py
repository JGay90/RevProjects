from dao.user_dao import UserDAO


# from exceptions.resource_unavailable import ResourceUnavailable


class UserService:
    user_dao = UserDAO

    @staticmethod
    def create_user(user):
        return UserDAO.create_user(user)

    @classmethod
    def all_users(cls):
        return UserDAO.get_all_users()

    @classmethod
    def get_by_uid(cls, user_id):
        return cls.user_dao.get_user(user_id)

    @staticmethod
    def update_user(user):
            UserDAO.update_user(user)
            # print("-------Service Debug Lines-----")
            # print(user)

    @classmethod
    def delete_user(cls,user_id):
       return cls.user_dao.delete_user(int(user_id))
