// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.7.0;

contract Sensors {
    string DHT22temp;
    string DHT22humid;
    string light;
    string moisture;
    string CO2;

    function set(string[] DHT22x, string lightx, string moisturex, string CO2x) public {
        DHT22temp = DHT22x[0];
        DHT22humid = DHT22x[1];
        light = lightx;
        moisture = moisturex;
        CO2 = CO2x;
    }

    function get() public view returns (int) {
        return (DHT22temp, DHT22humid, light, moisture, CO2);
    }
}