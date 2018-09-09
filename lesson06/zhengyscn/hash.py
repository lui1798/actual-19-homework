import hashlib



# hash_md5 = hashlib.md5()
#
#
# hash_md5.update('51reboot.com\n'.encode('utf-8'))
# hash_string = hash_md5.hexdigest()
#
# print(hash_string)


hash_md5 = hashlib.md5("51reboot.com\n".encode('utf-8'))
hash_string = hash_md5.hexdigest()

print(hash_string)