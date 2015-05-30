from socapp import app
import json
from socapp.models.monkey.model import Monkey



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
