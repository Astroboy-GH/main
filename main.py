#! usr/bin/env python3
# Thee Kanittasuntorn
# Start 15/10/2025 
# Project 01
import random

def main():
    number_game()


def number_game() -> None:
    # try-except to handle mistakes 
    # eg. high lower or equal to low or wrong type
    try:
        high = int(input("Please enter highest integer: "))
        low = int(input("Please enter lowest integer: "))

        if high <= low:
            print("High input is lower or equal to low input")
            number_game()

    except ValueError:
        print("Incorrect input")
        number_game()

    print("=====Show Time=====")

    # random number from random module
    number = random.randint(low, high)

    # try-except to handle same mistake
    try:
        ans = int(input("Summit your guess here: "))
    except ValueError:
        print("Incorrect input")

    # show how the answer differ from real number
    if ans < number:
        print(f"Too low | The number is {number}")
    elif ans > number:
        print(f"Too high | The number is {number}")
    else:
        print("Right on!")


if __name__ == '__main__':
    main()