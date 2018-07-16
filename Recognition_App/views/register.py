from flask import Blueprint, render_template, request, redirect,flash, url_for
from werkzeug.security import generate_password_hash

from Recognition_App.models import db
from Recognition_App.forms import LoginForm


REGISTER = Blueprint('register', __name__, template_folder='templates', static_folder='static')


@REGISTER.route('/register/', methods=['GET', 'POST']) 
def register() :

	error = None

	if request.method == 'GET':
		return render_template( 'register.html' )

	elif request.method == 'POST':
		form = request.form
		print( 'post:', form)

		if False:
			pass
			
		else :
			
			cursor = db.cursor()

			try :
				if( form.get( 'userRegister', None ) ) :
					sql = 'INSERT INTO car_personal_table ( IDNumber, name, birthday, licenseNumber, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\", \"%s\" );'
					cursor.execute( sql % ( form['registerID'], form['name'], form['birthday'], form['license'], generate_password_hash( form['password'] ) ))

				elif( form.get( 'fixRegister', None ) ) :
					sql = 'INSERT INTO repairer_personal_table ( repairerID, repairerName, agent, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\");'
					cursor.execute( sql % ( form['registerID'], form['repairerName'], form['agent'], generate_password_hash( form['password'] ) ))

				elif( form.get( 'auctionRegister', None ) ) :
					sql = 'INSERT INTO auction_personal_table ( auctioneerID, auctioneerName, agent, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\" );'
					cursor.execute( sql % ( form['registerID'], form['auctioneerName'], form['agent'], generate_password_hash( form['password'] ) ))
				

				db.commit()
				flash( '註冊成功' )

			except Exception as e :
				flash( str(e) )
				print( type(e), e )
				return redirect( url_for('register.register') )


			finally:
				cursor.close()

			return redirect( url_for('login.login') )

	else :
		pass


