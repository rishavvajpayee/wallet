from fastapi import FastAPI
from model import TransactionData
from transfer.transaction import make_transaction
from create_wallet.create_wallet import new_wallet
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Api Running successfully"}


@app.post("/api")
def transaction(transaction: TransactionData):
    from_acc = transaction.from_account
    to_acc = transaction.to_account
    private_key = transaction.private_key
    amount = transaction.amount

    hash = make_transaction(from_acc, to_acc, private_key, amount)
    message = "Successfull"
    return {
        "message": message,
        "transaction_hash": hash,
        "amount": amount,
        "from_account": from_acc,
        "to_account": to_acc,
    }


@app.get("/create-wallet")
def create_wallet():
    private_key, address = new_wallet()
    return {
        "message": "DO NOT SHARE YOUR PRIVATE KEY WITH ANYONE ELSE",
        "private_key": private_key,
        "new_address": address,
    }
