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

out = read_json("secrets/data.json")
query_word = "KILL"

count = 0
for userid in out.keys():
    for k, v in out[userid].items():
        if query_word in k:
            count += v

print(f"{query_word} has been said {count} times")

top_userid = 0
num = 0
for userid in out.keys():
    for k, v in out[userid].items():
        if query_word in k and v > num:
            num = v
            top_userid = userid

print(num)
print(top_userid)