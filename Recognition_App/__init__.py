from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

from .views.login import LOGIN
from .views.register import REGISTER
from .views.index import INDEX
from .views.factory import FACTORY
from .views.auction import AUCTION

from Recognition_App.models import User

import pymysql

app = Flask(__name__, instance_relative_config=True)

app.secret_key = os.urandom(24)

app.register_blueprint( LOGIN )
app.register_blueprint( REGISTER )
app.register_blueprint( INDEX, url_prefix='/index' )
app.register_blueprint( FACTORY )
app.register_blueprint( AUCTION )

db = pymysql.connect( host='127.0.0.1', user='root', passwd='root', db='DBO_CAR_RECORGNITION')

login_manager = LoginManager()
login_manager.session.protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app( app=app )

@login_manager.user_loader
def user_loader( user_id ):
	return User.get( user_id )


csrf = CsrfProtect()
csrf.init_app( app )


from Recognition_App import views