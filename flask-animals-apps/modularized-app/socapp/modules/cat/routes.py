from socapp import app
import json
from socapp.models.cat.model import Cat


@app.route('/animal/cat/goodcat/<name>', methods=['GET'])
def get_goodcat_details(name):

    cat = Cat()
    cat.setName(name)
    cat.setHatesDogs(False)
    return json.dumps(cat.__dict__)

@app.route('/animal/cat/badcat/<name>', methods=['GET'])
def get_badcat_details(name):

    cat = Cat()
    cat.setName(name)
    cat.setHatesDogs(True)
    return json.dumps(cat.__dict__)
