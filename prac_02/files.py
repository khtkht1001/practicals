name_file = open("name.txt", "w")
user_name = input("Please enter your name:")
print(user_name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
name = name_file.read().strip()
name_file.close()
print(name)
