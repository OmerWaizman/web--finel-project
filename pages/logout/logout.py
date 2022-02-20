from flask import Blueprint, render_template, request, redirect, session, url_for
from utilities.interactdb.forms import forms
logout = Blueprint('logout', __name__, static_folder='static', static_url_path='/logout', template_folder='templates')


@logout.route('/logout')
def index():
    session['login']=False
    return render_template('homepage.html')