import string
import random
import argparse

def generate_password(length, lowercase, uppercase, digits, special):
    """
    Generate a password with given length and composition
    """
    # define the character set based on composition
    charset = ''
    if lowercase:
        charset += string.ascii_lowercase
    if uppercase:
        charset += string.ascii_uppercase
    if digits:
        charset += string.digits
    if special:
        charset += string.punctuation

    # generate the password
    password = ''
    for i in range(length):
        if special and i < length - special:
            password += random.choice(string.ascii_letters + string.digits)
        else:
            password += random.choice(charset)
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a password')
    parser.add_argument('-l', '--lowercase', nargs='?', const=True, default=False,
                        help='Include lowercase letters (optionally specify the number of lowercase letters)')
    parser.add_argument('-u', '--uppercase', nargs='?', const=True, default=False,
                        help='Include uppercase letters (optionally specify the number of uppercase letters)')
    parser.add_argument('-d', '--digits', nargs='?', const=True, default=False,
                        help='Include digits (optionally specify the number of digits)')
    parser.add_argument('-s', '--special', nargs='?', const=True, default=False,
                        help='Include special characters (optionally specify the number of special characters)')
    parser.add_argument('length', type=int, nargs='?', default=12,
                        help='Length of the password (default: 12)')

    args = parser.parse_args()

    # handle the optional arguments
    lowercase = args.lowercase if args.lowercase is not None else False
    uppercase = args.uppercase if args.uppercase is not None else False
    digits = args.digits if args.digits is not None else False
    special = args.special if args.special is not None else False

    # if no composition is specified, use default composition
    if not any([lowercase, uppercase, digits, special]):
        lowercase = uppercase = digits = special = True

    # if a number is passed with an option, use it to determine the number of characters of that type
    if isinstance(args.lowercase, int):
        lowercase = args.lowercase
    elif args.lowercase is not False:
        lowercase = True

    if isinstance(args.uppercase, int):
        uppercase = args.uppercase
    elif args.uppercase is not False:
        uppercase = True

    if isinstance(args.digits, int):
        digits = args.digits
    elif args.digits is not False:
        digits = True

    if isinstance(args.special, int):
        special = args.special
    elif args.special is not False:
        special = True

    # generate the password
    password = generate_password(args.length, lowercase, uppercase, digits, special)
    print(password)
