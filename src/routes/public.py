from flask import Blueprint,request,render_template
from src.model.user import User
from src.model.database import db

public = Blueprint('public',__name__)

@public.route('/')
def home():
    return "You're home!"

@public.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User(username,password)
        
        db.session.add(user)
        db.session.commit()
        
        return "ok"
    
    else:
        return render_template('/pages/register.html')

    