from web3 import Web3, HTTPProvider
import json


class contractClass:
    def __init__(self, blockchain_addressx, deployed_contract_addressx, accountx):
        # self.blockchain_address = blockchain_addressx
        # self.deployed_contract_address = deployed_contract_addressx
        # self.account = accountx
        # truffle development blockchain address
        # blockchain_address = 'http://127.0.0.1:7545'
        # Client instance to interact with the blockchain
        web3 = Web3(HTTPProvider(blockchain_addressx))
        # Set the default account (so we don't need to set the "from" for every transaction call)
        web3.eth.defaultAccount = web3.eth.accounts[accountx]

        # Path to the compiled contract JSON file
        compiled_contract_path = "Truffle/build/contracts/Sensors.json"
        # Deployed contract address (see `migrate` command output: `contract address`)
        deployed_contract_address = deployed_contract_addressx

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json[
                "abi"
            ]  # fetch contract's abi - necessary to call its functions

        # Fetch deployed contract reference
        self.contract = web3.eth.contract(
            address=deployed_contract_address, abi=contract_abi
        )

        # Call contract function (this is not persisted to the blockchain)
        # ethSensor = contract.functions.getSensors().call()
        # print(ethSensor)

    def setTransactionInputValues(
        self, DHTtempx, DHThumidx, lightx, moistureCatx, moisturex, CO2x, dateTimex,
    ):

        # executes setSensor function
        tx_hash = self.contract.functions.setSensors(
            DHTtempx, DHThumidx, lightx, moistureCatx, moisturex, CO2x, dateTimex
        ).transact()
        # waits for the specified transaction (tx_hash) to be confirmed
        # (included in a mined block)
        # tx_receipt = Web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_hash.hex()

    def getLatestTransactionInputValues(self):
        ethSensor = self.contract.functions.getSensors().call()
        return ethSensor
