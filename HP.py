horses = {
    1: {"owner_name": "Turki", "horse_name": "Wadah", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 100, "health_score": 100},
    2: {"owner_name": "Turki", "horse_name": "Shahin", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 97, "health_score": 95},
    3: {"owner_name": "Turki", "horse_name": "Rayan", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 94, "health_score": 92},
    4: {"owner_name": "Turki", "horse_name": "Barq", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 98},
    5: {"owner_name": "Turki", "horse_name": "Saqr", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 91, "health_score": 93},
    6: {"owner_name": "Turki", "horse_name": "Hattan", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 95, "health_score": 96},
    7: {"owner_name": "Turki", "horse_name": "Nawaf", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 90, "health_score": 89},
    8: {"owner_name": "Turki", "horse_name": "Shibl", "age": 8, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 99, "health_score": 97},
    9: {"owner_name": "Turki", "horse_name": "Aseel", "age": 5, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 93, "health_score": 94},
    10: {"owner_name": "Turki", "horse_name": "Ghazal", "age": 4, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 92, "health_score": 90},
    11: {"owner_name": "Turki", "horse_name": "Fares", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 98, "health_score": 99},
    12: {"owner_name": "Turki", "horse_name": "Shamikh", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 95},
    13: {"owner_name": "Nawaf", "horse_name": "Mazyon", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 88, "health_score": 84},
    14: {"owner_name": "Khalid", "horse_name": "Saif", "age": 4, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 85, "health_score": 87},
    15: {"owner_name": "Fahad", "horse_name": "Qanoon", "age": 6, "gender": "male", "breed": "thoroughbred", "status": "boarding", "horse_level": 90, "health_score": 91},
    16: {"owner_name": "Abdullah", "horse_name": "Raed", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 82, "health_score": 86},
    17: {"owner_name": "Mohammed", "horse_name": "Najm", "age": 7, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 89, "health_score": 88},
    18: {"owner_name": "Saud", "horse_name": "Deem", "age": 4, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 84, "health_score": 90},
    19: {"owner_name": "Yazeed", "horse_name": "Anood", "age": 5, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 87, "health_score": 85},
    20: {"owner_name": "Ahmed", "horse_name": "Shadad", "age": 6, "gender": "male", "breed": "thoroughbred", "status": "boarding", "horse_level": 91, "health_score": 89}
}

trainee = {
    1:{}
    2:{}
    3:{}
    4:{}
    5:{}
    6:{}
    7:{}
    8:{}
}


def main_menu():
  while:
    print("===== Horse Stable System =====")
    print("1.Admin")
    print("2.Trainee")
    print("3.Horse Owner ")
    print("4.Exit")
    
    choice = int(input("Choose your role: "))

    if choice == 1 :
      admin_menu()
    elif choice == 2 :
      trainee_menu()
    elif choice == 3 :
      horse_owner_menu()
    elif choice == 4 :
      break
    else:
      print("Invalid input!!")

#nawaf zakri admin




#abdulaziz alshebl trainee



#turki abu haimed horse managmet



