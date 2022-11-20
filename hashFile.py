import hashlib

file = r"<insert file location>"

BLOCK_SIZE = 65536

file_hash = hashlib.sha256()

with open(file, 'rb') as file_to_hash:
    file_block = file_to_hash.read(BLOCK_SIZE)
    while len(file_block) > 0:
        file_hash.update(file_block)
        file_block = file_to_hash.read(BLOCK_SIZE)

print(file_hash.hexdigest())

