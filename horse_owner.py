def request_stable_service():
    print("--- boarding ---")

    owner_name = input("Enter Owner Name: ")                                       
    owner_phone = input("Enter Owner Phone Number: ")                                # If I had more time, I would improve this code and add features to it.
    horse_name = input("Enter Horse Name: ")
    horse_age = input("Enter your horse age: ")

    horse_gender = input("Enter your horse gender (male / female): ")
    if horse_gender != "male" and horse_gender != "female":
        print("Invalid input! Please enter 'male' or 'female' only.")
        return

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
        print("Success! boarding requested for 1 Month. Cost: 1500 SAR")            
    elif duration_choice == "2":
        print("Success! boarding requested for 3 Months. Cost: 4300 SAR")             # I enjoyed the if statement concept; writing the conditions was beautiful.
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
        return

    print(f"An invitation has been sent successfully!")


def view_my_horses():
    print("--- View My Horses ---")

    owner_name = input("Enter your name: ")

    for x in horses:
        horse_data = horses[x]

        
        if horse_data["owner_name"].lower() == owner_name.lower():
            print("Horse Name:", horse_data["horse_name"])


def horse_owner_menu():
    while True:
        print("\n=== Horse Owner Menu ===")                       #This part of the code was very challenging for me as I had to search through many data sources.   
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
        else:
            print("Invalid choice.")

horse_owner_menu()





























# ================= HORSE OWNER FUNCTIONS =================

def request_stable_service():
    print("--- boarding ---")

    owner_name = input("Enter Owner Name: ")
    owner_phone = input("Enter Owner Phone Number: ")                               
    horse_name = input("Enter Horse Name: ")
    horse_age = input("Enter your horse age: ")

    horse_gender = input("Enter your horse gender (male / female): ")
    if horse_gender != "male" and horse_gender != "female":
        print("Invalid input! Please enter 'male' or 'female' only.")
        return

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
        print("Success! boarding requested for 1 Month. Cost: 1500 SAR")
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
        return

    print(f"An invitation has been sent successfully!")


def view_my_horses():
    print("--- View My Horses ---")

    owner_name = input("Enter your name: ")

    for x in horses:
        horse_data = horses[x]

        
        if horse_data["owner_name"].lower() == owner_name.lower():
            print("Horse Name:", horse_data["horse_name"])


def horse_owner_menu():
    while True:
        print("\n=== Horse Owner Menu ===")                      
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
        else:
            print("Invalid choice.")


 # in request_stable_service()  (If I had more time, I would improve this code and add features to it.)
 # in if-elif-else statment  (I enjoyed the if statement concept; writing the conditions was beautiful.)
 # in horse_owner_menu()   ( This part of the code was very challenging for me as I had to search through many data sources.)
