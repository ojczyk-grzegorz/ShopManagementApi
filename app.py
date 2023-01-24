from flask import Flask, request
import json 


app = Flask(__name__) 

@app.get("/")
def get_main_page():
    return "Welcome to Shop Management API"


@app.get("/items")
def get_items():
    return get_db_data().get("items") 


@app.post("/buy_item")
def buy_item():
    request_data = request.get_json() 
    item_name = request_data.get("name")
    items = get_items()
    for id, data in items.items():
        if data.get("name") == item_name:
            new_data = {**data}
            new_data["count"] = data.get("count") - request_data.get("count")
            items[id] = new_data
            new_db_data = get_db_data()
            new_db_data["items"] = items
            update_db_data(new_db_data)
            return new_db_data

    return "Item not found."
    
    


DB_FILEPATH = "./db.json"


def get_db_data():
    with open(DB_FILEPATH) as db_file:
        return json.load(db_file)
    

def update_db_data(new_db_data):
    json_string = json.dumps(new_db_data)
    with open(DB_FILEPATH, "w") as db_file:
        db_file.write(json_string)