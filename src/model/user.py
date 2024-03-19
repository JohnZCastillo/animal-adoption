from src.model.database import db;
from sqlalchemy.orm import mapped_column,Mapped

class User(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username:  Mapped[str] =  mapped_column(unique=True)
    password: Mapped[str]
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    