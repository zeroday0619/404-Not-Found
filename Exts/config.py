import ujson


def Config():
    with open("config.json", 'r', encoding='utf-8') as json_file:
        json_data = ujson.load(json_file)
    return json_data
