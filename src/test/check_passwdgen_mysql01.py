import string
import secrets

def generate_mysql_password(length=16):
    # MySQL/MariaDB 密碼規則
    allowed_characters = string.ascii_letters + string.digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
    password = ''.join(secrets.choice(allowed_characters) for i in range(length))
    print(password)
    return password

if __name__ == "__main__":
    generate_mysql_password()