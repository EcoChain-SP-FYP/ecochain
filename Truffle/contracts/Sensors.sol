// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.7.0;

contract Sensors {
    string DHT22temp;
    string DHT22humid;
    string light;
    string moisture;
    string CO2;

    function setSensors(string memory DHT22tempx, string memory DHT22humidx,
     string memory lightx, string memory moisturex, string memory CO2x) public {
        DHT22temp = DHT22tempx;
        DHT22humid = DHT22humidx;
        light = lightx;
        moisture = moisturex;
        CO2 = CO2x;
    }

    function getSensors() public pure returns (string memory DHT22tempx, string memory DHT22humidx,
     string memory lightx, string memory moisturex, string memory CO2x) {
        return (DHT22tempx, DHT22humidx, lightx, moisturex, CO2x);
    }
}