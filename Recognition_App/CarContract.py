 # -*- coding: UTF-8 -*-

from web3 import Web3, HTTPProvider, contract
from web3.contract import ConciseContract
from solc import compile_source, compile_files, link_code
import os

web3 = Web3( HTTPProvider( 'http://localhost:8545' ) )
eth = web3.eth
assert web3.isConnected()
assert eth.accounts
import json


class Car_Recorgnition_Contract():

	"""Car_Recorgnition_Contract class in python"""

	def __init__( self ):
		print( '\nInit Car_Recorgnition_Contract\n')
		self.deployed = False



	def getContract( self, args ) :


		self.__adminAddr = eth.accounts[0]
		self.contractBytecode, self.contractABI = self.__get_Bytecode_ABI()

		self.contract_Car_Recorgnition = eth.contract( abi = self.contractABI, bytecode = self.contractBytecode )

		self.contractHash = self.contract_Car_Recorgnition \
			.constructor ( args['licencePlateNumber'], args['engineSerialNumber'], args['factory'], int(args['carYears']), args['carStyle'], args['carColor'], int(args['carLoading'])) \
			.transact( transaction = { "from": self.__adminAddr } )

		self.receipt = eth.waitForTransactionReceipt( self.contractHash )
		self.address = self.receipt.get('contractAddress', None)

		print( '\nContract deployed at\n%s\n%s\n' % ( self.address, '=' * len( self.address ) ) )

		self.deployed = True

		with open( 'contract.json', 'w' ) as jsonfile :
			json.dump( dict({
				'ABI': self.contractABI,
				'NEWEST_ADDRESS': self.address
				}), jsonfile, sort_keys=True, indent=4, ensure_ascii=False)

			jsonfile.close()


		


	def __get_Bytecode_ABI( self ) :

		contractPath = ['contract/CarContract.sol']
		print( __name__ )
		if __name__ == 'Recognition_App.CarContract':
			contractPath = ['Recognition_App/contract/CarContract.sol']
		
		compiledValues = list(compile_files( contractPath ).values())[0]

		return compiledValues['bin'] ,compiledValues['abi']



	def setFixRecord( self, addr ) :

		if self.deployed :
			_tx = self.contract_Car_Recorgnition.functions.setFixRecord( addr ).transact( { 'from': self.__adminAddr, 'to': self.receipt['contractAddress'] } )
			eth.waitForTransactionReceipt( _tx )
			return _tx

		else:
			return None



	def getCarInfos( self ) :

		if self.deployed :
			_tx = self.contract_Car_Recorgnition.functions.getCarInfos().call( {  'to': self.receipt['contractAddress'] } )
			return _tx

		else :
			return None


	def getCarAddress( self ) :

		if self.deployed :
			_tx = self.contract_Car_Recorgnition.functions.getAddr().call( {  'to': self.receipt['contractAddress'] } )
			return _tx

		else :
			return None


	
	def getTx( self, tx ) :
		_tx = eth.getTransaction( tx )
		return _tx


def getCarContract( contractAddress, contractABI ) :
	return eth.contract( address=contractAddress, abi=contractABI, ContractFactoryClass=ConciseContract )

def test( CarContract ):
	CarContract.getContract(
		{'licencePlateNumber': 'kobe', 'engineSerialNumber': 'kobe', 'factory': 'kobe', 'carStyle': 'kobe', 'carYears': '1999', 'carColor': 'blue', 'carLoading': '10', 'carPhoto': ''} 
	)

	print( CarContract.getCarInfos() )
	pass

if __name__ == '__main__':

	# test()
	Car_Recorgnition_Contract = Car_Recorgnition_Contract()
	

	test( Car_Recorgnition_Contract )

	





