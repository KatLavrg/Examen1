from flask import Blueprint, request, Flask
from flask_restful import Api, Resource
from marshmallow import Schema, fields
import json

tasks = []

bp = Blueprint('tasks', __name__)

class Error(Schema):
    message = fields.String(required=True,)

class TaskS(Schema):
    description = fields.String(required=True,)
    status = fields.String(required=True,)
    title = fields.String(required=True,)

TaskSM = TaskS(many=True)

class Task:
    description = None
    status = None
    title = None

class TasksRes(Resource):
    #@bp.route('/tasks', methods=['get'])
    def get(self):
        return TaskSM.dump(tasks), 200


    #@bp.route('/tasks', methods=['post'])
    def post(self):
        a = Task
        try:
            a.description = request.json["description"]
            a.status = request.json["status"]
            a.title = request.json["title"]
            tasks.append(a)
            return '', 201
        except:
            return '', 404

class TaskRes(Resource):
    #@bp.route('/tasks/<id>', methods=['put'])
    def put(self, task_id):
        if task_id < len(tasks):
            b = Task
            try:
                b.descript = request.json["description"]
                b.status = request.json["status"]
                b.title = request.json["title"]
                tasks[task_id].remove()
                tasks.insert(task_id, b)
                return '', 204
            except:
                return '', 400
        return '', 400


    #@bp.route('/tasks/<id>', methods=['delete'])
    def delete(self, task_id):
        if task_id < len(tasks):
            tasks[task_id].remove()
            return '', 204
        return '', 400


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask("newApi")
    api = Api(app)
    api.add_resource(TasksRes, '/tasks')
    api.add_resource(TaskRes, '/tasks/<int:task_id>')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
