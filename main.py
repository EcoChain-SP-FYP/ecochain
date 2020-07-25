import time
import random
import sys
from random import randint
from modules import simSensor
from datetime import datetime
from contract import contractClass


def main(blockchain_address, deployed_contract_addressx, accountx):
    try:
        contract = contractClass(
            blockchain_address, deployed_contract_addressx, accountx
        )
        print(blockchain_address)
        while True:
            DHT22 = simSensor.DHT22()
            DHTtemp = str(DHT22[0])
            DHThumid = str(DHT22[1])
            light = str(simSensor.light())
            moistureCat = str(simSensor.moisture()[0])
            moisture = str(simSensor.moisture()[1])
            CO2 = str(simSensor.CO2())
            time_now = datetime.now().strftime("%Y-%b-%d %H:%M:%S")

            print(
                contract.setTransactionInputValues(
                    DHTtemp, DHThumid, light, moistureCat, moisture, CO2, time_now
                )
            )
            print(f"Inputs = {contract.getLatestTransactionInputValues()}")
            time.sleep(2)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Transactions stopped")


if __name__ == "__main__":
    try:
        blockchain_address = f"http://{sys.argv[1]}"
        deployed_contract_address = str(sys.argv[2])
        account = int(sys.argv[3])
        main(blockchain_address, deployed_contract_address, account)
    except Exception as e:
        print("ERROR: MISSING ARGUMENTS")
        print("Usage: ./main.py {IP address:port} {Contract address} {Account index}")
