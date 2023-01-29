def check_dict_req_keys(dictionary, *keys):
    if type(dictionary) is not dict:
        return "Provided argument is not dict"
    
    missing_data = []
    for key in keys:
        if dictionary.get(key) is None:
            missing_data.append(key)

    return missing_data


def check_item_data(item, request_data=None):
    errors = []

    missing_data = check_dict_req_keys(item, "price/unit", "count", "currency")
    if len(missing_data) > 0: 
        errors.append(f"Lacking item data in database: {missing_data}.")

    price_unit_type = type(item.get("price/unit"))
    if price_unit_type is not int: 
        errors.append(f"price/unit type should be int not {price_unit_type}.")

    if request_data is not None:
        count_stock = item.get("count")
        count_request = request_data.get("count")

        count_difference = count_stock - count_request

        if count_difference < 0:
            errors.append("Requested more items than there are in stock.")

    if len(errors) > 0:
        error_message = "\n".join(errors)
        raise ValueError(error_message)
    
    return {"count_difference": count_difference, "count_stock": count_stock, "count_request": count_request}


def payment(transaction_id, user_id, price):
    pass