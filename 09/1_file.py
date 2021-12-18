# read from text file:
# - open file
file_handler = open('testtext.txt', 'rt')       # rt: read-text
# - read content
file_content = file_handler.read()
# - close
file_handler.close()
# - print out file content
print(file_content)


# write into text file:
# - open file
file_handler = open('testtext1.txt', 'wt')      # wt: write-text
# - content to write on file
message = 'hello world!'
# - write content on file
file_handler.write(message)
# - close
file_handler.close()


# append at end of text file:
# - open file
file_handler = open('testtext.txt', 'at')       # at: append text
# - content to append
content = '\nIm at the end of file'
# - append
file_handler.write(content)
# - close
file_handler.close()
