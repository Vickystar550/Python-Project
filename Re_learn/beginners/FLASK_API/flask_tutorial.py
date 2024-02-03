from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]


# POST - used to receive data
# GET - used to send data back only


#---------------------------------
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item {"name":, "price"}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_specific_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify(ErrorMessage="Store not found!")


#--------------------------------------
# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})

# GET /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item')
def get_item_in_specific_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(requested_item=store['items'])
    return jsonify({"Error": "Store item not found!"})

        
# GET /store/<string:name> 
@app.route('/store/<string:name>')
def get_specific_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(requested_store=store)
    return jsonify({"Error": "No such found!"})


app.run(port=4500)
