import random
from decimal import *
import time

class simSensor:
    def DHT22():
        dht22temp = round(random.uniform(-40, 80), 2)
        dht22humid = round(random.uniform(0, 1), 2)
        #time.sleep(2) # real DHT22 sensor only polls once every 2 seconds ***disabled for testing***
        return dht22temp, dht22humid

    def light():
        lightLevel = round(random.uniform(0, 1), 12)
        #time.sleep(2) # ***disabled for testing***
        return lightLevel
    
    def moisture():
        return moisture

    def CO2():
        return co2

if __name__ == "__main__":
    try:
        while True:
            print(simSensor.light()) # high = dark, low = bright
            print(simSensor.DHT22()[0]) # data received is in tuple, use [] to specify which value
            print(simSensor.DHT22()[1])
            time.sleep(2)
    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        print("Simulation stopped")