from socapp import app
import json
from socapp.models.dog.model import Dog


@app.route('/animal/dog/gooddog/<name>', methods=['GET'])
def get_gooddog_details(name):

    dog = Dog()
    dog.setName(name)
    dog.setChasesCats(False)
    return json.dumps(dog.__dict__)

@app.route('/animal/dog/baddog/<name>', methods=['GET'])
def get_baddog_details(name):

    dog = Dog()
    dog.setName(name)
    dog.setChasesCats(True)
    return json.dumps(dog.__dict__)
