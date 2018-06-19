from flask import Blueprint, render_template, request, redirect,flash, url_for
from .MYSQL import connect_to_db
# from Recognition_App.contract import ID_Recognition_Contract, getContractDBData


REGISTER = Blueprint('register', __name__, template_folder='templates', static_folder='static')

# ID_Recognition_Contract = ID_Recognition_Contract()


@REGISTER.route('/register/', methods=['GET', 'POST']) 
def register() :

	error = None

	if request.method == 'GET':
		return render_template( 'register.html' )

	elif request.method == 'POST':
		form = request.form
		print( 'post:', form)

		if ID_Recognition_Contract.getUserRegisterTable( userID=form['registerID'] ) :
			flash( '此ID已註冊過' )
			return redirect( url_for('register.register') )

		else :
			# registerTx = ID_Recognition_Contract.setUserRegisterTable( userID=form['personalID'] ).hex()
			# assert ID_Recognition_Contract.getUserRegisterTable( userID=form['personalID'] ) == True
			# assert registerTx != None

			conn = connect_to_db()
			cursor = conn.cursor()


			try :
				if( form.get( 'userRegister', None ) ) :
					sql = 'INSERT INTO car_personal_table ( IDNumber, name, birthday, licenseNumber, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\", \"%s\" );'
					cursor.execute( sql % ( form['registerID'], form['name'], form['birthday'], form['license'], form['password'] ))

				elif( form.get( 'fixRegister', None ) ) :
					sql = 'INSERT INTO repairer_personal_table ( repairerID, repairerName, agent, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\");'
					cursor.execute( sql % ( form['registerID'], form['repairerName'], form['agent'], form['password'] ))

				elif( form.get( 'auctionRegister', None ) ) :
					sql = 'INSERT INTO auction_personal_table ( auctioneerID, auctioneerName, agent, password ) values ( \"%s\", \"%s\", \"%s\", \"%s\" );'
					cursor.execute( sql % ( form['registerID'], form['auctioneerName'], form['agent'], form['password'] ))

				
				# sql = 'INSERT INTO contract_data ( personalID, contractAddress, contractABI, userToken ) values ( \"%s\", \"%s\", \"%s\", \"%s\" );'
				# cursor.execute( sql % ( form['personalID'], ID_Recognition_Contract.address, ID_Recognition_Contract.contractABI, registerTx ))

				conn.commit()
				flash( '註冊成功' )

			except Exception as e :
				flash( str(e) )
				print( type(e), e )
				return redirect( url_for('register.register') )


			finally:
				cursor.close()
				conn.close()

			return redirect( url_for('login.login') )

	else :
		pass


