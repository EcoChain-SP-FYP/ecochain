# EcoChain
Our project aims to support smart farming via the use of blockchains in agriculture.

By basing the project around blockchains and the use of a Raspberry Pi, it will serve to help to maintain the conditions of farmland using sensors and store said data in blockchains. 

Users will have an easier time to keep track of the state of their land and can also be easily notified when a certain aspect of the land needs to be taken care of.

Blockchain for Edge Devices Security Evaluation - Final Year Project in Singapore Polytechnic 

## How to use
1. Clone the repository.
```
git clone https://github.com/EcoChain-SP-FYP/ecochain.git
```
2. Install Python dependencies.
```
pip install -r requirements.txt
```
3. Configure config.ini
```
[DEFAULT]
blockchain_ip_address = 172.16.0.80
blockchain_port = 7545
contract_address = 0xe794a64514dA47296749a84193015411a17BdEe1
default_account = 0
```
4. Run the program.
```
python3 ./main.py
# to insert data into blockchain
# or
python3 ./dashboard.py
# to run webui
```

## Testing/Development environment with Truffle and Ganache
1. Install [Truffle](https://www.trufflesuite.com/truffle).
```
npm install truffle -g
```
2. Install [Ganache](https://github.com/trufflesuite/ganache/releases).

3. Compile and deploy contracts.
```
cd Truffle
truffle deploy
```

## Setting up on the Raspberry Pi
1. Download the Raspberry Pi Imager at [Raspberry Pi Foundation](https://www.raspberrypi.org/downloads/).

2. Run the Imager and choose the OS and SD card.
![RPi Imager](readme/rpi-imager-init.png)
Then click on write and wait till the image is validated.
![RPi Imager](readme/rpi-imager-complete.png)

3. In order to enable SSH and WiFi connection on the Raspberry Pi without a monitor and keyboard, we need to create some files in the SD /boot partition called 'ssh' and 'wpa_supplicant.conf' respectively.
![Config File](readme/configFile.png)

4. In "wpa_supplicant.conf", we will configure the connection to a WiFi network.
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=SG

network={
 ssid="{WiFi-Name}"
 psk="{WiFi-Password}"
}
```
5. Insert micro SD card into Raspberry Pi.
6. Power up the Raspberry Pi.
7. Find the IP Address of the Raspberry Pi by going to your router's WebUI usually at `192.168.1.1` via a browser.
8. SSH into the Raspberry Pi with the default user `pi` and enter the default password `raspberry`.
```
ssh pi@{IP address}
```