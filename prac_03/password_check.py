def main():
    password = input_password()  # input
    masked_password = process_password(password)  # processing
    print(masked_password)  # output


def input_password():
    password = input("Enter your password:")
    while not valid_password(password):
        print("Enter a password of at least 8 character to 20 characters")
        password = input("Enter your password:")
    return password


def valid_password(password):
    return 8 <= len(password) <= 20


def process_password(password):
    printed_password = ("*"*len(password))
    return printed_password


main()