from web3 import Web3
from smart_contract_dets import contractABI, contractAddress

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

web3.eth.defaultAccount = web3.eth.accounts[0]

print(f'Connected to blockchain: {web3.isConnected()}')

contract = web3.eth.contract(
    address=web3.toChecksumAddress(contractAddress), 
    abi=contractABI)
print(f'Current Owner: {contract.functions.getOwner().call()}')
# print(f'(Before) Total Reward Tokens issued: {contract.functions.getTotalRewardsIssued().call()}')

# ================= register clients/members
client1 = web3.eth.accounts[1]
# int ordinal can be passsed instead of enum in func call 

# tx_hash = contract.functions.registerParticipant(client1, 1).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print(f'(Before) client1 Balance: {contract.functions.getBalanceFor(client1).call()}')

# tx_hash = contract.functions.issueRewards(client1, 100).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)


client2 = web3.eth.accounts[2]

# tx_hash = contract.functions.registerParticipant(client2, 1).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print(f'(Before) client2 Balance: {contract.functions.getBalanceFor(client2).call()}')

# tx_hash = contract.functions.issueRewards(client2, 200).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)


# ================= register business/vendors
business1 = web3.eth.accounts[3]

# tx_hash = contract.functions.registerParticipant(business1, 2).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print(f'(Before) business1 Balance: {contract.functions.getBalanceFor(business1).call()}')


business2 = web3.eth.accounts[4]

# tx_hash = contract.functions.registerParticipant(business2, 2).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
# print(f'(Before) business1 Balance: {contract.functions.getBalanceFor(business2).call()}')


print(f'(After) Total Reward Tokens issued: {contract.functions.getTotalRewardsIssued().call()}')
print(f'(After) client1 Balance: {contract.functions.getBalanceFor(client1).call()}')
print(f'(After) client2 Balance: {contract.functions.getBalanceFor(client2).call()}')
print(f'(After) business1 Balance: {contract.functions.getBalanceFor(business1).call()}')
print(f'(After) business2 Balance: {contract.functions.getBalanceFor(business2).call()}')
