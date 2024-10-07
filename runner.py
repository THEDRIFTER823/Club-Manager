import csv
from methods import*

print("Welcome to the Club Manager Portal™!\nWe're super excited to have you!\nHere, you can:\n")
print("1: Get information on specific members\n2: Get broader club data\n3: Close the program\n\nType in a number to get started! (❁´◡`❁)\n")

action = int(input())
while (action != 3):
    if action == 1:
        print("You chose to get information on a specific member! Type in a name or member ID (1-1000) to pull data!\n")
        action = input()
        if action.isdigit():
            name = get_name(action)
            print(name)
            if name != "Name not found":
                print("\nWould you like to know more about " + name + "? Y/N")
                action = input().upper()
                if action == "Y":
                    print(get_info(name))
                else:
                    continue