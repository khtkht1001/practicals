def main():
    print("This program will convert Celsius to Fahrenheit or vice versa.")
    print("What do you want to convert?")
    print("(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit")
    choice = input(">").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius:"))
            result = cel_to_fah(celsius)
            print("Fahrenheit: {:.2f}".format(result))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            result = fah_to_cel(fahrenheit)
            print("Celsius: {:.2f}.".format(result))
        else:
            print("Enter a valid option.")
        print("(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit")
        choice = input(">").upper()


def cel_to_fah(celsius):
    return (celsius*(9/5))+32


def fah_to_cel(fahrenheit):
    return (fahrenheit-32)*(5/9)


main()
