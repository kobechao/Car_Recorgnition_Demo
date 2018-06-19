pragma solidity ^0.4.21;
pragma experimental ABIEncoderV2;


contract MaintananceContract {

	struct MaintananceInfo {
		address maintenanceAddr;
		address carAddr;
		string fixFactoryID;
		string fixDate;
		uint mileage;
		string fixType;
		string fixList;
		// bool hasData;
	}

	MaintananceInfo info;
	
	address admin;


	function MaintananceContract ( address _carAddr, string _fixFactoryID, string _fixDate, uint _mileage, string _fixType, string _fixList ) public {
		admin = msg.sender;

		info.maintenanceAddr = address( this );
		info.carAddr = _carAddr;
		info.fixFactoryID = _fixFactoryID;
		info.fixDate = _fixDate;
		info.mileage = _mileage;
		info.fixType = _fixType;
		info.fixList = _fixList;

	}	

	modifier isAdmin() { 
		require ( msg.sender == admin ); 
		_; 
	}
	

	function getMaintananceInfo() public view returns( address, string, string, uint, string, string )  {

		return( info.carAddr, info.fixFactoryID, info.fixDate, info.mileage, info.fixType, info.fixList );
	}
	
	
	
	function getAddr () public view returns(address)  {
		return address(this);
	}
	
}