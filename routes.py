from flask import Blueprint
from controller import say_hello, get_all_tasks, create_task, get_task, update_task, delete_task

tasks_bp = Blueprint('tasks_bp', __name__)

@tasks_bp.route('/', methods=['GET'])
def hello():
    return say_hello()

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return get_all_tasks()

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    return create_task()

@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
def get_single_task(id):
    return get_task(id)

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_single_task(id):
    return update_task(id)

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_single_task(id):
    return delete_task(id)
