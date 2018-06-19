import pymysql

def connect_to_db() :
	conn = pymysql.connect( host='127.0.0.1', user='root', passwd='root', db='DBO_CAR_RECORGNITION')

	return conn

def getCarRecordData( registerID, currentPerson=None ):

	conn = connect_to_db()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	try :
		if currentPerson :
			sql = ''

			if currentPerson == 'User':
				sql = "SELECT * FROM car_record_table WHERE IDNumber=\'%s\';" % ( registerID )
				pass
			elif currentPerson == 'Repairer':
				sql = "SELECT * FROM car_record_table WHERE IDNumber=\'%s\';" % ( registerID )
				pass
			elif currentPerson == 'Auctioneer':
				sql = "SELECT * FROM car_record_table WHERE IDNumber=\'%s\';" % ( registerID )
				pass


			cursor.execute( sql )
			carData = cursor.fetchall()

			# print( carData )
			return carData

	except Exception as e :
		print( e )
		return None

	finally:
		conn.close()
		cursor.close()

def setCarRecordData( addr, IDNumber ) :
	print( addr )

	if addr:
		conn = connect_to_db()
		cursor = conn.cursor()

		try:
			sql = 'INSERT INTO car_record_table( IDNumber, carContractAddr, status ) values( \'%s\', \'%s\', %s );'
			cursor.execute( sql % ( IDNumber, addr, '1' ) )
		except Exception as e:
			print( e )
			cursor.close()
			conn.close()
			return False
		
		conn.commit()
		cursor.close()
		conn.close()

		return True
		
	else :
		return False


def setFixRecordData( repairerID, addr) :

	if addr:
		conn = connect_to_db()
		cursor = conn.cursor()

		try:
			sql = 'INSERT INTO fix_Apply( repairerID, carContractAddr) values( \'%s\', \'%s\' );'
			cursor.execute( sql % ( repairerID, addr ) )
		except Exception as e:
			print( e )
			cursor.close()
			conn.close()
			return False
		
		conn.commit()
		cursor.close()
		conn.close()

		return True
		
	else :
		return False


def getFixRecordData() :

	conn = connect_to_db()
	cursor = conn.cursor( pymysql.cursors.DictCursor )

	try:
		sql = 'SELECT fix_Apply.fixApplyNo ,car_personal_table.name, fix_Apply.carContractAddr  FROM fix_Apply join car_record_table on fix_Apply.carContractAddr = car_record_table.carContractAddr join car_personal_table on car_record_table.IDNumber = car_personal_table.IDNumber; '
		cursor.execute( sql )
		fixData = cursor.fetchall()
		print( fixData )
		return fixData

	except Exception as e:
		print( e )
		cursor.close()
		conn.close()
		return False
		

	cursor.close()
	conn.close()

	
def getRepairerPersonalData():

	conn = connect_to_db()
	cursor = conn.cursor( pymysql.cursors.DictCursor )

	try:
		sql = 'SELECT repairerID, repairerName FROM repairer_personal_table;'
		cursor.execute( sql )
		repairerData = cursor.fetchall()
		print( repairerData )
		return repairerData

	except Exception as e:
		print( e )
		cursor.close()
		conn.close()
		return False
		

	cursor.close()
	conn.close()

def getAuctionPersonalData():
	conn = connect_to_db()
	cursor = conn.cursor( pymysql.cursors.DictCursor )

	try:
		sql = 'SELECT * FROM auction_personal_table;'
		cursor.execute( sql )
		auctionData = cursor.fetchall()
		print( auctionData )
		return auctionData

	except Exception as e:
		print( e )
		cursor.close()
		conn.close()
		return False
		

	cursor.close()
	conn.close()

def setAuctionData( auctoneerID, addr) :

	if addr:
		conn = connect_to_db()
		cursor = conn.cursor()

		try:
			sql = 'INSERT INTO auction_apply( auctioneerID, carContractAddr) values( \'%s\', \'%s\' );'
			cursor.execute( sql % ( auctoneerID, addr ) )
		except Exception as e:
			print( e )
			cursor.close()
			conn.close()
			return False
		
		conn.commit()
		cursor.close()
		conn.close()

		return True
		
	else :
		return False

def getAuctionData():

	conn = connect_to_db()
	cursor = conn.cursor( pymysql.cursors.DictCursor )

	try:
		sql = 'SELECT car_personal_table.name ,auction_personal_table.auctioneerName,auction_apply.carContractAddr FROM auction_personal_table join auction_apply on auction_personal_table.auctioneerID = auction_apply.auctioneerID join car_record_table on auction_apply.carContractAddr = car_record_table.carContractAddr join car_personal_table on car_record_table.IDNumber = car_personal_table.IDNumber ;'
		cursor.execute( sql )
		auctionData = cursor.fetchall()
		print( auctionData )
		return auctionData

	except Exception as e:
		print( e )
		cursor.close()
		conn.close()
		return False
		

	cursor.close()
	conn.close()

