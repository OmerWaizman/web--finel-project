from flask import Blueprint, render_template
from flask import request,session

from flask import redirect,url_for

from utilities.interactdb.interact_db import interactDb

# Products blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')

# Routes
@catalog.route('/catalog',methods=['GET','POST'])
def index():
    products = interactDb.getProducts()
    return render_template('catalog.html',products=products)

@catalog.route('/getjackets', methods=['GET'])
def jackets():
    products = interactDb.getJackets()
    return render_template('catalog.html',products=products)

@catalog.route('/getpants', methods=['GET'])
def pants():
    products = interactDb.getPants()
    return render_template('catalog.html',products=products)

@catalog.route('/getjeans', methods=['GET'])
def jeans():
    products = interactDb.getJeans()
    return render_template('catalog.html',products=products)

@catalog.route('/getcaots', methods=['GET'])
def coats():
    products = interactDb.getCoats()
    return render_template('catalog.html',products=products)

@catalog.route('/getsocks', methods=['GET'])
def socks():
    products = interactDb.getSocks()
    return render_template('catalog.html',products=products)

@catalog.route('/getskirts', methods=['GET'])
def skirts():
    products = interactDb.getSkirts()
    return render_template('catalog.html',products=products)

@catalog.route('/gettshirts', methods=['GET'])
def tshirts():
    products = interactDb.getTshirts()
    return render_template('catalog.html',products=products)

@catalog.route('/getproduct',methods=['GET'])
def getproduct():
    if request.method=='GET':
        productid=(request.args.get('productid'))
        product = interactDb.getproductbyid(productid)
        return render_template('/product.html',product=product[0],productid=productid)
    return render_template('/catalog.html')