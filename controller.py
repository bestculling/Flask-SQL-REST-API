from flask import request, jsonify
from models import Todo, db

def say_hello():
    return 'Hello, World'

def get_all_tasks():
    tasks = Todo.query.all()
    output = []
    for task in tasks:
        task_data = {'id': task.id, 'content': task.content, 'date_created': task.date_created}
        output.append(task_data)
    return jsonify({'tasks': output})

def create_task():
    data = request.get_json()
    new_task = Todo(content=data['content'])
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully!'})
    except Exception as e:
        return jsonify({'error': 'Failed to create task. Reason: ' + str(e)})

def get_task(id):
    task = Todo.query.get_or_404(id)
    task_data = {'id': task.id, 'content': task.content, 'date_created': task.date_created}
    return jsonify({'task': task_data})

def update_task(id):
    task = Todo.query.get_or_404(id)
    data = request.get_json()
    task.content = data['content']
    try:
        db.session.commit()
        return jsonify({'message': 'Task updated successfully!'})
    except Exception as e:
        return jsonify({'error': 'Failed to update task. Reason: ' + str(e)})

def delete_task(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully!'})
    except Exception as e:
        return jsonify({'error': 'Failed to delete task. Reason: ' + str(e)})
