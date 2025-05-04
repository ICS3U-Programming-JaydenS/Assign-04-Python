#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: April 18, 2025
# This program repeats a subword of the selected user word given user input!


def main():
    print("Welcome to Jayden's Word Repeater!")
    print("")

    while True:
        
        # Get the user input
        user_word_as_string = input("What is your word? ")
        user_length_as_string = input(
            "What do you want the length of the subword to be? "
        )
        user_copies_as_string = input("How many copies do you want? ")

        try:
            # Convert user input to int
            user_length_as_int = int(user_length_as_string)
            user_copies_as_int = int(user_copies_as_string)

            # Check if the subword length is not bigger then the user's word: Source https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
            if user_length_as_int < 0 or user_length_as_int > len(user_word_as_string):
                print("")
                print("Subword length must be between 0 and the length of your word!")
                print("")

            # Checks if user copies is less then zero
            elif user_copies_as_int < 0:
                print("")
                print("Number of copies must be positive!")
                print("")

            # If none of those the code breaks out of the loop
            else:
                break

        # If it was not a int this happens
        except Exception:
            print("")
            print("Please enter positive numbers for the length and copies!")
            print("")
    # Get the subword Source: https://stackoverflow.com/questions/509211/how-slicing-in-python-works
    user_subword = user_word_as_string[0:user_length_as_int]

    # Looping the subword
    for counter in range(user_copies_as_int):
        print(user_subword)


if __name__ == "__main__":
    main()
