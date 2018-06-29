from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm( FlaskForm ) :

	IDNumber = StringField( 'IDNumber', validators=[ DataRequired() ] )
	password = PasswordField( 'password', validators=[ DataRequired() ] )
