horses = {
    1: {"owner_name": "Turki", "horse_name": "Wadah", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 100, "health_score": 100},
    2: {"owner_name": "Turki", "horse_name": "Shamekh", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 97, "health_score": 95},
    3: {"owner_name": "Turki", "horse_name": "Alskb", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 94, "health_score": 92},
    4: {"owner_name": "Turki", "horse_name": "Abiah.t", "age": 7, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 98},
    5: {"owner_name": "Turki", "horse_name": "Seham", "age": 5, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 91, "health_score": 93},
    6: {"owner_name": "Turki", "horse_name": "Rahaf", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 95, "health_score": 96},
    7: {"owner_name": "Turki", "horse_name": "Kehelan", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 90, "health_score": 89},
    8: {"owner_name": "Turki", "horse_name": "shujaa", "age": 8, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 99, "health_score": 99},
    9: {"owner_name": "Turki", "horse_name": "Borkan", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 93, "health_score": 94},
    10: {"owner_name": "Turki", "horse_name": "Raad", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 92, "health_score": 90},
    11: {"owner_name": "Turki", "horse_name": "Barq", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 98, "health_score": 99},
    12: {"owner_name": "Turki", "horse_name": "Asael", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 95},
    13: {"owner_name": "Nawaf", "horse_name": "Mazyon", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 88, "health_score": 84},
    14: {"owner_name": "Abdulaziz", "horse_name": "alshqh", "age": 4, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 85, "health_score": 87},
    15: {"owner_name": "Nawaf.z", "horse_name": "gzar", "age": 6, "gender": "male", "breed": "thoroughbred", "status": "boarding", "horse_level": 90, "health_score": 91},
    16: {"owner_name": "Abdullah", "horse_name": "nomas", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    17: {"owner_name": "Khulod", "horse_name": "Najm", "age": 7, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    18: {"owner_name": "Abulaziz", "horse_name": "abiah", "age": 4, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 84, "health_score": 90},
    19: {"owner_name": "Nawaf", "horse_name": "Anood", "age": 5, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 87, "health_score": 85},
    20: {"owner_name": "Nawaf.z", "horse_name": "Shadad", "age": 6, "gender": "male", "breed": "thoroughbred", "status": "boarding", "horse_level": 91, "health_score": 89}
}

trainees = {
    1: {"trainee_name": "Turki", "age": 24, "training_type": "Jumping, For fun,", "experience_level": "Advanced", "assigned_horse": "Wadah", "sessions_completed": 70, "performance_score": 99},
    2: {"trainee_name": "Abdulaziz", "age": 24, "training_type": "Jumping", "experience_level": "Intermediate", "assigned_horse": "Shamekh", "sessions_completed": 46, "performance_score": 90},
    3: {"trainee_name": "Nawaf.z", "age": 24, "training_type": "For fun", "experience_level": "Beginner", "assigned_horse": "Alskb", "sessions_completed": 12, "performance_score": 70},
    4: {"trainee_name": "Nawaf", "age": 24, "training_type": "Racing", "experience_level": "Advanced", "assigned_horse": "Barq", "sessions_completed": 50, "performance_score": 97},
    5: {"trainee_name": "Khalid", "age": 22, "training_type": "Racing", "experience_level": "Intermediate", "assigned_horse": "Raad", "sessions_completed": 30, "performance_score": 84},
    6: {"trainee_name": "Saud", "age": 20, "training_type": "For fun", "experience_level": "Beginner", "assigned_horse": "Rahaf", "sessions_completed": 10, "performance_score": 68},
    7: {"trainee_name": "Abdullah", "age": 24, "training_type": "Jumping", "experience_level": "Intermediate", "assigned_horse": "Seham", "sessions_completed": 22, "performance_score": 80},
    8: {"trainee_name": "Mohammed", "age": 26, "training_type": "For fun", "experience_level": "Advanced", "assigned_horse": "Kehelan", "sessions_completed": 40, "performance_score": 92}
}


def main_menu():
  while:
    print("===== Horse Stable System =====")
    print("1.Admin")
    print("2.Trainees")
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
