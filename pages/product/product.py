from flask import Blueprint, render_template,request,session,redirect,url_for

# about blueprint definition
import utilities.interactdb.forms
from utilities.interactdb.interact_db import interactDb
from utilities.interactdb.forms import forms


product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')

# Routes
@product.route('/product', methods=['GET','POST'])
def index():
    return render_template('product.html')


@product.route('/addtocart', methods=['GET','POST'])
def addtocart():
    if session['login']==True:
        Email=session['email']
        ID=request.form['cart']
        type = interactDb.gettypebyid(ID)
        type1=str(type[0])
        name= interactDb.getnamebyid(ID)
        name1=str(name[0])
        color = interactDb.getcolorbyid(ID)
        color1=str(color[0])
        size=interactDb.getsizebyid(ID)
        size1=str(size[0])
        price=interactDb.getpricebyid(ID)
        if forms.add_to_cart(Email,ID,str(type1),str(name1),str(color1),str(size1),price)==1:
            message="Item Added To Cart"
            products = interactDb.getProducts()
        return render_template('/catalog.html',message=message,products=products)
        return render_template('/product.html')
    return render_template('/product.html')



