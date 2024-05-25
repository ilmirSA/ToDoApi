from flask import current_app as app
from flask import request, jsonify
from .dao import DaoTask
from datetime import datetime
@app.route('/tasks',methods=['GET'])
def get_all_tasks():
    """
        Получение списка всех задач.
    """
    result = DaoTask.get_all()
    return  jsonify(result)

@app.route('/tasks',methods=['POST'])
def create_task():
    """
    Создание новой задачи.

    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: Заголовок задачи
            description:
              type: string
              description: Описание задачи (опционально)
    """
    data = request.get_json()

    if not data.get('title',None) or not data.get('description', None) :
        return jsonify({'error': 'Invalid task data'}), 400


    title = data['title']
    description = data.get('description', None)
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
    result = DaoTask.create_task(title,description,created_at,updated_at)
    return jsonify(result),200


@app.route('/tasks/<int:id>', methods=['GET'])
def get_info_task(id):
    """
    Получение информации о задаче по ее идентификатору.

    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Идентификатор задачи
    """
    result = DaoTask.get_task_info(id)
    if result:
        return  jsonify(result),200
    else:
        return jsonify({'error': 'task not found'}), 404



@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Удаление задачи по ее идентификатору.

    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Идентификатор задачи
    """
    result = DaoTask.del_task(id)

    if not result:
        return jsonify({'error': 'task not found'}), 404
    else:
        return jsonify({'succes': 'you have successfully deleted the task'}), 200

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """
    Обновление задачи по ее идентификатору.

    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Идентификатор задачи
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: Заголовок задачи (опционально)
            description:
              type: string
              description: Описание задачи (опционально)

    """
    data =  request.get_json()
    title = data.get('title', None)
    description = data.get('description', None)
    updated_at = datetime.utcnow()
    result=DaoTask.update_task(id,title,description,updated_at)
    if result:
        return   jsonify(result)
    else:
        return jsonify({'error': 'Task not found'}), 404

