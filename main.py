print("Welcome to the fruit game! Chose your fruit and start to find it.")
print('''
  __            _ _   
 / _|          (_) |  
| |_ _ __ _   _ _| |_  
|  _| '__| | | | | __|   G A M E
| | | |  | |_| | | |_  
|_| |_|   \__,_|_|\__|
''')
print("---------------------------------")
print("Apple | Pear | Banana | Pineapple")
print("---------------------------------")

fruit_choice = input("Type the fruit you want: ")

number_choice = int(input("You are in a big kitchen with ten drawers. Your fruit is hidden in one of them. Type a number between 1 and 10: "))

if (number_choice == 1):
    if (fruit_choice == "Pineapple"):
        print("Congratulations !!!")
    else:
        print("It's not your fruit, game over !")

elif (number_choice == 3):
    if (fruit_choice == "Apple"):
        print("Congratulations !!!")
    else:
        print("It's not your fruit, game over !")

elif (number_choice == 5):
    if (fruit_choice == "Pear"):
        print("Congratulations !!!")
    else:
        print("It's not your fruit, game over !")

elif (number_choice == 7):
    if (fruit_choice == "Banana"):
        print("Congratulations !!!")
    else:
        print("It's not your fruit, game over !")

else:
    print("Game over !")
    
