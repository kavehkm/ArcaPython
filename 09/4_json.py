# standard
import json
import random
import string


def json_serializer(dict_content):
    return json.dumps(dict_content, indent=4)


def json_deserializer(serialized_content):
    return json.loads(serialized_content)



#############
# Serialize #
#############

# - configs file path
configs_file = 'configs.json'

# configs
configs = {
    'url': 'https://api.dropbox.com',
    'token': ''.join(random.choices(string.ascii_letters + string.punctuation, k=20)),
    'data': {
        'a': 1,
        'b': 2,
        'c': 3,
    }
}

# - serialize configs
serialized_configs = json_serializer(configs)

# - write serialized configs on file
with open(configs_file, 'wt') as f:
    f.write(serialized_configs)


###############
# Deserialize #
###############

# - read serialized configs from file
with open(configs_file, 'rt') as f:
    content = f.read()

# - deserilize
deserialized_configs = json_deserializer(content)

# - print out result
for key, value in deserialized_configs.items():
    print('{} => {}'.format(key, value))
