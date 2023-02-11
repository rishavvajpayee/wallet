from eth_account import Account
import secrets


def new_wallet():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    account = Account.from_key(private_key)
    address = account.address
    return private_key, address
