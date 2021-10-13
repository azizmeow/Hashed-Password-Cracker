import hashlib
import os
import sys
import termcolor

print('\n')
print('''Available hash type to decrypt are as follows: 
md5
sha1
sha256
sha512''')
print('\n')
type_of_hash = str(input('Enter the type of hash you want to decrypt (Please mention in lowercase): '))
hash_list = ['md5', 'sha1', 'sha256', 'sha512']

def hash_type_filter(hash, hashlist):
    for hash in hash_list:
        if type_of_hash in hash_list:
            return type_of_hash
        else:
            print('Hash Type Not Present For Decryption/Invalid Hash Type Specified.')
            exit(0)

hash_filter = hash_type_filter(type_of_hash, hash_list)

file_path = input('Enter password file/path for comparing hash values: ')
if os.path.exists(file_path) != True:
    print('Path/File does not exist, please enter correct file/path. ')
    sys.exit(1)

hashed_value = str(input('Enter hashed value for decryption: '))



with open(file_path, 'r') as file:
    for file in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(file.strip().encode())
            converted_hashed_value = hash_object.hexdigest()
            if hashed_value in converted_hashed_value:
                print('Password Found: ' + file)
                exit(0)

        elif type_of_hash == 'sha1':
            hash_object = hashlib.sha1(file.strip().encode())
            converted_hashed_value = hash_object.hexdigest()
            if hashed_value in converted_hashed_value:
                print('Password Found: ' + file)
                exit(0)

        elif type_of_hash == 'sha256':
            hash_object = hashlib.sha256(file.strip().encode())
            converted_hashed_value = hash_object.hexdigest()
            if hashed_value in converted_hashed_value:
                print('Password Found: ' + file)
                exit(0)

        elif type_of_hash == 'sha512':
            hash_object = hashlib.sha512(file.strip().encode())
            converted_hashed_value = hash_object.hexdigest()
            if hashed_value in converted_hashed_value:
                print('Password Found: ' + file)
                exit(0)

    print(termcolor.colored(('''Password not in file.(Try a different list) OR 
    Wrong type of hash specified among present hashes type.(You can check the type of hash value you have for decryption on internet)'''), 'red'))
