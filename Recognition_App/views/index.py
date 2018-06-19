from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify, abort
from Recognition_App.CarContract import Car_Recorgnition_Contract
# from Recognition_App.ApiExecuter import ApiExecuter
from flask_login import ( current_user, login_required, logout_user )
import requests, json

from .MYSQL import *


INDEX = Blueprint('index', __name__, template_folder='templates', static_folder='static', url_prefix='/index')
Car_Recorgnition_Contract = Car_Recorgnition_Contract()

@INDEX.route('/', methods=['GET', 'POST'])
def index() :

	if request.method == 'POST' :
		form = request.form
		print( form )
		print("=====")
		print( form.to_dict() ) 

		
		Car_Recorgnition_Contract.getContract( form.to_dict() )
		if setCarRecordData( Car_Recorgnition_Contract.getCarAddress(), session['userid'] ):
			return redirect( url_for('index.index'))
			
		else :
			flash( 'error' )
			return redirect( url_for('index.index'))

	else :
		if current_user.is_active :

			res = dict()
			res['carRecord'] = getCarRecordData( current_user.id, currentPerson=session['loginPerson'] ) 
			
			session['carAddrs'] = list()
			for data in res['carRecord'] :
				session['carAddrs'].append( data['carContractAddr'])
			flash( 'Login as ' + session['userName'] )
			
			session['userid'] = current_user.id
			print( session )



			return render_template('index.html', res=res )
		
		else :
			return redirect( url_for('login.login') )




@INDEX.route('/<url_institution>', methods=['GET', 'POST'] )
def institutionRegistration( url_institution ) :
	institution = url_institution.upper()

	if current_user.is_active and session['logged_in']:
		if request.method == 'POST':
			form = dict(request.form)

			if form.get( 'password', None )[0] == str(session['password']) :
				res = ApiExecuter( URLS_CONF[ institution ] + '/insertUserData', getContractDBData( current_user.id ), form ).getDBRespondData()
				flash( res[institution] )

			else :
				flash( 'Wrong Password!')

			return redirect( url_for('index.institutionRegistration', url_institution=url_institution) )


		else :
			# res = ApiExecuter( URLS_CONF[ institution ] + '/insertUserData', getContractDBData( current_user.id ), {'userName': 'kobe', 'birthday':'1996/09/23'} ).getDBRespondData()
			
			return render_template( '%s.html' % url_institution )

	else :
		return 'NOT LOGIN'


@INDEX.route('/profile', methods=['GET'])
def profile() :
	return render_template('profile.html')




@INDEX.route('/listCarInfo', methods=['POST'])
def listCarInfo() :
	form = dict( request.form )
	res = dict()
	print( form )

	if( form.get( 'IDNumber', None ) and form.get('carAddr', None) ) :
		if( form['carAddr'] in session['carAddrs'] ) :
			print( Car_Recorgnition_Contract.getCarInfos() )
		
			return render_template('carInfo.html', res=res )

		else :
			abort( 400, 'Wrong Token!' )

	else :
		abort( 400, 'No Token!' )



@INDEX.errorhandler(400) 
def errorHandler_400( err ) :
	response = jsonify( { 'message': err.description } )
	return response





