from src.model.database import db;
from src.model.type import Type;
from sqlalchemy.orm import mapped_column,Mapped,relationship
from typing import Optional

class Animal(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:  Mapped[str]
    age:  Mapped[int]
    profile:  Mapped[Optional[str]]
    type_id: Mapped[int] = mapped_column(db.ForeignKey("type.id"))
    type: Mapped["Type"] = relationship()
    
    def __init__(self,name,age,type,profile):
        self.name = name
        self.age = age
        self.type = type
        self.profile = profile
    