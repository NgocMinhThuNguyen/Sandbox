import random


def main():
    """Get score and display the result."""
    score = float(input("Enter score: "))
    print("Your result: ", check_score(score))
    random_score = get_random_score()
    print("Random score: ", random_score)
    print("Your result: ", check_score(random_score))


def check_score(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score():
    return random.randint(1, 100)


main()