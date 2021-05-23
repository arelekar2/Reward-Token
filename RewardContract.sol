// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract RewardContract {

    address private ownerAddr;
    uint256 public totalRewardsIssued;
    
    enum ParticipantType {UNKNOWN, CLIENT, BUSINESS}
    
    struct Participant {
        uint balance;
        ParticipantType pType;
    }
    
    // Map: addr -> participant data 
    mapping(address => Participant) participants;
    
    
    event Transfer(address indexed from, uint256 value, address indexed to);
    
    
    // modifier to check if caller is the contract owner
    modifier isContractOwner() {
        require(msg.sender == ownerAddr, "Caller is not contract owner!");
        _;
    }
    
    
    // Set contract deployer as merchantAddr
    constructor() {
        ownerAddr = msg.sender;
        emit Transfer(address(0), 0, msg.sender);
    }
    

    // getter for contract owner
    function getOwner() external pure returns (string memory) {
        return "MERCHANT X";
    }
    
    
    // ==================== Register participants ====================
    
    // registering participant
    function registerParticipant(address addr, ParticipantType _pType) public isContractOwner {
        // check if addr has not been already registered
        require(participants[addr].pType == ParticipantType.UNKNOWN, "Particpant already exists in the platform!");
        
        participants[addr].pType = _pType;
        participants[addr].balance = 0;
    }
    
    
    // unregistering participant
    function unregisterParticipant(address addr) public isContractOwner {
        // check if addr has been already registered
        require(participants[addr].pType != ParticipantType.UNKNOWN, "Addr is not part of the platform!");
        
        participants[addr].pType = ParticipantType.UNKNOWN;
        participants[addr].balance = 0;
    }
    
    
    
    // ==================== Transfers ====================
    
    // owner-to-participant transfer
    function issueRewards(address _toAddr, uint _amt) public isContractOwner {
        // check if Receiver is a participant
        require(participants[_toAddr].pType != ParticipantType.UNKNOWN, "Receiver is not a participant!");
        
        participants[_toAddr].balance += _amt;
        totalRewardsIssued += _amt;
        
        emit Transfer(ownerAddr, _amt, _toAddr);
    }
    
    
    // participant-to-participant transfer
    function transferP2P(address _toAddr, uint _amt) public {
        // check if Sender and Receiver are both participants
        require(participants[msg.sender].pType != ParticipantType.UNKNOWN, "Sender is not a participant!");
        require(participants[_toAddr].pType != ParticipantType.UNKNOWN, "Receiver is not a participant!");
        
        // check if Sender has enough balance to transfer
        require(participants[msg.sender].balance >= _amt, "Caller doesn't have enough balance!");
        
        participants[msg.sender].balance -= _amt;
        participants[_toAddr].balance += _amt;
        
        emit Transfer(msg.sender, _amt, _toAddr);
    }
    
    
    // participant-to-owner transfer
    function returnRewards(uint _amt) public {
        // check if Sender is a participant
        require(participants[msg.sender].pType != ParticipantType.UNKNOWN, "Sender is not a participant!");
        
        // check if Sender has enough balance to transfer
        require(participants[msg.sender].balance >= _amt, "Caller doesn't have enough balance!");
        
        participants[msg.sender].balance -= _amt;
        totalRewardsIssued -= _amt;
        
        emit Transfer(msg.sender, _amt, ownerAddr);
    }
    
    
    
    // ==================== Query balance ====================
    
    // Getter for any participant's balance
    function getBalanceFor(address _addr) external isContractOwner view returns (uint) {
        // check if given addr is a participant
        require(participants[_addr].pType != ParticipantType.UNKNOWN, "Given address is not a participant!");
        
        return participants[_addr].balance;
    }
    
    
    // Getter for self balance
    function getSelfBalance() external view returns (uint) {
        // check if Caller is a participant
        require(participants[msg.sender].pType != ParticipantType.UNKNOWN, "Caller is not a participant!");
        
        return participants[msg.sender].balance;
    }
    
    
    // Getter for total rewards issued
    function getTotalRewardsIssued() external isContractOwner view returns (uint) {
        return totalRewardsIssued;
    }
}