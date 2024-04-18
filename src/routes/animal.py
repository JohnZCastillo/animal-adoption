from flask import Blueprint,request,redirect,url_for,render_template,abort
from src.model.database import db
from src.model.type import Type
from src.model.animal import Animal
from flask_login import login_required
from flask import current_app
import os

animal = Blueprint('animal',__name__,url_prefix='/animal')

@animal.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == 'POST':
        
        name = request.form.get('name')
        age = request.form.get('age')
        type = request.form.get('type')
        
        try:
        
            file = request.files['profile']    
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            type = Type.query.filter_by(id=type).one()
            animal = Animal(name,age,type,file.filename)
            
            db.session.add(animal)
            db.session.commit()

            return "ok"
        
        except Exception as e:
            return 'Something went wrong',500
    else:
        try:
            types = Type.query.all()
            return render_template('/pages/animal-registration.html',types=types)
        except:
            return 'Something went wrong',500
            
    

@animal.post('/type')
def register_type():
    try:
        name = request.form.get('name')
        type = Type(name)
        
        db.session.add(type)
        db.session.commit()

        return redirect(url_for('animal.register'))
    
    except:
        return 'somethign went wrong',500
  