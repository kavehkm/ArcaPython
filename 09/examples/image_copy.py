# source and destination files path
source_path = 'python_creators.jpg'
destination_path = 'python_creators_copy.jpg'


# nested handlers
with open(source_path, 'rb') as source:         # binary mode: cause of jpg image
    with open(destination_path, 'wb') as dest:
        content = source.read()                 # read whole content
        dest.write(content)                     # write content at once
        # destination handler closed automatically
    # source handler closed automatically


# tell user about success
print('copy done successfully')
