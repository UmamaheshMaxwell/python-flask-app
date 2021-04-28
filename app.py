from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/" , methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete= Todo.query.get_or_404(id)

    try: 
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return 'There was a problem deleting that task'


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
        task= Todo.query.get_or_404(id)
        data = request.get_json()
        task.content = data['content']
        try: 

            db.session.commit()
            return redirect("/")
        except:
            return 'There was a problem updating that task'


@app.route("/getTaskById/<int:id>", methods=["GET"])
def getTaskById(id):
    task = Todo.query.get_or_404(id)
    return jsonify(id =task.id, content=task.content)


if __name__ == "__main__":
    app.run(debug=True)