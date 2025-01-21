from flask_app.config.myConnection import connect_to_mysql


class books:
    db="books_schema"
    def __init__(self,data):
        self.id =data["id"]
        self.title=data["title"]
        self.number_of_pages = data["number_of_page"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_books(cls):
        query = """SELECT * FROM books;"""
        data = connect_to_mysql(cls.db).query_db(query)
        return data
    
    
    @classmethod
    def get_book(cls,data):
        query = """SELECT * FROM books WHERE id=%(id)s"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        return info
    
    
    @classmethod 
    def add_book(cls,data):
        query ="""INSERT INTO books(title,number_of_pages,created_at) VALUES(%(title)s,%(number_of_pages)s,NOW())"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls
    
    @classmethod
    def update_book(cls,data):
        query = """UPDATE boooks SET title =%(title)s,%(number_of_pages)s,updated_at=NOW() WHERE id=%(id);"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls
    
    @classmethod
    def book_favorite_user(cls,data):
        query = """select users.id, users.first_name,users.last_name,books.title,books.id from books
                left join favorites on books.id = favorites.book_id
                left join users on users.id = favorites.user_id
                where books.id = %(id)s;"""
        info =connect_to_mysql(cls.db).query_db(query,data)
        return info
    
    @classmethod
    def add_favorite_user(cls,data):
        query = """INSERT INTO favorites(user_id,book_id) values(%(user_id)s,%(book_id)s);"""
        connect_to_mysql(cls.db).query_db(query,data)
        return cls