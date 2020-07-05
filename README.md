# EcoChain
Our project aims to support smart farming via the use of blockchains in agriculture.

By basing the project around blockchains and the use of a Raspberry Pi, it will serve to help to maintain the conditions of farmland using sensors and store said data in blockchains. 

Users will have an easier time to keep track of the state of their land and can also be easily notified when a certain aspect of the land needs to be taken care of.

Blockchain for Edge Devices Security Evaluation - Final Year Project in Singapore Polytechnic 

## How to use
1. Clone repository
```
git clone https://github.com/EcoChain-SP-FYP/ecochain.git
```
2. Install Python dependencies
```
pip install -r requirements.txt
```
3. Run the program
```
python ./main.py
```

### Testing
1. Install Truffle
```
npm install truffle -g
```
2. Install Ganache at [Ganache Github Releases](https://github.com/trufflesuite/ganache/releases)

3. Compile & Deploy contracts
```
cd Truffle
truffle migrate
```