from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task_title = request.form.get('item')
        if task_title:
            new_task = Task(title=task_title, completed=False)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('home'))
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
