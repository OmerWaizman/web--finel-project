from utilities.db.db_manager import dbManager
import mysql.connector
from flask import request

# New Class for interact with DB
class interactDB:
    def __init__(self):
        pass

    # Get - Gallery images src
    def getImges(self):
        query = "Select * From gallery"
        return dbManager.fetch(query)
    # Get - All recommends
    @staticmethod
    def getRecommends():
        query = "Select * From recommends"
        return dbManager.fetch(query)
    # Get - All products details
    def getProducts(self):
        products_query = "Select * From products"
        return dbManager.fetch(products_query)
    #Get - Prodcut Type
    def getJackets(self):
        jackets_query = "select * from products where type='Jacket'"
        return dbManager.fetch(jackets_query)
    def getTshirts(self):
        jackets_query = "select * from products where type='T-Shirt'"
        return dbManager.fetch(jackets_query)
    def getSocks(self):
        jackets_query = "select * from products where type='Socks'"
        return dbManager.fetch(jackets_query)
    def getCoats(self):
        jackets_query = "select * from products where type='Coat'"
        return dbManager.fetch(jackets_query)
    def getJeans(self):
        jackets_query = "select * from products where type='Jeans'"
        return dbManager.fetch(jackets_query)
    def getSkirts(self):
        jackets_query = "select * from products where type='Skirt'"
        return dbManager.fetch(jackets_query)
    def getPants(self):
        jackets_query = "select * from products where type='Pants'"
        return dbManager.fetch(jackets_query)
    def getSweaters(self):
        jackets_query = "select * from products where type='Sweater'"
        return dbManager.fetch(jackets_query)
    def getDresses(self):
        jackets_query = "select * from products where type='Dress'"
        return dbManager.fetch(jackets_query)
    def getproductbyid(self,productid):
        productquery=dbManager.fetch("select * from products where ID='%s'" % (productid))
        return (productquery)
    def gettypebyid(self,productid):
        result=dbManager.fetch("select type from products where ID='%s'" % (productid))
        type=[row[0] for row in result]
        return (type)
    def getnamebyid(self,productid):
        result=dbManager.fetch("select name from products where ID='%s'" % (productid))
        name=[row[0] for row in result]
        return (name)
    def getcolorbyid(self,productid):
        result=dbManager.fetch("select color from products where ID='%s'" % (productid))
        color=[row[0] for row in result]
        return (color)
    def getsizebyid(self,productid):
        result=dbManager.fetch("select size from products where ID='%s'" % (productid))
        size=[row[0] for row in result]
        return (size)
    def getpricebyid(self,productid):
        Total=0
        result=dbManager.fetch("select price from products where ID='%s'" % (productid))
        for row in result:
            Total+= row[0]
        return Total
    #Cart
    def getcartitems(self,seesion_email):
        email = dbManager.fetch(f"select * from charts where Email='{seesion_email}'")
        return email
    def sum_of_cart(self,Email):
        Total=0
        total = dbManager.fetch(f"select products.price from charts join products on charts.ID = products.ID where charts.Email='{Email}'")
        for row in total:
          Total+= row[0]
        return Total
    #Shopping History for user
    def orderhistory(self,Email):
        result=dbManager.fetch(f"select * from orders where Email='%s'" % (Email))
        return result
# Creates an instance for the interactDB class for export.
interactDb = interactDB()