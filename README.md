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
4. After successful deployment, run: `python3 init_participants.py` to intialize the participants in the loyalty reward blockchain
5. Start the DApp: `python3 app.py`
6. Access DApp at http://localhost:8050/ & interact with loyalty reward blockchain as either merchant / client / business(vendor)
