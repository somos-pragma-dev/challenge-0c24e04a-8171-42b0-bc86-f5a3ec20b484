from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.services.transaction_service import create_transaction_service, get_transaction_service, get_transactions_service, update_transaction_service, delete_transaction_service
from app.dependencies import get_db


router = APIRouter()


@router.post("/transactions/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction_service(db, transaction)


@router.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_service(db, transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/transactions/")
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    transactions = get_transactions_service(db, skip, limit)
    return transactions


@router.put("/transactions/{transaction_id}")
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    updated_transaction = update_transaction_service(db, transaction_id, transaction)
    if updated_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction


@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    deleted = delete_transaction_service(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted"}