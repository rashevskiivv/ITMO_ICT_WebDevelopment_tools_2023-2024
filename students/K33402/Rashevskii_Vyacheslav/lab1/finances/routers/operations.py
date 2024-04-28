from fastapi import APIRouter, Depends
from db import get_session
from finances.models import Operation, OperationEnum

operationRouter = APIRouter(prefix="/operations", tags=["operations", "operation"])


@operationRouter.get("/available")
async def get_available():
    return {"data": list(OperationEnum)}


@operationRouter.get("/", response_model=list[Operation])
async def get_operations(session=Depends(get_session)):
    operations = session.query(Operation).all()
    return operations
    # return {"data": operations}


@operationRouter.get("/{operation_name}", response_model=Operation)
# @operationRouter.get("/{operation_name}")
async def get_operation(operation_name: str, session=Depends(get_session)):
    if operation_name not in OperationEnum:
        return {"error": "Invalid operation name"}
    operation = session.query(Operation).filter(Operation.operation == operation_name).first()
    return operation
    # return {"data": operation}


@operationRouter.post("/")
async def create_operation(operation: Operation, session=Depends(get_session)):
    operation = Operation.validate(operation)
    if operation.operation not in OperationEnum:
        return {"error": "Invalid operation name"}
    operation.id = None
    session.add(operation)
    session.commit()
    session.refresh(operation)
    return {"data": operation}


@operationRouter.patch("/{operation_name}")
async def update_operation(operation: Operation, operation_name: str, session=Depends(get_session)):
    operation = Operation.validate(operation)
    if operation.operation not in OperationEnum:
        return {"error": "Invalid operation name"}
    operation_from_db = session.query(Operation).filter(Operation.operation == operation_name).first()
    if operation_from_db is None:
        return {"data": "No such operation"}
    operation_data = operation.model_dump(exclude_unset=True)
    for key, value in operation_data.items():
        setattr(operation_from_db, key, value)
    session.add(operation_from_db)
    session.commit()
    session.refresh(operation_from_db)
    return {"data": operation_from_db}


@operationRouter.delete("/{operation_name}")
async def delete_operation(operation_name: str, session=Depends(get_session)):
    session.query(Operation).filter(Operation.operation == operation_name).delete()
    session.commit()
    return {"data": "Deleted"}
