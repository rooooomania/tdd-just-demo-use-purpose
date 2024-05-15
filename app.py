# app.py
from flask import Flask, make_response


app = Flask(__name__)

@app.route('/')
def hello_world():
    response = make_response('Hello, World!')
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response

# @app.route('/parrot')
# def parrot():
#     say = request.args.get('say', '')
#     response = make_response(say)
#     response.headers['Content-Type'] = 'text/plain; charset=utf-8'
#     return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
