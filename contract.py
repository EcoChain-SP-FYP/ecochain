from web3 import Web3, HTTPProvider
import json
import configparser


class contractClass:
    def __init__(self):
        # read config.ini file
        config = configparser.ConfigParser()
        configfile = "config.ini"
        try:
            config.read(configfile)
            blockchain_ip = config["DEFAULT"]["Blockchain_IP_address"]
            blockchain_port = config["DEFAULT"]["Blockchain_port"]
            self.blockchain_address = "http://" + blockchain_ip + ":" + blockchain_port
            self.contract_address = config["DEFAULT"]["Contract_address"]
            self.default_account = int(config["DEFAULT"]["Default_account"])

            # Client instance to interact with the blockchain
            web3 = Web3(HTTPProvider(self.blockchain_address))
            # Set the default account (so we don't need to set the "from" for every transaction call)
            web3.eth.defaultAccount = web3.eth.accounts[self.default_account]

            # Path to the compiled contract JSON file
            compiled_contract_path = "Truffle/build/contracts/Sensors.json"
            # Deployed contract address (see `migrate` command output: `contract address`)
            deployed_contract_address = self.contract_address

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
        except (FileNotFoundError, KeyError):
            config["DEFAULT"] = {
                "Blockchain_IP_address": "172.16.0.80",
                "Blockchain_port": "7545",
                "Contract_address": "0xe794a64514dA47296749a84193015411a17BdEe1",
                "Default_account": "0",
            }
            with open(configfile, "w") as config_file:
                config.write(config_file)
        except AttributeError:
            print(
                f"Config File: ({configfile}) corrupted, please delete {configfile} and reinitialize the app."
            )

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
