# Reward-Token
Blockchain + Smart Contract powered Loyalty Reward platform

```
Token name: RewardToken
Symbol: RT
```

## Dependencies
- Python3
- Dash & dependencies (for DApp)
- Web3 (blockchain interaction)
- Ganache (personal blockchain)
- Remix (Online Browser)


## Steps to run the proj:
1. Run Ganache
2. Open Remix IDE in browser & Copy the contents of [RewardContract.sol](https://github.com/arelekar2/Reward-Token/blob/main/RewardContract.sol) to the IDE
3. Compile & Deploy the smart contract into the local blockchain on Remix IDE
4. Copy the correct `Smart Contract Address` into the [smart_contract_dets.py](https://github.com/arelekar2/Reward-Token/blob/main/smart_contract_dets.py) file
5. After successful deployment, run: `python3 init_participants.py` to intialize the participants in the loyalty reward blockchain
6. Start the DApp: `python3 app.py`
7. Access DApp at http://localhost:8050/ & interact with loyalty reward blockchain as either `merchant` / `client` / `business(vendor)`
