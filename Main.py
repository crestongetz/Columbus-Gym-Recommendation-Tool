from gymData import *

def print_line():
    print("-" * 100)

# Welcome message function
def welcome():
    print_line()
    print("\nWelcome to the Columbus Gym Recommendation Tool!")
    print("This tool will help you find a gym in Columbus, OH that matches your fitness goals and preferences.")
    print("Let's get started!\n")
    print_line()

#get user input and ensure it is a valid input
def get_user_input():
    while True:
        print("Enter 'q' to quit the program.")
        user_input = input("What type of gym are you looking for?\nType the beginning letter of that type and press enter to see if it's in Columbus!: ").lower()
        if user_input == 'q':
            return 'q'
        #if the input is a letter
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please try again.")


# User interaction function
def user_interaction():
    while True:
        #get user input for gym type
        user_input = get_user_input()
        print()

        if user_input == 'q':
            break

        #store a list of gym types that match the user input
        type_matches = [type for type in types if type.startswith(user_input)]

        #if there are many matches print the full list
        if len(type_matches) > 1:
            print(f"The following types of gyms match your input: {type_matches}")
        #if there is only one match print the match
        elif len(type_matches) == 1:
            print(f"The following type of gym matches your input: {type_matches[0]}")
            print("Would you like to see the gyms that match this type? (y/n)")
        #if there are no matches print a message
        else:
            print("No gyms found that match your input. ")
            print(f"Heres the full list of gym types: {types}")


#main function
if __name__ == "__main__":
    welcome()
    user_interaction()