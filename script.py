from web3 import Web3
from web3 import EthereumTesterProvider
from solcx import compile_source

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
last_block = web3.eth.get_block('latest')
p = web3.is_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")
balance = web3.eth.get_balance("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")
contract_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

smart_contract = compile_source(
        """ klsdjslkjsdlsj""", 
        output_values = ['abi', 'bin']
        )
