from flask import Blueprint, render_template,session,request
from utilities.interactdb.interact_db import interactDb
from utilities.interactdb.forms import forms
from datetime import datetime

# about blueprint definition
order = Blueprint('order', __name__, static_folder='static', static_url_path='/order', template_folder='templates')


# Routes
@order.route('/order',methods=['GET','POST'])
def index():
    if request.method=='POST':
        Email=session['email']
        items=interactDb.getcartitems(session['email'])
        for i in items:
            DT = datetime.now()
            ID=i[1]
            name=interactDb.getnamebyid(ID)
            price=interactDb.getpricebyid(ID)
            address=request.form['address']
            cc_num=request.form['cc_num']
            cc_month=request.form['cc_month']
            cc_year=request.form['cc_year']
            if forms.neworder(Email,ID,name[0],price,address,DT,cc_num,cc_month,cc_year)==1 and forms.updatequantity(ID)==1:
                print('Added')
        if forms.clearcart(Email)==1:
            message="Order Completed!"
            return render_template('order.html',message=message)
        return render_template('order.html')
    return render_template('order.html')



