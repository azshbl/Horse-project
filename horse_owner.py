

def request_stable_service():
    print("--- boarding ---")

    owner_name = input("Enter Owner Name: ")                                       # If I had more time, I would improve this code and add features to it.
    horse_name = input("Enter Horse Name: ")
    horse_age = input("Enter your horse age: ")
    horse_gender =inout("Enter your horse gender: ")


    print("\nChoose boarding Duration:")
    print("1. 1 Month  (1,500 SAR)")
    print("2. 3 Months (4,300 SAR)")
    print("3. 5 Months (7,300 SAR)")
    print("4. 7 Months (10,300 SAR)")
    print("5. 9 Months (13,300 SAR)")
    print("6. 11 Months (16,300 SAR)")
    print("7. 1 Year/12 Months (17,500 SAR)")

    duration_choice = input("Select 1 to 7: ")

    if duration_choice == "1":
        print("Success! boarding requested for 1 Month. Cost: 1500 SAR")            # I enjoyed the if statement concept; writing the conditions was beautiful.
    elif duration_choice == "2":
        print("Success! boarding requested for 3 Months. Cost: 4300 SAR")
    elif duration_choice == "3":
        print("Success! boarding requested for 5 Months. Cost: 7300 SAR")
    elif duration_choice == "4":
        print("Success! boarding requested for 7 Months. Cost: 10300 SAR")
    elif duration_choice == "5":
        print("Success! boarding requested for 9 Months. Cost: 13300 SAR")
    elif duration_choice == "6":
        print("Success! boarding requested for 11 Months. Cost: 16300 SAR")
    elif duration_choice == "7":
        print("Success! boarding requested for 1 Year. Cost: 17500 SAR")
    else:
        print("Invalid choice.")



def view_my_horses():
    print("--- View My Horses ---")

    owner_name = input("Enter your name: ")


    for x in horses:
        horse_data = horses[x]

        if horse_data["owner_name"] == owner_name:
            print("Horse Name:", horse_data["horse_name"])




def horse_owner_menu():
    while True:
        print("\n=== Horse Owner Menu ===")                 #This part of the code was very challenging for me as I had to search through many data sources.
        print("1. boarding")
        print("2. View My Horses")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            request_stable_service()
        elif choice == "2":
            view_my_horses()
        elif choice == "0":
            break

horse_owner_menu()










# ================= HORSE OWNER FUNCTIONS =================

def request_stable_service():
    print("        \nBOARDING REQUEST       ")

    owner_name = input("Enter Owner Name: ")
    horse_name = input("Enter Horse Name: ")
    horse_age = input("Enter your horse age: ")
    horse_gender = input("Enter your horse gender (male / female): ")   ###### male or female only

    print("\nChoose boarding Duration:")
    print("1. 1 Month  (1,500 SAR)")
    print("2. 3 Months (4,300 SAR)")
    print("3. 5 Months (7,300 SAR)")
    print("4. 7 Months (10,300 SAR)")
    print("5. 9 Months (13,300 SAR)")
    print("6. 11 Months (16,300 SAR)")
    print("7. 1 Year/12 Months (17,500 SAR)")

    duration_choice = input("Select 1 to 7: ")

    if duration_choice == "1":
        duration = "1 Month"
        cost = 1500
    elif duration_choice == "2":
        duration = "3 Months"
        cost = 4300
    elif duration_choice == "3":
        duration = "5 Months"
        cost = 7300
    elif duration_choice == "4":
        duration = "7 Months"
        cost = 10300
    elif duration_choice == "5":
        duration = "9 Months"
        cost = 13300
    elif duration_choice == "6":
        duration = "11 Months"
        cost = 16300
    elif duration_choice == "7":
        duration = "1 Year"
        cost = 17500
    else:
        print("Invalid choice.")
        return

    print("\nSuccess! Boarding request submitted.")
    print("Owner Name:", owner_name)
    print("Horse Name:", horse_name)
    print("Horse Age:", horse_age)
    print("Horse Gender:", horse_gender)
    print("Duration:", duration)
    print("Cost:", cost, "SAR")


def view_my_horses():
    print("\n--- VIEW MY HORSES ---")

    owner_name = input("Enter your name: ")
    found = False

    for x in horses:
        horse_data = horses[x]

        if horse_data["owner_name"].lower() == owner_name.lower():
            print("Horse Name:", horse_data["horse_name"])
            print("Status:", horse_data["status"])
            print("-" * 20)
            found = True

    if found == False:
        print("No horses found for this owner.")


def horse_owner_menu():
    while True:
        print("\n=== HORSE OWNER MENU ===")
        print("1. Boarding")
        print("2. View My Horses")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            request_stable_service()
        elif choice == "2":
            view_my_horses()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
