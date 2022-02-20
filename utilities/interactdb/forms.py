from utilities.db.db_manager import dbManager

# New Forms Class for interact with DB
class Forms:
    def _init_(self):
        pass

    ####FETCH QUERIES####
    # Login Page - Check User in DB
    def checkUser (self, email, password):
        return dbManager.fetch(f"Select * From users WHERE Email='{email}' AND password='{password}'")

    def getUserNameByEmail(self, Email):
        result = dbManager.fetch(f"Select fullname From users WHERE email= '{Email}'")
        username = [row[0] for row in result]
        return username[0]
        # Check Password in DB for specific user

    def getFullNameinSession(self,seesion_email):
        result = dbManager.fetch(f"select fullname from users where Email='{seesion_email}'")
        fullname = [row[0] for row in result]
        return fullname[0]
    def getEmailinSession(self,seesion_email):
        result = dbManager.fetch(f"select Email from users where Email='{seesion_email}'")
        email = [row[0] for row in result]
        return email[0]
    def getPhoneinSession(self,seesion_email):
        result = dbManager.fetch(f"select Phone from users where Email = '{seesion_email}'")
        phone = [row[0] for row in result]
        return phone[0]


    ####UPDATE QUERIES##
    def changename(self, email, newname):
        query = "UPDATE users SET fullname = '%s' WHERE Email='%s'" % (newname, email)
        dbManager.commit(query)
        return True

    def changephone(self, email, newphone):
        query = "UPDATE users SET phone = '%s' WHERE Email='%s'" % (newphone, email)
        dbManager.commit(query)
        return True

    # Set -Cahnge the user details
    def changePassword(self, email, newpassword):
        query = "UPDATE users SET password = '%s' WHERE Email='%s'" % (newpassword, email)
        dbManager.commit(query)
        return True

    #Update the product Quantity after oredered
    def updatequantity(self, ID):
        query = "UPDATE products SET quantity=(quantity-1)  WHERE ID='%s'" % (ID)
        dbManager.commit(query)
        return True


    # Set - Update new password for user
    def editpage(self, username, phone, newpassword, address, city, email):
        query = "UPDATE users SET username = '%s' ,phone = '%s' ,newpassword = '%s' ,address = '%s' ,city= '%s'  WHERE Email='%s'" % (username, phone, newpassword, address, city, email)
        dbManager.commit(query)
        return True


    ###INSERT QUERIES###

    # Login Page - Set - Registration New User
    def create_user(self, Email, fullname, phone ,password):
        query = "INSERT INTO users (fullname,password,Email,phone) VALUES ('%s','%s','%s','%s')" \
                % (fullname,password,Email,phone)
        dbManager.commit(query)
        return True

    #Add new order into Orders
    def neworder(self, Email,ID,name,price,address,DT,cc_num,cc_month,cc_year):
        query = "INSERT INTO orders (Email,ID,name,price,Address,DT,cc_num,cc_month,cc_year) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s' )" \
                % (Email,ID,name,price,address,DT,cc_num,cc_month,cc_year)
        dbManager.commit(query)
        return True

        # Add Item To Cart
    def add_to_cart(self, Email, ID ,type,name,color,size,price):
        query = "INSERT INTO charts (Email,ID,type,name,color,size,price) VALUES ('%s','%s','%s','%s','%s','%s','%s')" \
                % (Email,ID,type,name,color,size,price)
        dbManager.commit(query)
        return True

    ####DELETE QUERIES####
    # Delete user from DB
    def deleteUser(self, email):
        query = "DELETE FROM users WHERE Email='%s'" % email
        dbManager.commit(query)
        return True

    #clear Cart after order
    def clearcart(self, email):
        query = "DELETE FROM charts WHERE Email='%s'" % email
        dbManager.commit(query)
        return True


# Creates an instance for the forms class for export.
forms = Forms()