import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")
from adapters.adapter import Adapter
from blockchain import Blockchain
import db.database as database
from iota import Iota, Address, ProposedTransaction, TryteString, Bundle, Tag, TransactionHash


class IotaAdapter(Adapter):
    client = Iota('https://nodes.devnet.thetangle.org:443', testnet=True)
    credentials = database.find_credentials(Blockchain.IOTA)
    address = credentials['address']
    # There needs to be no key because it is a zero-value transfer
    key = credentials['key']

    # ---Store---
    @classmethod
    def create_transaction(cls, text):
        tx = [
            ProposedTransaction(
            # Recipient
            address=Address(cls.address
            ),
            value=0,
            tag=Tag(b'TAG'),
            message=TryteString.from_string(text),
            ),
        ]
        return tx

    @staticmethod
    def sign_transaction(tx):
        # tx will be signed and sent in send_raw_transaction
        return tx

    @classmethod
    def send_raw_transaction(cls, tx):
        # "https://pyota.readthedocs.io/en/latest/api.html#send-transfer"
        bundle = cls.client.send_transfer(
            depth=4,
            transfers=tx
        )
        bundle = bundle["bundle"]
        bundle = Bundle.as_json_compatible(bundle)
        bundle = bundle[0]
        tx_hash = bundle["hash_"]
        print(type(tx_hash))
        return tx_hash

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        # print(transaction_hash)
        # print(transaction_hash.decode(errors='ignore', strip_padding=False))
        # # print(transaction_hash.as_string())
        # print(type(transaction_hash))
        # database.add_transaction(transaction_hash, Blockchain.IOTA)
        pass

    # ---Retrieve---
    @classmethod
    def get_transaction(cls, transaction_hash):
        bundle = cls.client.get_bundles(hash)
        return bundle["bundles"][0]

    @staticmethod
    def extract_data(bundle):
        json = Bundle.as_json_compatible(bundle)
        data = json[0]["signature_message_fragment"]
        return data

    @staticmethod
    def to_text(data):
        data = TryteString.decode(data)
        return str(data)
