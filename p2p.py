from web3 import Web3
from smart_contract_dets import contractABI, contractAddress

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

web3.eth.defaultAccount = web3.eth.accounts[1]

print(f'Connected to blockchain: {web3.isConnected()}')

contract = web3.eth.contract(
    address=web3.toChecksumAddress(contractAddress), 
    abi=contractABI)
print(f'Before Client1 Balance: {contract.functions.getSelfBalance().call()}')

client2 = web3.eth.accounts[2]
# tx_hash = contract.functions.transferP2P(client2, 10).transact()
# web3.eth.waitForTransactionReceipt(tx_hash)
print(f'After Client1 Balance: {contract.functions.getSelfBalance().call()}')