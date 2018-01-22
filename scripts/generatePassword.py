#!/usr/bin/python
import crypt
import random
import string
import yaml

def generatePassword():
    clearPassword = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
    return clearPassword

def encryptPassword(password):
    encryptedPassword = crypt.crypt(password, '$6$' + 'salt1234')
    return encryptedPassword

with open("../ansible/params.yml", "r") as f:
    myDict = yaml.load(f)

for user in myDict['users']:
    if 'clear_password' and 'encrypted_password' in user:
        password = user['clear_password']
        if len(password) != 0:
            print("Password already exist, nothing to do !")
        else:
            clearPassword = generatePassword()
            encryptedPassword = encryptPassword(clearPassword)
            user['clear_password'] = clearPassword
            user['encrypted_password'] = encryptPassword
    else:
        clearPassword = generatePassword()
        encryptedPassword = encryptPassword(clearPassword)
        user['clear_password'] = clearPassword
        user['encrypted_password'] = encryptedPassword

with open("../ansible/params.yml", "w") as f:
    yaml.dump(myDict, f, default_flow_style=False)
