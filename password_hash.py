import bcrypt

password = b"1234554321"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
login_password = input('Enter the password')
login_password = bytes(login_password, encoding='utf-8')

if bcrypt.checkpw(login_password, hashed):
        print('login sucessful')
else:
    print('wrong password')
    while (login_password != hashed):
        login_password = input('Enter the password')
        login_password = bytes(login_password, encoding='utf-8')
        if bcrypt.checkpw(login_password, hashed):
            print('login sucessful')
            break
        else:
            print('wrong password')