from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.crud.transaction_crud import create_transaction, get_transaction, get_transactions, update_transaction, delete_transaction


def create_transaction_service(db: Session, transaction: TransactionCreate):
    return create_transaction(db, transaction)


def get_transaction_service(db: Session, transaction_id: int):
    return get_transaction(db, transaction_id)


def get_transactions_service(db: Session, skip: int = 0, limit: int = 10):
    return get_transactions(db, skip, limit)


def update_transaction_service(db: Session, transaction_id: int, transaction: TransactionUpdate):
    return update_transaction(db, transaction_id, transaction)


def delete_transaction_service(db: Session, transaction_id: int):
    return delete_transaction(db, transaction_id)