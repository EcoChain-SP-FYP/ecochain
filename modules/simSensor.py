import random
from random import randint
import time


def DHT22():
    dht22temp = round(random.uniform(-40, 80), 2)
    dht22humid = round(random.uniform(0, 1), 2)
    # time.sleep(2) # real DHT22 sensor only polls once every 2 seconds ***disabled for testing***
    return dht22temp, dht22humid


def light():
    lightLevel = round(random.uniform(0, 1), 12)
    # time.sleep(2) # ***disabled for testing***
    return lightLevel


def moisture():
    mlvl = randint(260, 520)
    if mlvl <= 440 and mlvl > 360:
        moisture = "water"
    elif mlvl <= 520 and mlvl > 440:
        moisture = "wet"
    else:
        moisture = "dry"
    # time.sleep(2)
    return moisture, mlvl


def CO2():
    co2 = round(random.uniform(50, 100), 2)
    # time.sleep(2)
    return co2


if __name__ == "__main__":
    try:
        while True:
            print("Light = " + str(light()))  # high = dark, low = bright
            print(
                "DHTtemp = " + str(DHT22()[0])
            )  # data received is in tuple, use [] to specify which value
            print("DHThumid = " + str(DHT22()[1]))
            print("Moisture category = " + str(moisture()[0]))
            print("Moisture level = " + str(moisture()[1]))
            print("CO2 = " + str(CO2()))
            print("\n")
            time.sleep(2)
    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        print("Simulation stopped")
