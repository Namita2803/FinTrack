from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/expenses")
def get_expenses(
    db: Session = Depends(get_db)
):

    expenses = db.query(models.Expense).all()

    return expenses
@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()


    if expense is None:
        return {
            "message": "Expense not found"
        }


    db.delete(expense)
    db.commit()


    return {
        "message": "Expense deleted successfully"
    }
@router.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()


    if expense is None:
        return {
            "message": "Expense not found"
        }


    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category


    db.commit()
    db.refresh(expense)


    return expense