from flask_app.config.myConnection import connect_to_mysql

class user:
    db = "books_schema"
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at =data["created_at"]
        self.updated_At=data["updated_at"]
        
    @classmethod
    def get_users(cls):
        query = """SELECT * FROM users;"""
        data =connect_to_mysql(cls.db).query_db(query)
        return data
    
    @classmethod
    def one_user(cls,data):
        query = """SELECT * FROM users WHERE id=%(id)s"""
        data = connect_to_mysql(cls.db).query_db(query,data)
        return data
    
    # @classmethod
    # def insert_user(cls,data):
    #     query = """INSERT INTO users(,created_at) VALUES(%(user_name)s,NOW())"""
    #     connect_to_mysql(cls.db).query_db(query,data)
    #     return cls
    
    # getting all the information from all tables using a join query
    # getting all the books that one user favore
    # getting all the users who favore a single book
    @classmethod
    def user_favorite_book(cls,data):
        query = """select first_name,last_name,books.title,books.number_of_pages,books.id from users
                    left join favorites on users.id = favorites.user_id
                    left join books on books.id = favorites.book_id
                    where users.id = %(id)s;"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        print(info)
        return info
    
    @classmethod
    def add_favorite_book(cls, data):
        query = """INSERT INTO favorites(user_id,book_id) values(%(user_id)s,%(book_id)s)"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls