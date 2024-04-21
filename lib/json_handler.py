import json
import datetime

def read_json(file_path):
    """
    :param file_path: string
    :return: dict
    """
    file = open(file_path)

    loaded_file = json.load(file)

    return loaded_file

def write_json(file_path, content):
    with open(file_path, 'w') as file:
        json_string = json.dumps(content, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        file.write(json_string)