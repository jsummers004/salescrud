from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime
from fastapi_crudrouter import SQLAlchemyCRUDRouter
import models
from fastapi import FastAPI
from database import SessionLocal

app = FastAPI()

class RefStateCreate(BaseModel): #serializer
    state_id:str
    name:Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    created_on:datetime
    modified_on:Union[datetime, None]
    created_by:int
    modified_by:Optional[int]


    class Config:
        orm_mode=True

class UpdateRefState(BaseModel):
    name:str 
    modified_on:Optional[datetime]
    modified_by:Optional[int]

class RefState(RefStateCreate):
    state_id:str
    name:str 
    created_on:datetime
    modified_on:Union[datetime, None]
    created_by:int
    modified_by:Optional[int]

    class Config:
        orm_mode = True


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


router = SQLAlchemyCRUDRouter(
    schema=RefState,
    create_schema=RefStateCreate,
    update_schema=UpdateRefState,
    db_model=models.RefStateModel,
    db=get_db,
    prefix='states'
)

app.include_router(router)