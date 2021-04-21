from exceptions.resource_not_found import ResourceNotFound
from models.users import Users
from util.db_connection import connection



class UserDAO:

    @staticmethod
    def create_user(user):
        sql = "Insert into banking.users Values(default,%s,%s,%s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (user.username, user.first_name, user.last_name))
        connection.commit()
        record = cursor.fetchone()
        new_user = Users(record[0], record[1], record[2], record[3])
        return new_user

    @staticmethod
    def get_user(user_id):
        sql = "SELECT * FROM banking.users where userid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        record = cursor.fetchone()

        if record:
            return Users(record[0], record[1], record[2], record[3])
        else:
            raise ResourceNotFound(f"User with ID {user_id} - Not Found")

    @staticmethod
    def get_all_users():
        sql = "SELECT * FROM banking.users"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        user_list = []

        for record in records:
            user = Users(record[0], record[1], record[2], record[3])
            user_list.append(user.json())

        return user_list
    @staticmethod
    def delete_user(user_id):
        sql = "DELETE FROM banking.users WHERE userid = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
    @staticmethod
    def update_user(user):
        sql = "UPDATE banking.users SET username=%s,first_name=%s,last_name=%s WHERE userid = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (user.username, user.first_name, user.last_name, user.id))
        connection.commit()

        record = cursor.fetchone()

        u = Users(int(record[0]), record[1], record[2], record[3])
        # print('-----Dao Debug lines-----')
        # print(u)

        return u

def _test():
    udao = UserDAO()
    users = udao.get_all_users()
    print(users)

    print(udao.get_user(1))


if __name__ == '__main__':
    _test()
