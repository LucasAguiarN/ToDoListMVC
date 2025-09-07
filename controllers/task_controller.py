from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all() 
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        
        if request.method == "POST":
            user_id = request.form['user_id']
            title = request.form['title']
            description = request.form['description']
            
            new_task = Task(title=title,description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("list_tasks"))

        # Buscar todos os usuários para exibir no <select> do formulário
        users = User.query.all()
        return render_template("create_task.html", users=users)


    @staticmethod
    def update_task_status(task_id):
        # Buscar a tarefa pelo id
        task = Task.query.get(task_id)
        if task is None:
            return render_template('create_task.html', error="Tarefa não existente", task_id=task_id)
        if task.status == "Pendente":
            task.status = "Concluído"
        else:
            task.status = "Pendente"
        db.session.commit()
        return redirect(url_for("list_tasks"))


    @staticmethod
    def delete_task(task_id):
        # Buscar a tarefa pelo id
        task = Task.query.get(task_id)
        if task is None:
            return render_template('create_task.html', error="Tarefa não existente", task_id=task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("list_tasks"))