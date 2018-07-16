from flask import ( Blueprint, render_template, request, redirect, session, g, url_for, flash )
from .MYSQL import *
from flask_login import ( login_user, current_user, logout_user, login_required )
from Recognition_App.models import User
from Recognition_App.MaintananceContract import MaintananceContract

from web3 import Web3, HTTPProvider, contract
from web3.contract import ConciseContract
web3 = Web3( HTTPProvider( 'http://localhost:8545' ) )
eth = web3.eth
assert web3.isConnected()
assert eth.accounts


FACTORY = Blueprint('factory', __name__, template_folder='templates', static_folder='static', url_prefix='/factory')
MaintananceContract = MaintananceContract()

@FACTORY.route( '/', methods = ['GET', 'POST'] )
@login_required
def factory() :
	if request.method == 'GET' :
		res = dict()
		res['fixData'] = getFixRecordData()
		
		return render_template( 'factoryIndex.html', res=res )

	elif request.method == 'POST':	

		form = request.form
		# print( form )
		if form :
			try :
				fixList = list()
				arg = dict()

				for key in form.keys():
					if 'maintanceItem' in key:
						fixList.append( form[key] )

				arg['fixList'] = ','.join(fixList)
				arg['fixDate'] = form['fixDate']
				arg['mileage'] = form['mileage']
				arg['fixType'] = form['fixType']
				arg['fixFactoryID'] = 'CINDY'
				arg['carAddr'] = form['carAddr']

				MaintananceContract.getContract( arg )
				maintainAddr = MaintananceContract.getMaintananceAddr()
				
				if( maintainAddr ):

					print( 'MaintananceContract.getMaintananceInfo' )
					print( '======================================' )
					print( MaintananceContract.getMaintananceInfo() )
					personalCarcontract = eth.contract( address=arg['carAddr'], abi=getCarABI() )
					
					tx = personalCarcontract.functions.setFixRecord( maintainAddr ).transact( {'from': eth.accounts[0], 'to': arg['carAddr']} )
					eth.waitForTransactionReceipt( tx )

					print( 'setFixRecord: tx hash' )
					print( '=====================' )
					print( tx.hex() )

					print( 'personalCarcontract.getCarInfos')
					print( '===============================')
					print( personalCarcontract.functions.getCarInfos().call( {'to': arg['carAddr']}) )
				
					return redirect( url_for('factory.factory') )

			except Exception as e:
				print( str(e) )
				return redirect( url_for('factory.factory') )
			
			




