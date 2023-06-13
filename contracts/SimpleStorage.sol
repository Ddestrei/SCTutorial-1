// SPDX-License-Identifier: MIT 
// SPDX-Licence-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract SimpleStorage {

    uint256 sotredData;
    
    constructor(){
        set(3);
    }
    
    function set(uint256 _x) public {
        sotredData=_x;
    }

    function get() public view returns (uint256) {
        return sotredData;
    }
}