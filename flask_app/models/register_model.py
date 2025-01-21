from flask_app.config.myConnection import connect_to_mysql
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}')
class register1:
    db = "books_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.dob = data["dob"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.passwd = data["passwd"]
        self.created_at = data["created_at"]
        self.updated_at =data["updated_at"]
        
    @classmethod
    def get_users(cls):
        query = """SELECT * from users"""
        data = connect_to_mysql(cls.db).query_db(query)
        return data
    
    
    @classmethod
    def add_user(cls,data):
        query ="""INSERT INTO users(first_name,last_name,dob,phone,email,passwd,created_at) VALUES(%(first_name)s,%(last_name)s,%(dob)s,%(phone)s,%(email)s,%(passwd)s,NOW());"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls
    
    @classmethod
    def user_by_email(cls,data):
        query = """SELECT * FROM users where email=%(email)s"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        return info
    
    @staticmethod
    def isValid(data,category):
        valid =True
        if len(data) > 2:
            if len(data["first_name"]) <3:
                flash("first name need length greater than 2",category)
                valid=False
            if len(data["last_name"]) <3:
                flash("Last name length must be greater than 2",category)
                valid=False
            if not EMAIL_REGEX.match(data["email"]):
                flash("Invalid email address",category)
                valid=False
        else:
            if data["email"] == 0:
                valid = False
                flash("email/password are empty",category)
        return valid