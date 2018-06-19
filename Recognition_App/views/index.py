from flask import Blueprint, render_template, request, session, g, redirect, url_for, flash, jsonify, abort
from Recognition_App.CarContract import Car_Recorgnition_Contract, getCarContract
from flask_login import ( current_user, login_required, logout_user )
import requests, json


from .MYSQL import *


from web3 import Web3, HTTPProvider, contract
from web3.contract import ConciseContract


web3 = Web3( HTTPProvider( 'http://localhost:8545' ) )
eth = web3.eth
assert web3.isConnected()
assert eth.accounts


INDEX = Blueprint('index', __name__, template_folder='templates', static_folder='static', url_prefix='/index')
Car_Recorgnition_Contract = Car_Recorgnition_Contract()



@INDEX.route('/', methods=['GET', 'POST'])
def index() :

	if request.method == 'POST' :
		form = request.form
		
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

			return render_template('index.html', res=res )
		
		else :
			return redirect( url_for('login.login') )





@INDEX.route('/applyMaintance', methods=['GET', 'POST'] )
def applyMaintance( ) :
	if request.method == 'POST' :
		form = request.form
		print( form )
		setFixRecordData( form.get('repairer', None), form.get('carAddr', None) )
		
		return redirect( url_for('index.applyMaintance' ) )
	res = getRepairerPersonalData()
	flash(res)
	return render_template( 'applyMaintance.html', res=res )


@INDEX.route('/applyAuction', methods=['GET', 'POST'] )
def applyAuction( ) :
	if request.method == 'POST' :
		form = request.form
		print( form )
		setAuctionData( form.get('auctioneer', None), form.get('carAddr', None) )
		
		return redirect( url_for('index.applyAuction' ) )
	res = getAuctionPersonalData()
	flash(res)
		
	return render_template( 'applyAuction.html', res=res )

	


@INDEX.route('/profile', methods=['GET'])
def profile() :
	return render_template('profile.html')




@INDEX.route('/listCarInfo', methods=['POST'])
def listCarInfo() :
	form = request.form 
	res = dict()
	print( form )

	if( form.get( 'IDNumber', None ) and form.get('carAddr', None) ) :
		if( form['carAddr'] in session['carAddrs'] ) :
			res = dict()

			with open( 'contract.json', 'r' ) as jsonfile :
				arg = json.load( jsonfile )
				personalCarContract = eth.contract( address=form['carAddr'], abi=arg['ABI'], ContractFactoryClass=ConciseContract )
				carList = personalCarContract.getCarInfos()

				res['licencePlateNumber'] = carList[0]
				res['engineSerialNumber'] = carList[1]
				res['factory'] = carList[2]
				res['carYears'] = carList[3]
				res['carStyle'] = carList[4]
				res['carColor'] = carList[5]
				res['carLoading'] = carList[6]
				res['fixRecords'] = carList[7]

				jsonfile.close()

			return render_template('carInfo.html', res=res )

		else :
			abort( 400, 'Wrong Token!' )

	else :
		abort( 400, 'No Token!' )



@INDEX.errorhandler(400) 
def errorHandler_400( err ) :
	response = jsonify( { 'message': err.description } )
	return response







