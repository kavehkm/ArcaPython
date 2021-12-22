# using python basic file handler to save and restore `structured files`

def serializer(dict_content):
    # keys_values:
    # [
    #   'a=1',
    #   'b=2',
    #   'c=3'
    # ]
    keys_values = list()

    # merge key-value pair
    for key, value in dict_content.items():
        keys_values.append('{}={}'.format(key, value))
    
    # join all keys_values member base on '\n' and return result:
    # 'a=1\nb=2\nc=3' ...
    return '\n'.join(keys_values)


def deserializer(serialized_content):
    # hold final deserialized content
    d = dict()

    # strip all unwanted characters from both side
    serialized_content = serialized_content.strip()
    # split base on '\n'
    keys_values = serialized_content.split('\n')
    # now split keys_values into key and value base on '='
    for kv in keys_values:
        k, v = kv.split('=')
        d[k] = v
    return d


#############
# Serialize #
#############

# - settings file path
settings_file = 'settings.txt'

# - settings
settings = {
    'server': 'localhost',
    'port': '3306',
    'username': 'kavehkm',
    'password': 's3cret'
}

# - serialize settings
serialized_settings = serializer(settings)

# - write serialized settings on file
with open(settings_file, 'wt') as f:
    f.write(serialized_settings)


###############
# Deserialize #
###############

# - read serialized settings from file
with open(settings_file, 'rt') as f:
    content = f.read()

# - deserilize
deserialized_settings = deserializer(content)

# - print out result
for key, value in deserialized_settings.items():
    print('{} => {}'.format(key, value))
