horses = {
    1: {"owner_name": "Turki", "horse_name": "Wadah", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 100, "health_score": 100},
    2: {"owner_name": "Turki", "horse_name": "Shamekh", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 97, "health_score": 95},
    3: {"owner_name": "Turki", "horse_name": "Alskb", "age": 7, "gender": "male", "breed": "frezian", "status": "stable", "horse_level": 94, "health_score": 92},
    4: {"owner_name": "Turki", "horse_name": "Abiah.t", "age": 7, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 98},
    5: {"owner_name": "Turki", "horse_name": "Seham", "age": 5, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 91, "health_score": 93},
    6: {"owner_name": "Turki", "horse_name": "Rahaf", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 72, "health_score": 96},
    7: {"owner_name": "Turki", "horse_name": "Kehelan", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 72, "health_score": 89},
    8: {"owner_name": "Turki", "horse_name": "shujaa", "age": 8, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 99, "health_score": 99},
    9: {"owner_name": "Turki", "horse_name": "Borkan", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 93, "health_score": 94},
    10: {"owner_name": "Turki", "horse_name": "Raad", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 92, "health_score": 90},
    11: {"owner_name": "Turki", "horse_name": "Barq", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 75, "health_score": 99},
    12: {"owner_name": "Turki", "horse_name": "Asael", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 77, "health_score": 95},
    13: {"owner_name": "Nawaf", "horse_name": "Mazyon", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 88, "health_score": 84},
    14: {"owner_name": "Abdulaziz", "horse_name": "alshqh", "age": 4, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 85, "health_score": 87},
    15: {"owner_name": "Nawaf.z", "horse_name": "gzar", "age": 6, "gender": "male", "breed": "frezian", "status": "boarding", "horse_level": 89, "health_score": 91},
    16: {"owner_name": "Abdullah", "horse_name": "nomas", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    17: {"owner_name": "Khulod", "horse_name": "Najm", "age": 7, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    18: {"owner_name": "Abdulaziz", "horse_name": "abiah", "age": 4, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 74, "health_score": 90},
    19: {"owner_name": "Nawaf", "horse_name": "Anood", "age": 5, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 70, "health_score": 85},
    20: {"owner_name": "Nawaf.z", "horse_name": "Shadad", "age": 6, "gender": "male", "breed": "frezian", "status": "boarding", "horse_level": 65, "health_score": 89}
}


trainers = {
    1: {"trainer_name": "Turki", "age": 24, "training_type": "Jumping, For fun,", "experience_level": "Advanced", "sessions_completed": 70, "performance_score": 99},
    2: {"trainer_name": "Abdulaziz", "age": 24, "training_type": "Jumping", "experience_level": "Intermediate", "sessions_completed": 56, "performance_score": 95},
    3: {"trainer_name": "Nawaf.z", "age": 24, "training_type": "For fun", "experience_level": "Beginner", "sessions_completed": 20, "performance_score": 95},
    4: {"trainer_name": "Nawaf", "age": 24, "training_type": "Racing", "experience_level": "Advanced", "sessions_completed": 50, "performance_score": 90},
    5: {"trainer_name": "Khalid", "age": 22, "training_type": "Racing", "experience_level": "Intermediate", "sessions_completed": 30, "performance_score": 85},
    6: {"trainer_name": "Saud", "age": 20, "training_type": "For fun", "experience_level": "Beginner", "sessions_completed": 10, "performance_score": 80},
    7: {"trainer_name": "Abdullah", "age": 24, "training_type": "Jumping", "experience_level": "Intermediate", "sessions_completed": 22, "performance_score": 75},
    8: {"trainer_name": "Mohammed", "age": 26, "training_type": "For fun", "experience_level": "Advanced", "sessions_completed": 40, "performance_score": 70}


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
"""
trainee = {
    
           name
           age
           when do you want the class
           what type do want(jumping,for fun,racing)
           how many hours have you trained(1,20,3,30)
           what package do you want(1,,10,20,40)
                      
           40 class 
           after you finish 40 classes  


           Jumping
           90

           hourse level 100
           trainer performance 99
           trainers hours completed 98

}
"""


#turki abu haimed horse managmet
