from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
METAMASK_PRIVATE_KEY = os.getenv("METAMASK_PRIVATE_KEY")

class MetaMask:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        if not self.web3.isConnected():
            raise Exception("Failed to connect to Infura")
        self.account = self.web3.eth.account.privateKeyToAccount(METAMASK_PRIVATE_KEY)

    def get_balance(self):
        balance = self.web3.eth.get_balance(self.account.address)
        return self.web3.fromWei(balance, 'ether')

    def send_transaction(self, to_address, amount):
        nonce = self.web3.eth.getTransactionCount(self.account.address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key=METAMASK_PRIVATE_KEY)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)
