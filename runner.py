import csv
from methods import*

print("Welcome to the Club Manager Portal™!\nWe're super excited to have you!\nHere, you can:\n")
print("1: Get information on specific members\n2: Get broader club data\n3: Close the program\n\nType in a number to get started! (❁´◡`❁)\n")
action = input()
while (not action.isdigit()):
    action = input("Please type a number ༼ つ ◕_◕ ༽つ:")
action = int(action)
while (action < 3):
    if action == 0:
        print("\nWelcome to the Club Manager Portal™!\nWe're super excited to have you!\nHere, you can:\n")
        print("1: Get information on specific members\n2: Get broader club data\n3: Close the program\n\nType in a number to get started! (❁´◡`❁)\n")
        action = input()
        while (not action.isdigit()):
            action = input("Please type a number ༼ つ ◕_◕ ༽つ:")
        action = int(action)
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
                    print("\nWould you like to see more information? Y/N")
                    action = input().upper()
                    if action == "Y":
                        print("Position: " + get_something(name, "membership_type") + "\nMembership: " + get_membership_duration(name) + "\nHours: " + get_hours(name) + "\nPayment Status: " + get_something(name, "payment_status") 
                             + "\nSigned up: " + get_something(name, "signed_up"))
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
        print("1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
        action = input()
        while (not action.isdigit()):
            action = input("Please type a number ༼ つ ◕_◕ ༽つ:")
        action = int(action)
        while (action < 7 and action > 0):
            action = int(action)
            if action == 1:
                array = get_overdue()
                print(array)
                print("\n" + str(len(array)) + "/" + str(len(get_members())) + " members are overdue on payments!")
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
            if action == 2:
                array = get_paid()
                print(array)
                print("\n" + str(len(array)) + "/" + str(len(get_members())) + " members have paid!")
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
            if action == 3:
                print(total_revenue())
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
            if action == 4:
                array = get_signed_up()
                print(array)
                print("\n" + str(len(array)) + "/" + str(len(get_members())) + " members are signed up!")
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
            if action == 5:
                print(total_hours())
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
            if action == 6:
                print(get_members())
                action = input("\nPress enter to continue")
                print("\nPerform another action or go back to the main menu!")
                print("\n1: Get members overdue on payments\n2: Get members who have paid\n3: Get the total amount of club money\n4: Get members signed up for an upcoming event\n5: Get the total hours contributed by the club\n6: Get a list of all members\n7: Go back to the main menu!\nType in a number to get started! (¬_¬ )\n")
                action = input()
        action = 0
        continue
    elif action >= 3:
        print("Thank you for using the Club Manager Portal™! Come again soon!")
        quit()
            