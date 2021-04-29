#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This programs adds together two number inputted by the user


def main():
    # this function adds together the two numbers inputted by the user

    # input
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    # process
    answer = first_number + second_number

    # output
    print("\n{0} + {1} = {2}".format(first_number, second_number, answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
