from blockchain import Blockchain, blockchain
from db.credential import credential
from db.transaction import transaction

AMOUNT = 0
ENCODING = 'utf-8'
DATABASE = 'db/bcio.db'
BLOCKCHAINS = (
    blockchain(
        blockchain=Blockchain.ETHEREUM,
        name='ETHEREUM'
    ),
    blockchain(
        blockchain=Blockchain.MULTICHAIN,
        name='MULTICHAIN'
    ),
    blockchain(
        blockchain=Blockchain.BITCOIN,
        name='BITCOIN'
    ),
    blockchain(
        blockchain=Blockchain.POSTGRES,
        name='POSTGRES'
    ),
    blockchain(
        blockchain=Blockchain.STELLAR,
        name='STELLAR'
    ),
    blockchain(
        blockchain=Blockchain.HYPERLEDGER,
        name='HYPERLEDGER'
    )
)
CREDENTIALS = (
    credential(
        blockchain=Blockchain.ETHEREUM,
        address='0xDEB92221FED1Dfe74eA63c00AEde6b31F02d6ABe',
        key='d54db06062615cf2fb8133b96aa8c2becf7524c7ea7bf7f0387ee9b903b6b662'
    ),
    credential(
        blockchain=Blockchain.MULTICHAIN,
        address='1MRQf6mYRDoXjtoKVBi8huxBC69zmSzheYN4yM',
        key='V7BFGjp4wrowNSJDSouXVFJQkwZxMFDScba4SkHYA9aYjEDhLrFBV2Nd',
        user='multichainrpc',
        password='GkHfnch8QBgqvZJeMLyb57h42h6TZREr25Uhp5iZ8T2E'),
    credential(
        blockchain=Blockchain.BITCOIN,
        address='2NGMq7iBuJTeDMQPxSaEQVqMtdt3VQxuN7B',
        key='cS6kdk7zxTCij8HpXHE8Kdnh1uAM46PU5LNtQxpBZ6YjP3t3zgWL',
        user='bitcoinrpc',
        password=
        'f7efda5c189b999524f151318c0c86$d5b51b3beffbc02b724e5d095828e0bc8b2456e9ac8757ae3211a5d9b16a22ae'
    ),
    credential(
        blockchain=Blockchain.POSTGRES,
        # database name
        address='test',
        # port number
        key='5000',
        user='test',
        password='123456'),
    credential(
        blockchain=Blockchain.STELLAR,
        address='GCCAETWXN5VYPOU4MYTUGTFPTSWWNFYMDZWHWS566PUXR5GCQ7SY7QHQ',
        key='SBJF56A62FP7OEATJIDFYUTXORNJXWGXD5GBWW7TDVN2QMHDJMOXBLPK',
        user='stellar (not used)',
        password='stellar (not used)'),
    credential(
        blockchain=Blockchain.HYPERLEDGER,
        address='tbd',
        key='tbd',
        user='hyperledger (not used)',
        password='hyperledger (not used)'),
)
TRANSACTIONS = (
    transaction(
        transaction_hash='826e7100deeef7def0bfed7f5160ae6ac55a3a0cc8fca660a30488c1755e370d',
        blockchain=Blockchain.MULTICHAIN
    ),
    transaction(
        transaction_hash='151d65141a9a4a9c37fc0c8ac7aa23feb0981876b8198a970fb9956ca34e467c',
        blockchain=Blockchain.BITCOIN
    )
)
