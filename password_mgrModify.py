from cryptography.fernet import Fernet

# Uncomment this function to generate and save a new key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.strip().split("|")
            print(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")

while True:
    mode = input("Would you like to add a new password ('a'), view passwords ('v'), or quit ('q')? a/v/q: ")
    if mode == 'q':
        break
    elif mode == 'a':
        add()
    elif mode == 'v':
        view()
    else:
        print("Invalid mode.")
