from flask import Blueprint, render_template, request, redirect, session, url_for
from utilities.interactdb.forms import forms

# from utilities.interactdb.interact_db import interactDb
# from utilities.interactdb.Emails import emails

# login blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')
login.secret_key = "123436"

# Routes
@login.route('/login', methods=['GET','POST'])
def index():
    session['login'] = False
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['pass']
        if not forms.checkUser(email,passwd):
            massage = 'One of the details is wrong!'
            return render_template('login.html', massage=massage)
        userName = forms.getUserNameByEmail(email)
        print(userName)
        session['login'] = True
        session['name'] = userName
        session['email'] = email
        print(email)
        phone=forms.getPhoneinSession(email)
        session['phone']=phone
        print(phone)
        return redirect('/homepage')
    return render_template('login.html')

@login.route('/newuser', methods=['GET','POST'])
def newuser():
    if request.method == 'POST':
        fullname = request.form['fullname']
        passwd = request.form['pass']
        passwd1 = request.form['pass1']
        email = request.form['email']
        phone = request.form['phone']
        if forms.create_user(email, fullname,phone,passwd) == 1:
            massage = 'Registration succsessful!'
            session['login'] = True
            userName = forms.getUserNameByEmail(email)
            session['name'] = userName
            session['email'] = email
            session['email'] = email
            session['phone']=phone
            return render_template('/homepage.html', massage=massage)
        success=False
    return render_template('/login.html', success=success)