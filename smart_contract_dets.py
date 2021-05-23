import json

with open('reward_contract_abi.json') as f:
    contractABI = json.load(f)

# replace below value with the actual smart contract address
contractAddress = '0x17131B3b0766d482366dE553624C1bBF39e31805'
