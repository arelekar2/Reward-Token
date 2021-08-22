from web3 import Web3
from smart_contract_dets import contractABI, contractAddress

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# set default acc to owner 
web3.eth.defaultAccount = web3.eth.accounts[0]

print(f'\n===== Connected to blockchain: {web3.isConnected()} =====')

contract = web3.eth.contract(
    address=web3.toChecksumAddress(contractAddress), 
    abi=contractABI)


# Participants
owner = web3.eth.accounts[0]
client1 = web3.eth.accounts[1]

# ================= Stake creation
web3.eth.defaultAccount = client1
print(f'client1 Balance (Before): {contract.functions.balanceOf(client1).call()}')
tx_hash = contract.functions.createStake(10).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print(f'client1 stake: {contract.functions.stakeOf(client1).call()}')


# ================= Stake & Reward check
web3.eth.defaultAccount = owner
print(f'Total stakes in blockchain: {contract.functions.getTotalStakes().call()}\n')

tx_hash = contract.functions.distributeStakingRewards().transact()
web3.eth.waitForTransactionReceipt(tx_hash)

print(f'client1 reward: {contract.functions.stakingRewardOf(client1).call()}')
print(f'Total distributed staking rewards: {contract.functions.getTotalStakingRewards().call()}\n')


# =================  Withdrawal & UnStaking 
web3.eth.defaultAccount = client1
tx_hash = contract.functions.withdrawStakingRewards().transact()
web3.eth.waitForTransactionReceipt(tx_hash)

tx_hash = contract.functions.removeStake(10).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print(f'client1 Balance (After): {contract.functions.getSelfBalance().call()}')
print('===== =====\n')
