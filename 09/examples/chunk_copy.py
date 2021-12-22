# standard
from os import read
import time


CHUNK_SIZE = 1024 * 100 # 100KB


# source and destination files path
source_file_path = 'top_10000000_passwords.txt'
destination_file_path = 'top_passwords_copy.txt'


# open source file for read
source_fh = open(source_file_path, 'rt')
# open destination file to write
destination_fh = open(destination_file_path, 'wt')


# track how many readed from file
readed = 0


# read content by CHUNK_SIZE for first time
content = source_fh.read(CHUNK_SIZE)
# - update readed value
readed += len(content)


# check for content
while content:
    # write content of destination file
    destination_fh.write(content)
    print('{} bytes wrote on destination file'.format(readed))
    time.sleep(0.2)
    # read remain content and update readed
    content = source_fh.read(CHUNK_SIZE)
    readed += len(content)


# clouse source and destination files
source_fh.close()
destination_fh.close()


# job done!, tell user about success
print('copy done successfully')
