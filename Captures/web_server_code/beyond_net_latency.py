from flask import Flask, make_response
import time

app = Flask(__name__)

# Load up some canned responses into memory
with open('./supercookie.txt') as c:
    supercookie = c.read()
with open('./rfc9000.txt') as qr:
    quic_response = qr.read()
with open('./v-90.txt') as sr:
    slow_response = sr.read()

@app.route('/', methods=['GET'])
def set_complex_cookie():
    resp = make_response('basic response object')
    resp.set_cookie('cookie',supercookie)
    return resp

@app.route('/quick_response', methods=['GET'])
def quick_response():
    resp = make_response(quic_response)
    return resp

@app.route('/slow_response', methods=['GET'])
def slow_respnse():
    resp = make_response(slow_response)
    time.sleep(1)
    return resp

if __name__ == "__main__":
    app.run(port=8000)