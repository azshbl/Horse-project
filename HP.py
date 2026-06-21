horses = {
    1:{"owner_name" : "Nawaf" ,"horse_name ": "Ali" ,"age":4  ,  "ginder" : "male"  , "breed" : "" , "status" : ""}
    2:{"owner_name":"Turki" ,"horse_name ": "alking" ," age ": 6 , "ginder" : "female" , "breed" : "" , "status" : }
    3:{}
    4:{}
    5:{}
    6:{}
    7:{}
    8:{}
    9:{}
    10:{}
    11:{}
    12:{}
    13:{}
    14:{}
    15:{}
    16:{}
    17:{}
    18:{}
    19:{}
    20:{}
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
stable_orders = []

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




