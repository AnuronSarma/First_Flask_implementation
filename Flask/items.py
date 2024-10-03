from flask import Flask,jsonify,request

# Creates an instance of the Flask class which will be the WSGI application
app = Flask(__name__)

#Initial data in my to do list
items=[{"id":1,"name":"item 1","description":"This is item no. 1"},
       {"id":2,"name":"item 2","description":"This is item no. 2"}]

@app.route("/")
def welcome():
    print("Home route accessed")  # Print to debug
    return "Welcome to my To Do List APP"

#Retrive all the items
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

#Retrive specific item by its item no.
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    else:
        return jsonify(item)
    
#POST: Create new items
@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item={"id":items[-1]["id"]+1 if items else 1,
              "name":request.json["name"],
              "description":request.json["description"]}
    items.append(new_item)
    return jsonify(new_item)

#PUT: update existing items
@app.route("/items<int:item_id>",methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    else:
        item['name']=request.json.get('name',item['name'])
        item['description']=request.json.get('description',item['description'])
        return jsonify(item)

#DELETE: to delete items
@app.route("/items<int:item_id>",methods=['DELETE'])
def delete_items(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({"result":"item is deleted"})
 

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)