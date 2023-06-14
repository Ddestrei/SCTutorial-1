// SPDX-License-Identifier: MIT 
// SPDX-Licence-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract Ballot {
    address public creator;

    struct Voter{
        address delegate;
        // a = 0
        // b = 1
        // c = 2
        uint vote;
        uint weight;
        bool voted;
    }
    struct Proposal{
        string name;
        uint voteCount;
    }

    mapping(address => Voter) public voters;
    Proposal[] public proposals;

    constructor(string[] memory _name){
        creator = msg.sender;
        for (uint i=0;i<_name.length;i++){
            proposals.push(Proposal(_name[i], 0));
        }
    }

    function giveRightToVote(address _voter) external {
        require(msg.sender==creator, "Only creator can assign to vote!!!");
        require(!voters[_voter].voted, "This voter has already voted!!!");
        require(voters[_voter].weight == 0, "Voter already has the right to vote!!!");
        voters[_voter].weight = 1;
    }

    function vote(uint _proposal) external {
        Voter storage sender = voters[msg.sender];
        require(sender.weight > 0 , "No right to vote!!!");
        require(!sender.voted, "Already voted!!!");
        sender.voted=true;
        sender.vote=_proposal;
        proposals[_proposal].voteCount += sender.weight;
    }

    function delegate(address _delegateTo) external {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted!!! Cannot delegate!!!");
        require(msg.sender != _delegateTo, "YOu cannot delegate to yourself!!!");
        Voter storage _delegate = voters[_delegateTo];
        require(_delegate.weight >0, "Delegate person don`t have rights to vote!!!");
        require(!_delegate.voted, "Delegate person already vote!!!");

        sender.voted = true;
        sender.delegate = _delegateTo;
        _delegate.weight += sender.weight;
    }

    function winningProposalFunc() public view returns(string memory){
        string memory winningProposal;
        uint winningVoteCount = 0;
        for (uint i=0;i<proposals.length;i++){
            if(proposals[i].voteCount>winningVoteCount){
                winningProposal = proposals[i].name;
                winningVoteCount = proposals[i].voteCount;
            }
        }
        return winningProposal;
    }

}