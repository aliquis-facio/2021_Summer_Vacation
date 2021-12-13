from flask import Flask, json, jsonify, request
# from urllib.parse import urlsplit, parse_qsl

app = Flask(__name__)

@app.route('/whoami')
def get_git():
    return jsonify({'name': 'jenych0314'})

@app.route('/echo')
def get_value():
    data = request.args.get('value')
    if data:
        return jsonify({'value': data})
    return 'Nothing happened'

weapons = [{"name": "knife", "stock": 4}]

@app.route('/weapons', methods = ['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = {'name':request_data['name'], 'stock':request_data['stock']}
    weapons.append(new_weapon)
    return jsonify(new_weapon)

@app.route('/weapons', methods = ['GET'])
def read_weapon_all():
    return jsonify(weapons)

@app.route('/weapons/<name>', methods = ['GET'])
def read_weapon_single(name):
    if name:
        for weapon in weapons:
            if weapon['name'] == name:
                return weapon
        else:
            return 'not found'
    else:
        read_weapon_all()

@app.route('/weapons/<name>', methods = ['PUT'])
def update_weapon(name):
    request_data = request.get_json()
    if name:
        for weapon in weapons:
            if weapon['name'] == name:
                weapon['name'] = request_data['name']
                weapon['stock'] = request_data['stock']
                return weapon
        else:
            return 'not found'
    else:
        return 'Currently exsist weapons list:\n' + read_weapon_all

@app.route('/weapons/<name>', methods = ['DELETE'])
def delete_weapon(name):
    if name:
        for i in range(len(weapons)):
            if weapons[i]['name'] == name:
                abandoned = weapons.pop(i)
                return 'delete ' + abandoned['name']
        else:
            return 'not found'
    else:
        return 'Currently exsist weapons list:\n' + read_weapon_all

if __name__ == '__main__':
    app.run()