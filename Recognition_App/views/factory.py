from flask import ( Blueprint, render_template, request, redirect, session, url_for, flash )
from .MYSQL import *
from flask_login import ( login_user, current_user, logout_user, login_required )
from Recognition_App.models import User


FACTORY = Blueprint('factory', __name__, template_folder='templates', static_folder='static')

@FACTORY.route( '/factory/', methods = ['GET', 'POST'] )
def factory() :
	if request.method == 'GET' :
		res = dict()

		res['fixData'] = getFixRecordData()
		print( res )
		flash (res )

		return render_template( 'factoryIndex.html', res=res )

	elif request.method == 'POST':	
		form = request.form
		# print( form )
		
		if form :			
			try:

				return redirect( url_for('factory.factory') )

			except Exception as e:
				return str(e)
			
			finally:
				cursor.close()
				conn.close()

@FACTORY.route('/logout/')
@login_required
def logout() :
	print('logout')
	logout_user()
	session.pop( 'logged_in', None )
	session.pop( 'userid', None )
	session.pop( 'password', None )

	return redirect( url_for('login.login') )


