from flask import Blueprint, render_template,session
from utilities.interactdb.interact_db import interactDb
from utilities.interactdb.forms import forms
# about blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    items=interactDb.getcartitems(session['email'])
    Total=interactDb.sum_of_cart(session['email'])
    print(Total)

    return render_template('cart.html',items=items,Total=Total)

@cart.route('/ordernow')
def order():
    items=interactDb.getcartitems(session['email'])
    return render_template('/order.html',items=items)

