from flask import Blueprint
from socapp import app
import json
from socapp.models.monkey.model import Monkey


monkey_routes = Blueprint('monkeyroutes', app.name)

@monkey_routes.route('/goodmonkey/<name>', methods=['GET'])
def get_goodmonkey_details(name):

    monkey = Monkey()
    monkey.setName(name)
    monkey.setEatsBananas(True)
    return json.dumps(monkey.__dict__)

@monkey_routes.route('/badmonkey/<name>', methods=['GET'])
def get_badmonkey_details(name):

    monkey = Monkey()
    monkey.setName(name)
    monkey.setEatsBananas(False)
    return json.dumps(monkey.__dict__)
