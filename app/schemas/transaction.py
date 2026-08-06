from pydantic import BaseModel
from typing import Optional


class TransactionBase(BaseModel):
    amount: int
    status: str


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    timestamp: str

    class Config:
        orm_mode = True