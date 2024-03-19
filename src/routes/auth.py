from flask import Blueprint,request,redirect,url_for,render_template
from src.model.database import db
from src.model.user import User
from flask_login import login_user,logout_user,login_required

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        try:
            user = db.session.execute(db.select(User).filter_by(username=username,password=password)).scalar_one()
            login_user(user)
            return redirect(url_for('homepage'))
        except:
            return redirect(url_for('auth.login'))
    else:
        return render_template('/pages/login.html')
    
@auth.post('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))