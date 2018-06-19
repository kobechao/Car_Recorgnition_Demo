from flask import ( Blueprint, render_template, request, redirect, session, url_for, flash )
from .MYSQL import *
from flask_login import ( login_user, current_user, logout_user, login_required )
from Recognition_App.models import User

from web3 import Web3, HTTPProvider, contract
from web3.contract import ConciseContract


web3 = Web3( HTTPProvider( 'http://localhost:8545' ) )
eth = web3.eth
assert web3.isConnected()
assert eth.accounts


AUCTION = Blueprint('auction', __name__, template_folder='templates', static_folder='static')

@AUCTION.route( '/auction/', methods = ['GET', 'POST'] )
def auction() :
	if request.method == 'GET' :
		res = dict()

		res['auctionData'] = getAuctionData()

		print( res )

		return render_template( 'auctionIndex.html', res=res)

	elif request.method == 'POST':	
		form = request.form
		# print( form )
		
		if form :			
			try:

				return redirect( url_for('auction.auction') )

			except Exception as e:
				return str(e)
			
			finally:
				cursor.close()
				conn.close()

@AUCTION.route('/logout/')
@login_required
def logout() :
	print('logout')
	logout_user()
	session.pop( 'logged_in', None )
	session.pop( 'userid', None )
	session.pop( 'password', None )

	return redirect( url_for('login.login') )


