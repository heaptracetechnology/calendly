import os
import requests
from flask import Flask, request, jsonify
from calendly import Calendly
from json import dumps


app = Flask(__name__)

API_KEY = os.environ['API_KEY']
calendly = Calendly(API_KEY)

def api(data,endpoint):
    res = requests.post(
        'https://calendly.com/api/v1/'+ endpoint,
        data=data,
        headers={
            'X-TOKEN': API_KEY,
        }
    )
    return res.json()

@app.route('/create', methods=['POST'])
def create():
    req = request.get_json()
    data=[]
    data={    
    "events[]":req['events'],
    "url" :req['url'],
    }
    endpoint="hooks"
    return jsonify(api(data,endpoint))

@app.route('/subscribe', methods=['POST'])
def subscribe():
    req = request.get_json()
    resp= calendly.get_webhook(req['hooksId'])
    return jsonify(resp)


@app.route('/subscribe/list', methods=['GET'])
def subscribeList():
    resp= calendly.list_webhooks()
    return jsonify(resp)

@app.route('/delete', methods=['POST'])
def deleteHook():
    req = request.get_json()
    resp= calendly.remove_webhook(req['hooksId'])
    return jsonify(resp)    

@app.route('/event/type', methods=['GET'])
def eventsList():
    resp= calendly.event_types()
    return jsonify(resp)

@app.route('/about', methods=['GET'])
def about():
    resp= calendly.about()
    return jsonify(resp)

@app.route('/health', methods=['GET'])
def health():
    return dumps(dict(
            contentType='application/json',
            data="ok",
            status=200
        ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
