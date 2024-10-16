#activity 3

choice = input("select if u want the bike or car:")
if choice == 'bike' or choice == 'BIKE':
    bike_choice = input("select Yamaha or M1Cycle")
    if bike_choice == 'Yamaha' or bike_choice == 'yamaha' or bike_choice == 'YAMAHA'or bike_choice == 'm1cycle':
        print("you have selected yamaha :)")
    else:
        print("you have selected M1Cycle")
elif choice == 'car' or choice == 'CAR':
    car_choice = input("select McLaren or Ferrari")
    if car_choice == 'Mclaren' or car_choice == "mclaren" or car_choice == 'MCLAREN' or car_choice == 'ferrari':
        print("you have selected MClaren")
    else:
        print("you have selected Ferrari")