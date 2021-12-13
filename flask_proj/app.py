from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello World!"

# @app.route('/<int:message_id>')
# def get_message(message_id):
#     return "message id: %d" %message_id

# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' %name

menus = [
    {'id': 1, 'name': 'Espresso', 'price': 38000}, 
    {'id': 2, 'name': 'Americano', 'price': 41000}, 
    {'id': 3, 'name': 'CafeLatte', 'price': 48000}
]

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})

@app.route('/menus/<int:menu_id>')
def get_menu(menu_id):
    for menu in menus:
        if menu_id == menu['id']:
            return menu
    else:
        return 'Not found'

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menus(): #request가 json이라 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() #type(request_data) == dict
    new_menu = {'id': create_menus.counter + 4, 'name': request_data['name'], 'price': request_data['price']}
    menus.append(new_menu)
    create_menus.counter += 1
    return jsonify(new_menu)
create_menus.counter = 0

@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menus(menu_id): 
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == menu_id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return menu
    else:
        return 'not found'

@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menus(menu_id):
    for i in range(len(menus)):
        if menus[i]['id'] == menu_id:
            del menus[i]
            # return menus #500 Internal Server Error
            return 'delete %d' %menu_id
    else:
        return 'not found'


if __name__ == '__main__':
    app.run()