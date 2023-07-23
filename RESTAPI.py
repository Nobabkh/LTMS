from flask import Flask, request, jsonify
import os
from client import *
from user import *
app = Flask(__name__)

@app.before_request
def check_security_header():
    if request.endpoint == 'calculate_distance':
        expected_token = '123456'
        token = request.headers.get('x-token')
        if token != expected_token:
            return jsonify({'error': 'Invalid token'}), 401
    if request.endpoint == 'register':
        auth = request.headers.get('auth-key')
        if auth == 'LAPB1234':
            return jsonify({'error': 'Not found'}), 404

@app.route('/total_distance', methods=['POST'])
def calculate_distance():
    data = request.get_json()

    lo1 = float(data['lo1'])
    la1 = float(data['la1'])
    lo2 = float(data['lo2'])
    la2 = float(data['la2'])


    total_distance = req(latitude1=lo1, longitude1=la1, latitude2=lo2, longitude2=la2)
    print(total_distance)

    response = {'total_distance': total_distance}


    headers = {'Content-Type': 'application/json'}

    return jsonify(response), 200

@app.route('/register', methods=['POST'])
def handle_register():
    data = request.get_json()
    name = str(data['name'])
    phone = str(data['phone'])
    idno = str(data['idno'])
    password = str(data['pass'])
    if Register(name, phone, idno, password):
        return jsonify({'state': True}), 200
    else:
        return jsonify({'state': False}), 200
    
@app.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    phone = str(data['phone'])
    password = str(data['pass'])
    if Login(phone, password):
        return jsonify({'state': True}), 200
    else:
        return jsonify({'state': False}), 200
    
@app.route('/total_distance', methods=['GET'])
def calculate_distance1():
    # Get data from URL parameters using request.args
    lo1 = float(request.args.get('lo1'))
    la1 = float(request.args.get('la1'))
    lo2 = float(request.args.get('lo2'))
    la2 = float(request.args.get('la2'))

    total_distance = req(latitude1=la1, longitude1=lo1, latitude2=la2, longitude2=lo2)
    print(total_distance)

    response = {'total_distance': total_distance}
    return jsonify(response), 200

@app.route('/register', methods=['GET'])
def handle_register1():
    data = request.get_json()
    name = str(request.args.get('name'))
    phone = str(request.args.get('phone'))
    idno = str(request.args.get('idno'))
    password = str(request.args.get('pass'))
    if Register(name, phone, idno, password):
        return jsonify({'state': True}), 200
    else:
        return jsonify({'state': False}), 200
    
@app.route('/login', methods=['GET'])
def handle_login1():
    phone = str(request.args.get('phone'))
    password = str(request.args.get('pass'))
    if Login(phone, password):
        return jsonify({'state': True}), 200
    else:
        return jsonify({'state': False}), 200

@app.route('/fare', methods=['POST'])
def calculate_fare():
    distance = float(request.args.get('distance'))
    fare = distance*2.5
    return jsonify({'fare': distance})

@app.route('/addcard', methods=['POST'])
def addcard():
    phone = str(request.args.get('phone'))
    card = str(request.args.get('card'))
    if(ISUSER(phone)):
        ADDCard(card)
if __name__ == '__main__':
    app.run()