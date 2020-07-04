import json
import time
import random
from decimal import *
from random import randint
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'truffle/build/contracts/HelloWorld3.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x12605f76742C4ab0d0C0d30D292b1a78fb3C9a8f'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
message = contract.functions.sayHello().call()

print(message)


def moisture():
    mlvl = randint(260,520)
    if(mlvl<=350):
        moisture = "water"
    elif (mlvl<=530 and mlvl>350):
        moisture = "wet"
    else:
        moisture = "dry"
    return moisture , mlvl

def DHT22():
    dht22temp = round(random.uniform(-40, 80), 2)
    dht22humid = round(random.uniform(0, 1), 2)
    #time.sleep(2) # real DHT22 sensor only polls once every 2 seconds ***disabled for testing***
    return str(dht22temp), str(dht22humid)

def light():
    lightLevel = round(random.uniform(0, 1), 12)
    #time.sleep(2) # ***disabled for testing***
    return lightLevel

moisture, mlvl = moisture()
temp, humid = DHT22()
light = str(light())

	
while True:
    # executes setPayload function
    tx_hash = contract.functions.setPayload(moisture, mlvl, temp, humid, light).transact()
    # waits for the specified transaction (tx_hash) to be confirmed
    # (included in a mined block)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print('tx_hash: {}'.format(tx_hash.hex()))
    time.sleep(2)



