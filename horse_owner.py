def request_stable_service():
    print("--- boarding ---")
    
    owner_name = input("Enter Owner Name: ")
    horse_name = input("Enter Horse Name: ")
    
    print("\nChoose boarding Duration:")
    print("1. 1 Month  (5,000 SAR)")
    print("2. 3 Months (15,000 SAR)")
    print("3. 5 Months (25,000 SAR)")
    print("4. 7 Months (35,000 SAR)")
    print("5. 9 Months (45,000 SAR)")
    print("6. 11 Months (55,000 SAR)")
    print("7. 1 Year/12 Months (50,000 SAR)")
    
    duration_choice = input("Select 1 to 7: ")
    
    if duration_choice == "1":
        print("Success! boarding requested for 1 Month. Cost: 5000 SAR")
    elif duration_choice == "2":
        print("Success! boarding requested for 3 Months. Cost: 15000 SAR")
    elif duration_choice == "3":
        print("Success! boarding requested for 5 Months. Cost: 25000 SAR")
    elif duration_choice == "4":
        print("Success! boarding requested for 7 Months. Cost: 35000 SAR")
    elif duration_choice == "5":
        print("Success! boarding requested for 9 Months. Cost: 45000 SAR")
    elif duration_choice == "6":
        print("Success! boarding requested for 11 Months. Cost: 55000 SAR")
    elif duration_choice == "7":
        print("Success! boarding requested for 1 Year. Cost: 50000 SAR")
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
