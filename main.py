import json
import time
import random
import sys
from random import randint
from web3 import Web3, HTTPProvider
import simSensor

def initWeb3(blockchain_address):
    # truffle development blockchain address
    #blockchain_address = 'http://127.0.0.1:7545'
    # Client instance to interact with the blockchain
    web3 = Web3(HTTPProvider(blockchain_address))
    # Set the default account (so we don't need to set the "from" for every transaction call)
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Path to the compiled contract JSON file
    compiled_contract_path = 'Truffle/build/contracts/Sensors.json'
    # Deployed contract address (see `migrate` command output: `contract address`)
    deployed_contract_address = '0x0e08daDEbE8CBD92267Dcf0D177275C8530bF85b'

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    # Fetch deployed contract reference
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    # Call contract function (this is not persisted to the blockchain)
    #ethSensor = contract.functions.getSensors().call()
    #print(ethSensor)
    return contract

def setTransactionInputValues(contract):
    # get sensor values
    DHT22 = simSensor.DHT22()
    DHTtemp = str(DHT22[0])
    DHThumid = str(DHT22[1])
    light = str(simSensor.light())
    moisture = str(simSensor.moisture())
    CO2 = str(simSensor.CO2())
    # executes setSensor function
    tx_hash = contract.functions.setSensors(DHTtemp, DHThumid, light, moisture, CO2).transact()
    # waits for the specified transaction (tx_hash) to be confirmed
    # (included in a mined block)
    #tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash.hex()

def getLatestTransactionInputValues(contract):
    ethSensor = contract.functions.getSensors().call()
    return ethSensor

def main(blockchain_address):
    try:
        contract = initWeb3(blockchain_address)
        print(blockchain_address)
        while True:
            #print(setTransactionInputValues())
            print(f"Inputs = {getLatestTransactionInputValues(contract)}")
            time.sleep(2)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Transactions stopped")

if __name__ == "__main__":
    try:
        blockchain_address = f"http://{sys.argv[1]}:7545"
        main(blockchain_address)
    except Exception as e:
        blockchain_address = "http://127.0.0.1:7545"
        main(blockchain_address)