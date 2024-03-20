from flask import Blueprint,request,redirect,url_for,render_template,abort
from src.model.database import db
from src.model.type import Type
from src.model.animal import Animal
from flask_login import login_required

animal = Blueprint('animal',__name__,url_prefix='/animal')

@animal.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == 'POST':
        
        name = request.form.get('name')
        age = request.form.get('age')
        type = request.form.get('type')
        
        try:
            
            type = Type.query.filter_by(id=type).one()
            animal = Animal(name,age,type)
            
            db.session.add(animal)
            db.session.commit()

            return "ok"
        
        except:
            return "something went wrong"
    else:
        types = Type.query.all()
        return render_template('/pages/animal-registration.html',types=types)
    

@animal.post('/type')
def register_type():

    name = request.form.get('name')

    try:
        type = Type(name)
        
        db.session.add(type)
        db.session.commit()

        return redirect(url_for('animal.register'))
    
    except:
        return name
  