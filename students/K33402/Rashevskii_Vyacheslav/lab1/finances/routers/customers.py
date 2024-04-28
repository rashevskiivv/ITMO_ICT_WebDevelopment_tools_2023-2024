from fastapi import APIRouter, Depends
from db import get_session
from finances.models import Customer

customerRouter = APIRouter(prefix="/customers", tags=["customers", "customer"])


@customerRouter.get("/", response_model=list[Customer])
async def get_customers(session=Depends(get_session)):
    customers = session.query(Customer).all()
    return {"data": customers}


@customerRouter.get("/{username}", response_model=Customer)
async def get_customer(username: str, session=Depends(get_session)):
    customer = session.query(Customer).filter(Customer.username == username).first()
    return {"data": customer}


@customerRouter.post("/")
async def create_customer(customer: Customer, session=Depends(get_session)):
    customer = Customer.validate(customer)
    customer.id = None
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return {"data": customer}


@customerRouter.patch("/{username}")
async def update_customer(customer: Customer, username: str, session=Depends(get_session)):
    customer = Customer.validate(customer)
    customer_from_db = session.query(Customer).filter(Customer.username == username).first()
    if customer_from_db is None:
        return {"data": "No such customer"}
    customer_data = customer.model_dump(exclude_unset=True)
    for key, value in customer_data.items():
        setattr(customer_from_db, key, value)
    session.add(customer_from_db)
    session.commit()
    session.refresh(customer_from_db)
    return {"data": customer_from_db}


@customerRouter.delete("/{username}")
async def delete_customer(username: str, session=Depends(get_session)):
    session.query(Customer).filter(Customer.username == username).delete()
    session.commit()
    return {"data": "Deleted"}
