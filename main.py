from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''

    if username == '':
        username_error = "Please enter a valid username."

    for character in username:
        if character == ' ':
            username_error = "Please enter a valid user name with no spaces."

    if password == '':
        password_error = "Please enter a valid password."
        password = ''

    for character in password:
        if character == ' ':
            password_error = "Please enter a valid password wth no spaces."

    if confirm == '':
        confirm_error = "Plese enter a valid password confirmation."
        confirm = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters."

    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters."
        password = ''

    if password != confirm:
        confirm_error = "Passwords do not match."
        confirm = ''

    if len(email) < 3 or len(email) > 20:
        email_error = "Please enter an email between 3 and 20 characets."
    
    for character in email:
        if character == '':
            email_error = "Please enter a valid email address."

    count = 0
    for character in email:
        if character == '@':
            count += 1
    
    if count > 1 or count == 0:
        email_error = "Please enter a valid email address"
    
    count = 0
    for character in email:
        if character == '.':
            count += 1

    if count > 1 or count == 0:
        email_error = "Pleaes enter a valid email address."

    if email == '':
        email_error = ''
 
    if not username_error and not password_error and not confirm_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('home.html', username_error=username_error, password_error=password_error, confirm_error = confirm_error, email_error = email_error, username=username, password='', confirm='', email=email)

app.run()