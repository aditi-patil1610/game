import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n" + "rock vs paper -> Paper wins \n" + "rock vs scissors -> rock wins \n" + "Paper vs scissors -> scissors wins \n" )
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3- scissors \n")

    choice = int(input("Enter your choice: "))
 
    while choice > 3 or choice < 1 :
     choice = int(input('Enter a valid choice please :'))
    if choice == 1:
     choice_name = 'Rock'
    elif choice == 2:
     choice_name = 'Paper'
    else:
     choice_name ='Scissors'

    print('User choice is:', choice_name)
    print("Noe it's Computer 's Turn...")

    comp_choice = random.randint(1,3)
 
    if comp_choice == 1:
     comp_choice_name = 'rock'
    elif comp_choice == 2:
     comp_choice_name = 'Paper'
    else:
     comp_choice_name = 'Scissors'

    print("Computer choice is :", comp_choice_name )
    print(choice_name, 'vs',comp_choice_name)

    if choice == comp_choice:
     result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
     result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
     result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
     result = 'Scissors'
   
    if result == "DRAW":
     print("<== It's Tie! ==>")
    elif result == choice_name:
     print("<== User wins! ==>")
    else:
     print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    ans =  input().lower()
    if ans =='n':
     break;
 
print("Thank for playing!")