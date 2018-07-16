from flask import ( Blueprint, render_template, request, redirect, session, url_for, flash )
from flask_login import ( LoginManager, login_user, current_user, logout_user, login_required )

from Recognition_App.models import User, db
from Recognition_App.forms import LoginForm

# from .MYSQL import connect_to_db


LOGIN = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@LOGIN.route( '/login/', methods = ['GET', 'POST'] )
@LOGIN.route( '/signin/', methods = ['GET', 'POST'] )
def login() :

	loginForm = LoginForm()
	print( request.form )
	if request.method == 'GET' :
		return render_template( 'login.html', form=loginForm )

	elif request.method == 'POST':	
		
		if loginForm.validate_on_submit() :			
			IDNumber = request.form.get( 'IDNumber', None )
			password = request.form.get( 'password', None )
			
			user = User( IDNumber )
			if user.verify_password( password ):
				session['logged_in'] = True
				print( session )
				login_user( user )

			# except Exception as e:
			# 	return str(e)

			return redirect( url_for('index.index') )
		else :
			return redirect( url_for('login.login') )


		# if form.validate_on_submit() :			
		# 	IDNumber = request.form.get( 'personalID', None )
		# 	password = request.form.get( 'password', None )
		# 	assert IDNumber is not None and password is not None
			
		# 	cursor = db.cursor()

		# 	try:
		# 		sql = 'SELECT IDNumber, name, birthday, licenseNumber, password FROM car_personal_table where IDNumber=\'%s\';' 
		# 		# print( sql )
		# 		cursor.execute( sql % IDNumber )
		# 		userLoginData = cursor.fetchone()

		# 		if userLoginData is None:
		# 			print( 'No Such User' )
		# 			flash( '無此使用者' )
		# 			return redirect( url_for('login.login') )

		# 		print( userLoginData )

		# 		if IDNumber == userLoginData[0] and password == userLoginData[4] :
		# 			user = User()
		# 			user.id = IDNumber
		# 			login_user( user )
		# 			session['userName']= userLoginData[0]
		# 			session['logged_in'] = True
		# 			session['password'] = password
		# 			session['birthday'] = userLoginData[2].strftime("%Y-%m-%d")
		# 			session['loginPerson'] = 'User'

		# 			print( session )


		# 			return redirect( url_for('index.index') )

		# 		else :
					
		# 			print( 'Wrong Password' )
		# 			flash( '密碼錯誤' )
		# 			return redirect( url_for('login.login') )


		# 	except Exception as e:
		# 		return str(e)
			
		# 	finally:
		# 		cursor.close()


@LOGIN.route('/logout/')
@login_required
def logout() :
	print('logout')
	logout_user()
	session.pop( 'logged_in', None )
	session.pop( 'userid', None )
	session.pop( 'password', None )

	return redirect( url_for('login.login') )


