from web3 import Web3
import json

class BlockchainLogger:
    def __init__(self, rpc_url, private_key, contract_address, abi_path):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = self.web3.eth.account.from_key(private_key)
        self.contract_address = Web3.to_checksum_address(contract_address)

        with open(abi_path, 'r') as abi_file:
            abi = json.load(abi_file)

        self.contract = self.web3.eth.contract(address=self.contract_address, abi=abi)

    def log_hash(self, data_hash):
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        txn = self.contract.functions.logHash(data_hash).build_transaction({
            'from': self.account.address,
            'nonce': nonce,
            'gas': 200000,
            'gasPrice': self.web3.to_wei('5', 'gwei'),
        })

        signed_txn = self.web3.eth.account.sign_transaction(txn, private_key=self.account.key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return tx_hash.hex()

