// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.7.0;

contract Sensors {
    string DHT22temp;
    string DHT22humid;
    string light;
    string moistureCat;
    string moisture;
    string CO2;
    string dateTime;

    function setSensors(
        string memory DHT22tempx,
        string memory DHT22humidx,
        string memory lightx,
        string memory moistureCatx,
        string memory moisturex,
        string memory CO2x,
        string memory dateTimex
    ) public {
        DHT22temp = DHT22tempx;
        DHT22humid = DHT22humidx;
        light = lightx;
        moistureCat = moistureCatx;
        moisture = moisturex;
        CO2 = CO2x;
        dateTime = dateTimex;
    }

    function getSensors()
        public
        view
        returns (
            string memory,
            string memory,
            string memory,
            string memory,
            string memory,
            string memory,
            string memory
        )
    {
        return (
            DHT22temp,
            DHT22humid,
            light,
            moistureCat,
            moisture,
            CO2,
            dateTime
        );
    }
}
