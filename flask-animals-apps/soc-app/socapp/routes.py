from socapp import app
import json
from model import Dog, Cat, Monkey

@app.route('/')
def index():
    return "Hello you are at the root level"


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

@app.route('/animal/monkey/goodmonkey/<name>', methods=['GET'])
def get_goodmonkey_details(name):

    monkey = Monkey()
    monkey.setName(name)
    monkey.setEatsBananas(True)
    return json.dumps(monkey.__dict__)

@app.route('/animal/monkey/badmonkey/<name>', methods=['GET'])
def get_badmonkey_details(name):

    monkey = Monkey()
    monkey.setName(name)
    monkey.setEatsBananas(False)
    return json.dumps(monkey.__dict__)
