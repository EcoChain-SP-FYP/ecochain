import time
from modules import simSensor
from datetime import datetime
from contract import contractClass


def main():
    try:
        contract = contractClass()
        print(
            "Address: ",
            contract.blockchain_address,
            "\nAccount: ",
            contract.default_account,
        )
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
            time.sleep(5)
    except KeyboardInterrupt:
        print("Transactions stopped")
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    main()
