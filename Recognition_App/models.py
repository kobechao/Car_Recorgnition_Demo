
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 
import json
import uuid
import pymysql

from Recognition_App import db


class User( UserMixin ):

	'''
	User Model!
	'''

	def __init__( self, IDNumber ):
		self.IDNumber = IDNumber
		self.id = self.get_id()


	@property
	def password( self ):
		return AttributeError("Not Readable Password!")
 	

	@password.setter
	def password( self, password ):
		self.password_hash = generate_password_hash( password )


	def verify_password( self, password ):
		return check_password_hash( self.get_password(), password )


	def get_password( self ):
		cursor = conn.cursor( pymysql.cursors.DictCursor )

		try:
			sql = 'SELECT password FROM car_personal_table WHERE IDNumber = \'%s\';' % ( self.IDNumber )
			print( sql )
			cursor.execute( sql )
			password = cursor.fetchone()

			return password

		except Exception as e:
			print( e )
			cursor.close()
			return None

		return None


	def get_id( self ):
		if self.IDNumber is not None:
			return True

		return unicode( uuid.uuid4() )


	@staticmethod
	def get( user_id ):
		if not user_id:
			return None

		return True
