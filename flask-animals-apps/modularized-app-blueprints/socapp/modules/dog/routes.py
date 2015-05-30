from flask import Blueprint
from socapp import app
import json
from socapp.models.dog.model import Dog


dog_routes = Blueprint('dogroutes', app.name)

@dog_routes.route('/gooddog/<name>', methods=['GET'])
def get_gooddog_details(name):

    dog = Dog()
    dog.setName(name)
    dog.setChasesCats(False)
    return json.dumps(dog.__dict__)

@dog_routes.route('/baddog/<name>', methods=['GET'])
def get_baddog_details(name):

    dog = Dog()
    dog.setName(name)
    dog.setChasesCats(True)
    return json.dumps(dog.__dict__)
