import hashlib

def hash(st, ec='utf-8'):
    hash_md5 = hashlib.md5("{}\n".format(st).encode(ec))
    hash_string = hash_md5.hexdigest()
    return hash_string

# print(hash('111111', 'utf-8'))