from flask import Blueprint
from socapp import app
import json
from socapp.models.cat.model import Cat


cat_routes = Blueprint('catroutes', app.name)

@cat_routes.route('/goodcat/<name>', methods=['GET'])
def get_goodcat_details(name):

    cat = Cat()
    cat.setName(name)
    cat.setHatesDogs(False)
    return json.dumps(cat.__dict__)

@cat_routes.route('/badcat/<name>', methods=['GET'])
def get_badcat_details(name):

    cat = Cat()
    cat.setName(name)
    cat.setHatesDogs(True)
    return json.dumps(cat.__dict__)
