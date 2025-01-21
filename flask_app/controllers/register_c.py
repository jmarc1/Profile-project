from flask_app import app
from flask import redirect,request,render_template,session,flash
from flask_bcrypt import Bcrypt
from flask_app.models.register_model import register1
import re
bcrypt =  Bcrypt(app)
PASSWORD_REGEX = re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}')
phone_regex = re.compile(r'[0-9]{10,}')

@app.route('/register-user', methods =["POST"])
def register_new():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "dob":request.form["dob"],
        "phone":request.form["phone"],
        "email":request.form["email"],
        "passwd":None
    }
    #print(PASSWORD_REGEX)
    if register1.isValid(data) != True:
        return redirect('/register_user')
    if request.form["passwd"] != request.form["confirm_passwd"]:
        flash("Invalid Email/Password")
        return redirect('/')
    elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,}',request.form["passwd"]):
        flash("Invalid PASSWORD requirement {{PASSWORD_REGEX}}")
        return redirect('/register_user')
    else:
        data["passwd"] = bcrypt.generate_password_hash(request.form["passwd"])
        register1.add_user(data)
        userinf = register1.user_by_email(data)
        session["user"] = data["first_name"]
        session["user_id"] = userinf[0]["id"]
        return redirect('/dashboard')