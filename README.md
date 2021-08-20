# RewardToken
Blockchain based Multifunctional Token for Loyalty Programs

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
2. Open Remix IDE in browser & Copy the contents of [RewardContract2.sol](https://github.com/arelekar2/Reward-Token/blob/main/RewardContract2.sol) (has Staking functionality) to the IDE
3. Compile & Deploy the smart contract into the local blockchain on Remix IDE
4. Copy the correct `Smart Contract Address` into the [smart_contract_dets.py](https://github.com/arelekar2/Reward-Token/blob/main/smart_contract_dets.py) file
5. After successful deployment, run: [init_participants.py](https://github.com/arelekar2/Reward-Token/blob/main/init_participants.py) to intialize the participants in the loyalty reward blockchain
6. Additionally [StakingInteraction.py](https://github.com/arelekar2/Reward-Token/blob/main/StakingInteraction.py) can be run to see the entire flow of new Staking feature
7. Start the DApp: `python3 app.py`
8. Access DApp at http://localhost:8050/ & interact with loyalty reward blockchain as either `merchant` / `client` / `business(vendor)`
