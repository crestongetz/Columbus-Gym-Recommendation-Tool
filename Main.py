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


# Gets the users input using a given prompt and ensures it is a valid input
# This function hanldes letter input to ensure its valid and a single letter for searching gym types
def get_user_input_letter(prompt):

    #ensure prompt is a string, not empty, and not None
    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    if prompt is None:
        raise ValueError("Prompt cannot be None")

    while True:
        print_line()
        print("\nEnter 'q' to quit the program.")
        user_input = input(prompt).strip().lower()
        if user_input == 'q':
            return 'q'
        #if the input is a letter
        if user_input.isalpha() and len(user_input) == 1:
            return user_input
        else:
            print("Invalid input. Please enter a single letter")


# Getsthe users input using a given string prompt and ensures it is a valid input
# This function hanldes string input to ensure its valid and inside the types of gyms
def get_user_input_string(prompt):
    #ensure prompt is a string, not empty, and not None
    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    if prompt is None:
        raise ValueError("Prompt cannot be None")

    while True:
        print_line()
        print("\nEnter 'q' to quit the program.")
        user_input = input(prompt).strip().lower()
        if user_input == 'q':
            return 'q'
        if user_input in types:
            return user_input
        else:
            print("Invalid input. Please enter a valid type of gym")


def print_gym_info(gym):
    print(f"""
    Name: {gym['name'].title() if gym['name'] else 'N/A'}
    Type: {gym['type'].title() if gym['type'] else 'N/A'}
    Location: {gym['location'].title() if gym['location'] else 'N/A'}
    Rating: {gym['rating'] if gym['rating'] else 'N/A'}
    Price: ${gym['price'] if gym['price'] else 'N/A'} per month.
    """)


# This function will search the gym data for gyms that match the user input string
def search_gyms(user_input_string, Gym_Data=Gym_Data):

    user_input_string = user_input_string.lower()
    print_line()
    print(f"\nHere are all the {user_input_string.title()} gyms in Columbus, OH:")

    found = False
    for gym in Gym_Data:
        if user_input_string in gym['type'].lower():
            print_gym_info(gym)
            found = True

    if not found:
        print("No gyms found that match your input.")
        print(f"Heres the full list of gym types: {types}\n")

# User interaction function
def user_interaction():
    while True:
        #get user input for gym type
        user_input_letter = get_user_input_letter("What type of gym are you looking for?\nType the beginning letter of that type and press enter to see if it's in Columbus!: ")
        print()
        if user_input_letter == 'q':
            break

        #store a list of gym types that match the user input
        type_matches = [gym_type for gym_type in types if gym_type.startswith(user_input_letter)]

        #if there are no matches print a message and ask the user to enter a different letter
        if len(type_matches) == 0:
            print("No gyms found that match your input.")
            user_input_letter = get_user_input_letter("Would you like to see the full list of gym types? (y/n): ")
            if user_input_letter == 'y':
                print(f"Heres the full list of gym types: {types}\n")
            elif user_input_letter == 'n':
                continue
            else:
                print("Invalid input. Please enter a valid input.")
                continue



        #if there are many matches print the full list and ask the user which one they want to see
        if len(type_matches) > 1:
            print(f"The following types of gyms match your input: {type_matches}\n")
            user_input_string = get_user_input_string("Which type of gym would you like to see? (enter the full type): ")
            #if the string the user enters is like or similar to any of the types of gyms in the data print the gyms that match the string
            search_gyms(user_input_string)


        #if there is only one match print the match
        elif len(type_matches) == 1:
            print(f"The following type of gym matches your input: {type_matches[0]}")
            user_input = get_user_input_letter(f"Would you like to see the {type_matches[0].title()} gyms in Columbus, OH? (y/n): ")
            print()
            if user_input == 'y':
                search_gyms(type_matches[0])
            elif user_input == 'n':
                continue
        else:
            continue



#main function
if __name__ == "__main__":
    welcome()
    user_interaction()