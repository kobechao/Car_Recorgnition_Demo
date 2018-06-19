pragma solidity ^0.4.21;
/**
 * The CarInfo contract does this and that...
 */
contract CarContract {

	struct Car {
		string licencePlateNumber;
		string engineSerialNumber;
		string factory;
		uint carYears;
		string carStyle;
		string carColor;
		uint carLoading;
		string carEquipments;
		address[] fixRecords;
	}
	
	address admin;

	Car car;

	event LogUpdateCarInfo( address addr, bool Successed );
	event LogGetCarInfos( address addr, bool Successed );
	event LogSetFixRecord( address addr, bool Successed );
	event LogUpdateCarDataLst( address addr, bool Successed );
	event LogSetCarEquipment( address addr, bool Successed );

	
	function CarContract ( string _licencePlateNumber, string _engineSerialNumber, string _factory, uint _carYears, string _carStyle, string _carColor,  uint _carLoading, string _carEquipments ) public {
		admin = msg.sender;

		car.licencePlateNumber = _licencePlateNumber;
		car.engineSerialNumber = _engineSerialNumber;
		car.factory = _factory;
		car.carYears = _carYears;
		car.carStyle = _carStyle;
		car.carColor = _carColor;
		car.carLoading = _carLoading;
		car.carEquipments = _carEquipments;
		car.fixRecords = new address[](0);


	}	


	modifier isAdmin() { 
		require ( msg.sender == admin ); 
		_;
	}


	function updateCarInfo ( string _licencePlateNumber, string _engineSerialNumber, string _factory, uint _carYears, string _carStyle, string _carColor, uint _carLoading ) isAdmin public returns ( bool Successed ) {

		car.licencePlateNumber = _licencePlateNumber;
		car.engineSerialNumber = _engineSerialNumber;
		car.factory = _factory;
		car.carYears = _carYears;
		car.carStyle = _carStyle;
		car.carColor = _carColor;
		car.carLoading = _carLoading;

		Successed = true;

		emit LogUpdateCarInfo( msg.sender, Successed );
	} 


	
	function getCarInfos() public view returns(string, string, string, uint, string, string, uint, address[] ) {
		
		emit LogGetCarInfos( msg.sender, true );

		return (
			car.licencePlateNumber,
			car.engineSerialNumber,
			car.factory,
			car.carYears,
			car.carStyle,
			car.carColor,
			car.carLoading,
		 	car.fixRecords 
		 );
	}


	function getAddr () public constant returns(address)  {
		return address(this);
	}

 
	function getCarEquipment() public view returns( string, bool ) {
		return ( car.carEquipments, true );
	}
	
	


	


}
