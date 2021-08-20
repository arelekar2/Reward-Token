from web3 import Web3
from smart_contract_dets import contractABI, contractAddress

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# set default acc to owner 
web3.eth.defaultAccount = web3.eth.accounts[0]

print(f'===== Connected to blockchain: {web3.isConnected()} =====')

contract = web3.eth.contract(
    address=web3.toChecksumAddress(contractAddress), 
    abi=contractABI)
print(f'Current Owner: {contract.functions.getOwner().call()}')


# ================= Stake creation
client1 = web3.eth.accounts[1]

tx_hash = contract.functions.registerParticipant(client1, 1).transact()
web3.eth.waitForTransactionReceipt(tx_hash)

tx_hash = contract.functions.issueTokens(client1, 200).transact()
web3.eth.waitForTransactionReceipt(tx_hash)

web3.eth.defaultAccount = client1
tx_hash = contract.functions.createStake(10).transact()
web3.eth.waitForTransactionReceipt(tx_hash)


# ================= Stake & Reward check
print(f'client1 stake: {contract.functions.stakeOf(client1).call()}\n')


web3.eth.defaultAccount = web3.eth.accounts[0]
print(f'Total stakes in blockchain: {contract.functions.getTotalStakes().call()}')

tx_hash = contract.functions.distributeStakingRewards().transact()
web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Total distributed staking rewards: {contract.functions.getTotalStakingRewards().call()}\n')


web3.eth.defaultAccount = client1
print(f'client1 reward: {contract.functions.stakingRewardOf(client1).call()}')


# ================= UnStaking & withdrawal
tx_hash = contract.functions.withdrawStakingRewards().transact()
web3.eth.waitForTransactionReceipt(tx_hash)

tx_hash = contract.functions.removeStake(10).transact()
web3.eth.waitForTransactionReceipt(tx_hash)


print(f'Updated client1 Balance: {contract.functions.getSelfBalance().call()}')
print('===== =====')
