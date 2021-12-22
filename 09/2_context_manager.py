# using `Context Manager` as shortcut for working with text and binary files

########
# Read #
########
# - path to file
file_path = 'testbin.bin'
# - open handler
with open(file_path, 'rb') as file_handler:
    # - read while content
    content = file_handler.read()
    # handler closed automatically after indent
# - print out content
print(content)


#########
# Write #
#########
# - path to new file
file_path = 'testtext2_context_manager.txt'
# - content to write on new file
content = 'hey there'
# - open handler
with open(file_path, 'wt') as f:
    # - write content to new file
    f.write(content)
    # - handler closed automaticall
