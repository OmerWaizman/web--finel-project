from flask import Blueprint, render_template, redirect, url_for,session,request
from utilities.interactdb.forms import forms
from utilities.interactdb.interact_db import interactDb
# aboutu blueprint definition
edit = Blueprint('edit', __name__, static_folder='static', static_url_path='/edit', template_folder='templates')


@edit.route('/edit',methods=['GET','POST'])
def index():
    if session['login']:
        phone=forms.getPhoneinSession(session['email'])
        email=forms.getEmailinSession(session['email'])
        orders=interactDb.orderhistory(session['email'])
        fullname=forms.getUserNameByEmail(session['email'])
        return render_template('edit.html',phone=phone,email=email,fullname=fullname,orders=orders)
    return render_template('homepage.html')

@edit.route('/selfdelete',methods=['POST','GET'])
def selfdelete():
    email=forms.getEmailinSession(session['email'])
    forms.deleteUser(email)
    session.login=False
    return render_template('homepage.html')

@edit.route('/changedetails', methods=['POST','GET'])
def changedetails():
    email=forms.getEmailinSession(session['email'])
    newfullname = request.form['fullname']
    newphone = request.form['phone']
    newpassword = request.form['password']
    session['name']=newfullname
    session['phone']=newphone
    session['password']=newpassword
    forms.changename(email,newfullname)
    forms.changePassword(email,newpassword)
    forms.changephone(email,newphone)
    return render_template('homepage.html')




