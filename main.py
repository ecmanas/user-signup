from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('forms.html')


@app.route("/hello", methods=['POST'])
def validate_info():
    username = str(request.form['username'])
    username_from_form = username
    username_error = ''

    if len(username_from_form) < 3:
        username_error = "username must be longer than 3 characters"
    
    if len(username_from_form) > 20:
        username_error = "username cannot be longer than 20 characters"

    if " " in username_from_form:
        username_error = "username may not contain spaces"

    password = str(request.form['password'])
    password_verification = str(request.form['password_verification'])
    password_error = ''

    if password != password_verification:
        password_error = "passwords must match, please re-enter"

    if len(password) < 3:
        password_error = "password must be longer than 3 characters"
    if len(password) > 20:
        password_error = "password cannot be longer than 20 characters"
    if " " in password:
        password_error = "password may not contain spaces"
    
    email_from_form = str(request.form['email'])
    email_error = ''

    if "." not in email_from_form:
        email_error = "please enter valid email"
    if "@" not in email_from_form:
        email_error = "please enter valid email"
    if len(email_from_form) < 3:
        email_error = "email must be longer than 3 characters"
    if " " in email_from_form:
        email_error = "email may not contain spaces"
    
    if not email_error and not username_error and not password_error:
        return redirect('/successful_signin'.format(username))
    else:
        return render_template('forms.html', email_error = email_error, password_error = password_error, username_error = username_error, username = username_from_form, email = email_from_form)

@app.route('/successful_signin')
def success():
    return render_template('successful_signin.html')

app.run()