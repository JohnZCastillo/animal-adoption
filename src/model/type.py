from src.model.database import db;
from sqlalchemy.orm import mapped_column,Mapped

class Type(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:  Mapped[str]
    
    def __init__(self,name):
        self.name = name
    