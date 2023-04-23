import random
import string

def generate_mysql_password(length=16):
    """
    Generate a MySQL/MariaDB compatible password that meets the length and complexity requirements.
    :param length: Desired length of the password (default 16)
    :return: A string representing the generated password
    """
    # Define character classes for the password
    upper_case_letters = string.ascii_uppercase
    lower_case_letters = string.ascii_lowercase
    digits = string.digits
    
    # MySQL/MariaDB requires at least one uppercase letter, one lowercase letter and one digit
    # Start with one character of each
    password = random.choice(upper_case_letters)
    password += random.choice(lower_case_letters)
    password += random.choice(digits)
    
    # Fill the rest of the password with random characters from all three character classes
    remaining_chars = length - 3
    password += ''.join(random.choice(upper_case_letters + lower_case_letters + digits) for i in range(remaining_chars))
    
    # Shuffle the characters to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(password)
    return password

if __name__ == "__main__":
    generate_mysql_password()