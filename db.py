from flask import request

DB_FILEPATH = "./db.json"


def get_db_data():
    with open(DB_FILEPATH) as db_file:
        data = json.load(db_file)
        return data if type(data) is dict else {}
    

def update_db_data(new_db_data):
    json_string = json.dumps(new_db_data)
    with open(DB_FILEPATH, "w") as db_file:
        db_file.write(json_string)




def retrieve_items():
    all_shop_items = get_db_data().get("items")
    return all_shop_items if type(all_shop_items) is dict else {}


def retrieve_item_by_id(id):
    return retrieve_items().get(id)


def filter_item(**filters):
    filters = request.get_json() if request.is_json else None

    items = retrieve_items()

    if type(filters) is dict:
        for item_id, item_params in list(items.items()):
            for filter, filter_value in list(filters.items()):
                if item_params.get(filter) != filter_value:
                    items.pop(item_id)
                    break
    
    return items

    