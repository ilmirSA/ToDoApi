from .models import db, Task
from flask import current_app as app
from flask import jsonify

class DaoTask:
    @staticmethod
    def get_all():
        with app.app_context():
            tasks = Task.query.all()
        return tasks

    @staticmethod
    def create_task(title,description,created_at,updated_at):
        with app.app_context():
            new_task = Task(title=title, description=description, created_at=created_at,updated_at=updated_at)
            db.session.add(new_task)
            db.session.commit()
            return {
                    "id":new_task.id,
                                                "title":new_task.title,
                    "description":new_task.description,
                                    "created_at":new_task.created_at,
                    "updated_at":new_task.updated_at,
                }

    @staticmethod
    def get_task_info(id):

        with app.app_context():
            task=Task.query.get(id)
            if task:
                return task
            else:
                return False


    @staticmethod
    def del_task(id):

            with app.app_context():
                task=Task.query.get(id)
                if task:
                    db.session.delete(task)
                    db.session.commit()
                    return True
                else:
                    return False

    @staticmethod
    def update_task(id,title,description,updated_at):
        task=Task.query.get(id)
        if task:
            task.title = title if title else task.title
            task.description =description if description else task.description
            task.updated_at=updated_at
            db.session.commit()
            return {'message': 'Task updated successfully',
                    'task': {'id': task.id, 'title': task.title, 'description': task.description,"updated_at":updated_at}}
        else:
            return False

