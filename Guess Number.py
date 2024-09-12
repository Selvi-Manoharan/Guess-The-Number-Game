import random
def guess_number():
    random_number=random.randint(1,100)
    player_name=input("Enter Your Name: ")
    confirm_play=input("Would you like to start the game? (Enter yes/no): ")
    attempts=0


    while confirm_play.lower()=="yes":
        guess=int(input("Guess any number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please guess any number in the range.")
        elif guess==random_number:
            print("Congratulations ",player_name, 'you won!')
            attempts+=1
            print("It took you ",attempts,"attempts to win this game")
            break
        elif guess > random_number:
            print("HINT: Try smaller number")
            attempts+=1
        elif guess < random_number:
            print("HINT: Try larger number")
            attempts+=1
    else:
        print("Thanks ", player_name, "for your Time.")
guess_number()