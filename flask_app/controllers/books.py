from flask_app import app
from flask import redirect,request,render_template
from flask_app.models.books import books  
from flask_app.models.users import user

@app.route('/books')
def book_library():
    books1 =books.get_books()
    return render_template("book_library.html", books1 =books1)

@app.route('/add_book',methods =["POST"])
def add_book():
    data ={
        "title":request.form["title"],
        "number_of_pages":request.form["number_of_pages"]
    }
    
    books.add_book(data)
    return redirect('/books')

@app.route("/books_dashboard/<int:book_id>")
def dashboard(book_id):
    # get user information that like this books
    data ={
        "id":book_id
    }    
    # having a many to many join to get both books and users information
    favor_books= books.book_favorite_user(data)
    user_list = user.get_users()
    #print("users: ",user_list)
    #print("favorite books: ",favor_books)
    return render_template("book_dashboard.html",favor_books =favor_books,book_id =book_id, user_list=user_list)

@app.route("/user_fav/<int:book_id>", methods=["POST"])
def user_fav(book_id):
    data={
        'user_id':request.form["user"],
        'book_id':book_id
    }
    books.add_favorite_user(data)
    return redirect(f"/books_dashboard/{book_id}")