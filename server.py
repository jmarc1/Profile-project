from flask_app import app
from flask_app.controllers import index_page
from flask_app.controllers import books
from flask_app.controllers import users
from flask_app.controllers import register_c
from flask_app.controllers import login_c

if __name__ == "__main__":
    app.run(debug=True)