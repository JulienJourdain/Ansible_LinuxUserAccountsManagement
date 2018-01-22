#!/usr/bin/python
import crypt
import random
import string
import yaml

# Generate a random 16 characters password
def generatePassword():
    clearPassword = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
    return clearPassword

# Encrypt clear password
def encryptPassword(password):
    encryptedPassword = crypt.crypt(password, '$6$' + 'salt1234')
    return encryptedPassword

with open("../ansible/params.yml", "r") as f:
    myDict = yaml.load(f)

for user in myDict['users']:
    # If keys exsists
    if 'clear_password' and 'encrypted_password' in user:
        password = user['clear_password']
        # And password not empty
        if len(password) != 0:
            # This means that the password already exists
            print("Password already exist, nothing to do !")
        # Else, add password entries (clear and encrypted)
        else:
            clearPassword = generatePassword()
            encryptedPassword = encryptPassword(clearPassword)
            user['clear_password'] = clearPassword
            user['encrypted_password'] = encryptPassword
    # Else, add password entries (clear and encrypted)
    else:
        clearPassword = generatePassword()
        encryptedPassword = encryptPassword(clearPassword)
        user['clear_password'] = clearPassword
        user['encrypted_password'] = encryptedPassword

# Update YAML file
with open("../ansible/params.yml", "w") as f:
    yaml.dump(myDict, f, default_flow_style=False)
