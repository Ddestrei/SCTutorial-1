// SPDX-License-Identifier: MIT 
// SPDX-Licence-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract Coin {
    address public creator;

    mapping(address => uint256) public balances;

    event SendCoins(address _sender, address _receiver, uint256 _amount);
    event MintCoins(address _receiver, uint256 _amount);

    constructor(){
        creator = msg.sender;
    }

    function checkAmount() public view returns (uint256){
        return balances[msg.sender];
    }

    function mint(address _receiver, uint256 _amount) public{
        require(msg.sender==creator, "You cannot change it !!!");
        balances[_receiver] +=_amount;
        emit MintCoins(_receiver, _amount);
    }

    function send(address _receiver, uint256 _amount) public{
        require(balances[msg.sender]>=_amount, "You don`t have enought coins!!!");
        balances[msg.sender]-=_amount;
        balances[_receiver]+=_amount;
        emit SendCoins(msg.sender, _receiver, _amount);
    }

    error InsufficientBalance(uint256 requested, uint256 bal_available);

}