import csv
from methods import*

print("Welcome to the Club Manager Portal™!\nWe're super excited to have you!\nHere, you can:\n")
print("1: Get information on specific members\n2: Get broader club data\n3: Close the program\n\nType in a number to get started! (❁´◡`❁)\n")

action = int(input())
while (action != 3):
    if action == 0:
        print("\nWelcome to the Club Manager Portal™!\nWe're super excited to have you!\nHere, you can:\n")
        print("1: Get information on specific members\n2: Get broader club data\n3: Close the program\n\nType in a number to get started! (❁´◡`❁)\n")
        action = int(input())
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
                    print("\nWould you like to see their membership duration and hours committed? Y/N")
                    action = input().upper()
                    if action == "Y":
                        print(get_membership_duration(name) + "\n" + get_hours(name))
                        print("\nPress any key to go back to the main menu!\n")
                        action = input()
                        action = 0
                    else:
                        action = 0
                else:
                    action = 0
                    continue
            else:
                print("That name was not found! Type any key to go back to the main menu!\n")
                action = input()
                action = 0
        else:
            print("That's not a number! Type any key to go back to the main menu!\n")
            action = input()
            action = 0
    elif action == 2:
        print("You chose to get club data! Here, you can:\n")
        print("1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
        action = input()
        while (action != 6 and action.isdigit()):
            action = int(action)
            if action == 1:
                print(get_overdue() )
                print("\nPerform another action or go back to the main menu!")
                action = input()
            if action == 2:
                print(get_paid())
                print("\nPerform another action or go back to the main menu!")
                action = input()
            if action == 3:
                print(total_revenue())
                print("\nPerform another action or go back to the main menu!")
                action = input()
            if action == 4:
                print(get_signed_up())
                print("\nPerform another action or go back to the main menu!")
                action = input()
            if action == 5:
                print(total_hours())
                print("\nPerform another action or go back to the main menu!")
                action = input()
        action = 0
        continue
    elif action == 3:
        print("Thank you for using the Club Manager Portal™! Come again soon!")
        quit()
            