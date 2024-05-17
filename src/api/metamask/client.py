from web3 import Web3
from eth_account import Account

class MetaMaskClient:
    def __init__(self, private_key, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)

    def send_transaction(self, to, value, gas, gas_price):
        tx = {
            'to': to,
            'value': self.web3.toWei(value, 'ether'),
            'gas': gas,
            'gasPrice': self.web3.toWei(gas_price, 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.account.address),
            'chainId': 1  # Mainnet ID
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)
