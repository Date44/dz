from config import db


class Users(object):
    @staticmethod
    def get_all_users() -> list:
        result = db.users.find()
        users = [n for n in result]
        return users
