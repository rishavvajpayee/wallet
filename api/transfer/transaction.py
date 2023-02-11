from web3 import Web3

infure_url = "https://mainnet.infura.io/v3/fc04cd6ad6c44e23b23f2a929d891c83"
ganache_url = "http://127.0.0.1:8545"


def make_connection():
    web = Web3(Web3.HTTPProvider(ganache_url))
    return web


def sign_and_send(web, tx, private_key):
    sign_tx = web.eth.account.signTransaction(tx, private_key)
    tx_hash = web.eth.sendRawTransaction(sign_tx.rawTransaction)
    return tx_hash


def make_transaction(from_acc, to_acc, private_key, value):
    web = make_connection()
    nonce = web.eth.getTransactionCount(from_acc)

    tx = {
        "nonce": nonce,
        "to": to_acc,
        "value": web.toWei(value, "ether"),
        "gas": 2000000,
        "gasPrice": web.toWei("20", "gwei"),
    }

    tx_hash = sign_and_send(web, tx, private_key)
    return web.toHex(tx_hash)
