from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

#login
from pages.login.login import login
app.register_blueprint(login)
#logout
from pages.logout.logout import logout
app.register_blueprint(logout)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

#Header
from components.Header.header import header
app.register_blueprint(header)

#footer
from components.footer.footer import footer
app.register_blueprint(footer)

#edit
from pages.edit.edit import edit
app.register_blueprint(edit)

#product
from pages.product.product import product
app.register_blueprint(product)

#cart
from pages.cart.cart import cart
app.register_blueprint(cart)

#order
from pages.order.order import order
app.register_blueprint(order)

#contact
from pages.contact.contact import contact
app.register_blueprint(contact)