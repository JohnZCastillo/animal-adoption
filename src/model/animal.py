from src.model.database import db;
from src.model.type import Type;
from sqlalchemy.orm import mapped_column,Mapped,relationship

class Animal(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:  Mapped[str]
    age:  Mapped[int]
    type: Mapped["Type"] = relationship()
    
    def __init__(self,name):
        self.name = name
    