from web3 import Web3, HTTPProvider
import os
from interface import ContractInterface
w3 = Web3(HTTPProvider('HTTP://127.0.0.1:7545'))
print ("Latest Ethereum block number" , w3.eth.blockNumber)