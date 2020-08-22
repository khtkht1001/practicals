def main():
    email_dic = {}
    email = input("Email: ")
    while email != "":
        user_name = get_name(email)
        check_name = input("Is your name {}? (Y/n) ".format(user_name)).upper()
        if check_name != "Y" or check_name != "":
            user_name = input("Name: ")
        email_dic[email] = user_name
        email = input("Email: ")
    for email, user_name in email_dic.items():
        print("{} ({})".format(user_name, email))


def get_name(email):
    remove_email = email.split("@")[0]
    separate_names = remove_email.split(".")
    user_name = " ".join(separate_names).title()
    return user_name


if __name__ == '__main__':
    main()
