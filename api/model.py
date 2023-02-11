from typing import Union
from pydantic import BaseModel


class TransactionData(BaseModel):
    from_account: str
    to_account: str
    private_key: str
    amount: float
