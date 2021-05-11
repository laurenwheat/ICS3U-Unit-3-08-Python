#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program uses a NOT boolean statement


def main():
    # this function uses a NOT boolean statement

    is_a_multiple_of_four_str = input("Enter the year: ")

    try:
        is_a_multiple_of_four = int(is_a_multiple_of_four_str)

        if (is_a_multiple_of_four % 4) == 0:
            print("That is a leap year")
        else:
            print("That is not a leap year")
    except Exception:
        print("That is not a valid input!")
    finally:
        print("Thanks for playing! <3")


if __name__ == "__main__":
    main()
