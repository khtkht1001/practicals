user_name = input("Enter name:")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(user_name))
    elif choice == "G":
        print("Goodbye {}".format(user_name))
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>").upper()
print("Finished.")

