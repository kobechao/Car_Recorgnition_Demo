 # -*- coding: UTF-8 -*-

from web3 import Web3, HTTPProvider, contract
from solc import compile_source, compile_files, link_code
import os

web3 = Web3( HTTPProvider( 'http://localhost:8545' ) )
eth = web3.eth
assert web3.isConnected()
assert eth.accounts


class MaintananceContract():

	"""MaintananceContract class in python"""

	def __init__( self ):
		
		self.__deployed = False



	def getContract( self, args ) :
		print( args )
		self.__adminAddr = eth.accounts[0]
		self.contractBytecode, self.contractABI = self.__get_Bytecode_ABI()
		self.contract_Car_Recorgnition = eth.contract( abi = self.contractABI, bytecode = self.contractBytecode )

		self.contractHash = self.contract_Car_Recorgnition \
			.constructor ( args['carAddr'], args['fixFactoryID'], args['fixDate'], int(args['mileage']), args['fixType'], args['fixList'] ) \
			.transact( transaction = { "from": self.__adminAddr } )

		self.receipt = eth.waitForTransactionReceipt( self.contractHash )
		self.address = self.receipt.get('contractAddress', None)

		print( '\nContract Deployed at\n%s\n%s\n' % ( self.address, '=' * len( self.address ) ) )

		self.__deployed = True
		


	def __get_Bytecode_ABI( self ) :

		contractPath = ['contract/MaintananceContract.sol']
		print(__name__)
		if __name__ == 'Recognition_App.MaintananceContract':
			contractPath = ['Recognition_App/contract/MaintananceContract.sol']
		
		compiledValues = list(compile_files( contractPath ).values())[0]

		return compiledValues['bin'] ,compiledValues['abi']



	def setFixRecord( self, addr ) :

		if self.__deployed :
			_tx = self.contract_Car_Recorgnition.functions.setFixRecord( addr ).transact( { 'from': self.__adminAddr, 'to': self.receipt['contractAddress'] } )
			eth.waitForTransactionReceipt( _tx )
			return _tx

		else:
			return None



	def getMaintananceInfo( self ) :

		if self.__deployed :
			_tx = self.contract_Car_Recorgnition.functions.getAddr().call( {  'to': self.receipt['contractAddress'] } )
			return _tx

		else :
			return None


	def getMaintananceAddr( self ) :

		if self.__deployed :
			_tx = self.contract_Car_Recorgnition.functions.getAddr().call( {  'to': self.receipt['contractAddress'] } )
			return _tx

		else :
			return None


	
	def getTx( self, tx ) :
		_tx = eth.getTransaction( tx )
		return _tx



def test( MaintananceContract ):
	MaintananceContract.deployContract( 
		dict({
			'carAddr': '0x692a70D2e424a56D2C6C27aA97D1a86395877b3A', 
			'fixFactoryID': 'ABC', 
			'fixDate': '2018/06/31', 
			'mileage': 1000,
			'fixType': 'glasses',
			'fixList': 'front, back, fuck',
		}) 
	)

	print( MaintananceContract.getMaintananceInfo() )
	pass

if __name__ == '__main__':

	# test()
	MaintananceContract = MaintananceContract()
	

	test( MaintananceContract )

	





