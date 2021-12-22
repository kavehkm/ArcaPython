########
# TEXT #
########

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


##########
# BINARY #
##########

# read from binary file:
# - open file
bin_handler = open('testbin.bin', 'rb')         # rb: read binary
# - read content as bytes
bin_content = bin_handler.read()
# - close
bin_handler.close()
# - print out content of binary file
print(bin_content)


# write into binary file:
# - open file
bin_handler = open('testbin1.bin', 'wb')        # wb: write binary
# - write bytes on file
content = 'خسته نباشید!'
bin_handler.write(content.encode())
# - close
bin_handler.close()

# append at the end of binary file:
# - open file
bin_handler = open('testbin.bin', 'ab')         # ab: append binary
# - append
content = '\nمن در پایان فایل هستم'
bin_handler.write(content.encode())
# - close
bin_handler.close()


################
# FILE METHODS #
################

# open testtext.txt to test readonly file methods
fh = open('testtext.txt', 'rt')

# - read(n)                             read n bytes from file
fh.read(5)                              # 'sunt '
# - seek(index)                         move cursor in index position
fh.seek(10)
fh.read(2)                              # 'lp'
# - tell                                where is cursor?
fh.tell()                               # 12 
# - close                               # close open file handler
fh.close()

# open testtext2.txt to test write method
fh = open('testtext2.txt', 'wt')
# - write
fh.write('some content is here')        # 20 : number of character that wrote on the file
fh.close()
