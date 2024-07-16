#lesson from Tech with Tim youtube video
from cryptography.fernet import Fernet

# Uncomment this function to generate and save a new key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#master_pwd = input("what is your master password? ")
key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like add new password 'a', view 'v' or quit 'q': a/v/q ")
    if mode == 'q':
        break
    elif mode == 'a':
        add()
    elif mode == 'v':
        view()
    else:
        print("invalid mode")
        continue
