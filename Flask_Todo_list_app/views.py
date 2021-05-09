from flask import render_template, redirect, url_for, request
from Flask_Todo_list_app import db
from Flask_Todo_list_app.models import Todo
from Flask_Todo_list_app import app



@app.route('/', methods=['GET', 'POST'])
def home():
    #gets all tasks that is yet to be completed
    tasks = Todo.query.filter_by(is_Completed = False).all()
        
    return render_template('base.html', tasks = tasks)



@app.route('/completed', methods=['GET', 'POST'])
def completed():
    #gets all tasks that are completed
    tasks = Todo.query.filter_by(is_Completed = True).all()

    return render_template('completed.html', tasks = tasks)



@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.form:

        try:
            task = str(request.form['todo'])
        except:
            KeyError = 'todo'

        newtask = Todo(task)
        db.session.add(newtask)
        db.session.commit()
            
        return redirect(url_for('home'))

    return render_template('base.html')



@app.route('/<int:id>/remove', methods=['GET', 'POST'])
def delete(id):
            
    task = Todo.query.get(id)
    db.session.delete(task)
    db.session.commit()        
    return redirect(url_for('home'))

@app.route('/cleartask', methods=['GET', 'POST'])
def clearall():
            
    tasks = Todo.query.all()

    for task in tasks:

        db.session.delete(task)
        db.session.commit()

    return redirect(url_for('home'))


@app.route('/done/<int:id>', methods=['GET', 'POST'])
def done(id):
            
    task = Todo.query.get(id)
    task.is_Completed = True
    db.session.commit()  
    
    return redirect(url_for('home'))

