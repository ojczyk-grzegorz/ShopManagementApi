from flask import Flask, request
import json 

from common_utils import check_dict_req_keys, check_item_data, payment
from db import get_db_data, update_db_data, retrieve_item_by_id, filter_item

app = Flask(__name__) 

@app.get("/")
def get_main_page():
    return "Welcome to Shop Management API"


@app.get("/items")
def get_items():
    return filter_item()


@app.post("/buy_item")
def buy_item():
    if request.is_json:
        request_data = request.get_json()
    else:
        return "No payload sent."
    
    missing_data = check_dict_req_keys(request_data, "transaction_id", "user_id", "item_id", "count")
    if len(missing_data) > 0: 
        return f"Lacking payload keys: {missing_data}"


    item_id = request_data.get("item_id")
    item = retrieve_item_by_id(item_id)
    if item is None:
        return "No item with provided item_id was found"
    
    try:
        item_check = check_item_data(item, request_data=request_data)
    except ValueError as e:
        return str(e)    

 
    price = item_check.get("count_request") * item.get("price/unit")
    try:
        payment(request_data.get("transaction_id"), request_data.get("user_id"), price)
    except Exception as e:
        return e


    item["count"] = item_check.get("count_difference")   
    db_data = get_db_data()
    items = db_data.get("items")
    if type(items) is dict:
        items[item_id] = item
    else:
        items = {item_id: item}

    db_data["items"] = items
    update_db_data(db_data)


    return "Transaction finished successfully."
        