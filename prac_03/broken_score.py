def main():
    score = float(input("Enter score:"))
    print(process_score(score))


def process_score(score):
    while score > 100 or score < 0:
        return "Invalid score. (Must be between 0 and 100)"
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
