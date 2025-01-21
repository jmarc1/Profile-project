from flask import flash
from flask_app.config.myConnection import connect_to_mysql

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class user_login:
    db = "books_schema"
    def __ini__(self,data):
        self.id = data["id"]
        self.first_name=data["first_name"]
        self.last_name = data["last_name"]
        self.dob = data["dob"]
        self.phone= data["phone"]
        self.email =data["email"]
        self.passwd = data["passwd"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_info(cls,data):
        query = """SELECT * FROM users WHERE email= %(email)s;"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        return info
    
    @classmethod
    def get_users(cls):
        query = """SELECT * FROM users;"""
        info = connect_to_mysql(cls.db).query_db(query)
        return info
    
    @staticmethod
    def isValid(data,category):
        valid = True
        if not EMAIL_REGEX.match(data["email"]):
            flash("Check email format",category)
            valid = False
        if len(data["email"]) <3:
            flash("email/password can't be empty!",category)
            valid= False
        return valid
    
    @classmethod
    def update_passwd(cls,data):
        query = """UPDATE users SET passwd =%(passwd)s where email=%(email)s"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls