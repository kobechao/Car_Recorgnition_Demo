import pymysql

def connect_to_db() :
	conn = pymysql.connect( host='127.0.0.1', user='root', passwd='tina1633', db='DBO_CAR_RECORGNITION')
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

			print( carData )
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





