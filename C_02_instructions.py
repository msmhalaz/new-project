# checks users enter yes (y) or no (n)


def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
         # check if the user response is a word in the list
            if item == user_response:
                return item

           # check if the user response is the same as
           # the first letter of an item in the list
            elif user_response == item[0]:
                 return item

            # print error if user does not enter something that is valid
            print(error)
            print()

def instructions():
    """"prints instructions"""

    print("""
    *** Instructions ***
    
Then played against the computer. you need to choose R (rock), P (paper), or S (scissors).
        """)


# Main routine
print()
print("💎📃✂️ Rock / Paper / Scissors Game ✂️📃💎")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want see the instructions? ")
# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()


print()
print("Program continues")
