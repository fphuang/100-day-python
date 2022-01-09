import json

new_data = {
        'website#4': {
            'email': 'huang.fp@gmail.cn',
            'password': 'fxh-password'
        }
    }

# write json data

def write_json_data():
    with open('website.json', 'w') as data_file:
        json.dump(new_data, data_file, indent=4)


def load_json():
    with open('website.json', 'r') as data_file:
        data = json.load(data_file)
        print(data)
        print(type(data))


def update_json():
    with open('website.json', 'r') as data_file:
        data = json.load(data_file)
        print(data)
        data.update(new_data)
    with open('website.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)

try:
    update_json()
except Exception as ke:
    print(ke)
