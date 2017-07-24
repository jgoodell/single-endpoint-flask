import time, random

from flask import Flask, make_response, request, jsonify


DEFAULT_ACCEPT = 'application/json'
DEFAULT_CONTENT_TYPE = 'application/json'


CONFLICT_JSON = {
    'Conflicts': [
        ]
    }


app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to the Garden'


@app.route('/contacts/<contact_id>/enrollments/', methods=['PUT'])
def enrollment(contact_id):
    bad_flag = random.randint(0, 10)
    
    if bad_flag == 6: # Contact Not Present
        status = 409
        CONFLICT_JSON['Conflicts'] = [request.json]
        return make_response(jsonify(CONFLICT_JSON), status)
    elif bad_flag == 2: #
        status = 500
        return make_response("500 Server Error", status)
    
    if DEFAULT_ACCEPT in request.headers['Accept']:
        if DEFAULT_CONTENT_TYPE in request.headers['Content-Type']:
            time.sleep(random.uniform(199,1000)/1000.0)
            print(contact_id)
            status = 201
        else:
            status = 415
    else:
        status = 406
    return make_response(contact_id, status)
