// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";
import "github.com/OpenZeppelin/openzeppelin-contracts/contracts/utils/math/SafeMath.sol";
import "github.com/OpenZeppelin/openzeppelin-contracts/contracts/access/Ownable.sol";

contract RewardContract2 is ERC20, Ownable {
    using SafeMath for uint256;

    address private _owner;
    
    enum ParticipantType {UNKNOWN, CLIENT, BUSINESS}
    
    // Map: addr -> participant data 
    mapping(address => ParticipantType) participants;
    
    
    // Set contract deployer as Owner
    constructor() ERC20("RewardToken", "RT") {
        _owner = msg.sender;
        _mint(_owner, 1000000);
    }
    

    // getter for contract owner
    function getOwner() public view virtual returns (string memory) {
        return "MERCHANT X";
    }
    
    
    // ==================== Register participants ====================
    
    // predicate to check if an address is a Participant or not
    function isParticipant(address _addr) public view returns(bool) {
        return participants[_addr] != ParticipantType.UNKNOWN;
    }
    
    // registering participant
    function registerParticipant(address _addr, ParticipantType _pType) public onlyOwner {
        // check if addr has not been already registered
        require(!isParticipant(_addr), "Particpant already exists in the platform!");
        
        participants[_addr] = _pType;
    }
    
    
    // unregistering participant
    function unregisterParticipant(address _addr) public onlyOwner {
        // check if addr has been already registered
        require(isParticipant(_addr), "Addr is not part of the platform!");
        
        participants[_addr] = ParticipantType.UNKNOWN;
    }
    
    
    
    // ==================== Transfers ====================
    
    // owner-to-participant transfer
    function issueTokens(address _toAddr, uint256 _amt) public onlyOwner {
        // check if Receiver is a participant
        require(isParticipant(_toAddr), "Receiver is not a participant!");
        
        _mint(_toAddr, _amt);
    }
    
    
    // participant-to-participant transfer
    function transferP2P(address _toAddr, uint256 _amt) public {
        // check if Sender and Receiver are both participants
        require(isParticipant(msg.sender), "Sender is not a participant!");
        require(isParticipant(_toAddr), "Receiver is not a participant!");
        
        // check if Sender has enough balance to transfer
        require(balanceOf(msg.sender) >= _amt, "Caller doesn't have enough balance!");
        
        transfer(_toAddr, _amt);
    }
    
    
    // participant-to-owner transfer
    function redeemTokens(uint256 _amt) public {
        // check if Sender is a participant
        require(isParticipant(msg.sender), "Sender is not a participant!");
        
        // check if Sender has enough balance to transfer
        require(balanceOf(msg.sender) >= _amt, "Caller doesn't have enough balance!");
        
        _burn(msg.sender, _amt);
    }
    
    
    
    // ==================== Query balance ====================
    
    // Getter for any participant's balance
    function getBalanceFor(address _addr) external onlyOwner view returns (uint256) {
        // check if given addr is a participant
        require(isParticipant(_addr), "Given address is not a participant!");
        
        return balanceOf(_addr);
    }
    
    
    // Getter for self balance
    function getSelfBalance() external view returns (uint256) {
        // check if Caller is a participant
        require(isParticipant(msg.sender), "Caller is not a participant!");
        
        return balanceOf(msg.sender);
    }
    
    
    // Getter for total RewardTokens issued
    function getTotalTokensIssued() external onlyOwner view returns (uint256) {
        return totalSupply();
    }


    // ================================ STAKING ================================

    struct Stakeholder {
        uint256 idx;
        uint256 stake;
        uint256 reward;
        bool isStakeholder;
        uint256 startTimestamp;
    }

    // A dynamic array of all stakeholders
    address[] internal stakeholders;

    // Map: addr -> staking data 
    mapping(address => Stakeholder) stakeholdersMap;
    

    // === Regarding STAKEHOLDERS === 

    // predicate to check if an address is a Stakeholder or not
    function isStakeholder(address _addr) public view returns(bool) {
        return stakeholdersMap[_addr].isStakeholder;
    }


    // method to add an address as a stakeholder
    function addStakeholder(address _addr) public {
        // check if addr is already a member of blockchain
        require(isParticipant(_addr), "Addr is not part of the platform!");
        
        if(!isStakeholder(_addr)) {
            stakeholders.push(_addr);
            stakeholdersMap[_addr].idx = stakeholders.length - 1;
            stakeholdersMap[_addr].isStakeholder = true;
        }
    }
    
    
    // method to remove an address as a stakeholder
    function removeStakeholder(address _addr) public {
        // check if addr is already a member of blockchain
        require(isParticipant(_addr), "Addr is not part of the platform!");
        
        if(isStakeholder(_addr)) {
            stakeholdersMap[_addr].isStakeholder = false;
            uint256 i = stakeholdersMap[_addr].idx;
            stakeholders[i] = stakeholders[stakeholders.length - 1];
            stakeholders.pop();
        }
    }


    // === Regarding STAKES ===

    uint256 _totalStakes = 0;

    
    // method to get stake for a stakeholder
    function stakeOf(address _stakeholder) public view returns(uint256) {
        // check if addr is already a stakeholder
        require(stakeholdersMap[_stakeholder].isStakeholder, "Addr is not one of the Stakeholders!");
        
        return stakeholdersMap[_stakeholder].stake;
    }

 
    // method to get the aggregated stakes from all stakeholders
    function getTotalStakes() public onlyOwner view returns(uint256) {
        return _totalStakes;
    }


    // method for a stakeholder to create a stake
    function createStake(uint256 _stake) public {
        _burn(msg.sender, _stake);
        addStakeholder(msg.sender);
        stakeholdersMap[msg.sender].stake += _stake;
        _totalStakes += _stake;
        stakeholdersMap[msg.sender].startTimestamp = block.timestamp;
   }

   
    // method for a stakeholder to remove a stake
    function removeStake(uint256 _stake) public {
        // check if addr is already a stakeholder
        require(stakeholdersMap[msg.sender].isStakeholder, "Addr is not one of the Stakeholders!");
        
        stakeholdersMap[msg.sender].stake -= _stake;
        removeStakeholder(msg.sender);
        _mint(msg.sender, _stake);
        _totalStakes -= _stake;
        stakeholdersMap[msg.sender].startTimestamp = 0;
    }
    
    
    // === Regarding STAKING REWARDS ===
    uint256 _stakeRewardRate = 36;
    uint256 _totalStakingRewards = 0;


    // method to check a stakeholder's rewards
    function stakingRewardOf(address _stakeholder) public view returns(uint256) {
        return stakeholdersMap[_stakeholder].reward;
    }


    // method to the aggregated rewards from all stakeholders
    function getTotalStakingRewards() public onlyOwner view returns(uint256) {
        return _totalStakingRewards;
    }


    // method to calculate the reward for each stakeholder
    function calculateStakingReward(address _addr) public view returns(uint256) {
        uint256 stake = stakeholdersMap[_addr].stake;
        uint256 daysDiff = (block.timestamp - stakeholdersMap[_addr].startTimestamp) / 86400;
        return  stake * (_stakeRewardRate / 100) * (daysDiff / 365);
    }


    // method to distribute rewards to all stakeholders
    function distributeStakingRewards() public onlyOwner {
        for (uint256 s = 0; s < stakeholders.length; s += 1) {
            address stakeholder = stakeholders[s];
            uint256 reward = calculateStakingReward(stakeholder);
            stakeholdersMap[stakeholder].reward += reward;
            _totalStakingRewards += reward;
        }
    }


    // method to allow a stakeholder to withdraw his/her rewards
    function withdrawStakingRewards() public {
        uint256 reward = stakeholdersMap[msg.sender].reward;
        stakeholdersMap[msg.sender].reward = 0;
        _totalStakingRewards -= reward;
        _mint(msg.sender, reward);
    }

}
