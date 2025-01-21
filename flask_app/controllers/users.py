from flask_app import app
from flask import redirect,request,render_template,session
from flask_app.models.users import user
from flask_app.models.books import books


# @app.route('/dashboard')
# def root():
#     return redirect('/users')
@app.route('/dashboard')
def user1():
    data = {'id':session['user_id']}
    users = user.user_favorite_book(data)
    books1 = books.get_books()
    return render_template("user_dashboard.html",users = users, books1 = books1)

@app.route('/users/add_user', methods=["POST"])
def add_user():
    data ={
        "user_name":request.form["user_name"]
    }
    user.insert_user(data)
    return redirect("/users")

# view users profile with books
# @app.route('/view_user/<int:user_id>')
# def view_user(user_id):
#     data ={
#         "id":user_id
#     }
#     users = user.user_favorite_book(data)
#     books1 = books.get_books()
#     print(books1)
#     #need to get the imformation from books where the books and user have the same user_id and books_id in favorites 
#     return render_template("user_dashboard.html", users = users, books = books1)

@app.route("/add_book_favorite/<int:user_id>", methods=["POST"])
def add_new_favorite_book(user_id):
    data={
        "user_id":user_id,
        "book_id":request.form["book"]
    }
    user.add_favorite_book(data)
    return redirect("/dashboard")