pragma solidity ^0.4.21;
/**
 * The CarInfo contract does this and that...
 */
contract CarContract {

	struct Car {
		string licencePlateNumber;
		string vehicleLicenseNumber;
		string factory;
		uint carYears;
		string carStyle;
		string carColor;
		address[] fixRecords;
	}
	
	address admin;

	Car car;

	event LogUpdateCarInfo( address addr, bool Successed );
	event LogGetCarInfos( address addr, bool Successed );
	event LogSetFixRecord( address addr, bool Successed );
	event LogUpdateCarDataLst( address addr, bool Successed );

	
	function CarContract ( string _licencePlateNumber, string _vehicleLicenseNumber, string _factory, uint _carYears, string _carStyle, string _carColor ) public {
		admin = msg.sender;

		car.licencePlateNumber = _licencePlateNumber;
		car.vehicleLicenseNumber = _vehicleLicenseNumber;
		car.factory = _factory;
		car.carYears = _carYears;
		car.carStyle = _carStyle;
		car.carColor = _carColor;
		car.fixRecords = new address[](0);

	}	


	modifier isAdmin() { 
		require ( msg.sender == admin ); 
		_;
	}


	function updateCarInfo ( string _licencePlateNumber, string _vehicleLicenseNumber, string _factory, uint _carYears, string _carStyle, string _carColor ) isAdmin public returns ( bool Successed ) {

		car.licencePlateNumber = _licencePlateNumber;
		car.vehicleLicenseNumber = _vehicleLicenseNumber;
		car.factory = _factory;
		car.carYears = _carYears;
		car.carStyle = _carStyle;
		car.carColor = _carColor;

		Successed = true;

		emit LogUpdateCarInfo( msg.sender, Successed );
	} 


	
	function getCarInfos() public view returns(string, string, string, uint, string, string, address[] ) {
		
		emit LogGetCarInfos( msg.sender, true );

		return (
			car.licencePlateNumber,
			car.vehicleLicenseNumber,
			car.factory,
			car.carYears,
			car.carStyle,
			car.carColor,
		 	car.fixRecords 
		 );
	}


	function getAddr () public constant returns(address)  {
		return address(this);
	}

 
	function setFixRecord ( address _fixRecord ) isAdmin public returns( bool Successed ) {
		car.fixRecords.push( _fixRecord );

		Successed = true;
		emit LogSetFixRecord( msg.sender, Successed );
	}


	


}
