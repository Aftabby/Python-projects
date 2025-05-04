#Word hangman
import random

def select_a_word():
    words = ["Sunday", "Monday", "Tuesday", "Wednesday", "Saturday", "Friday"]
    index = random.randint(0, len(words) - 1)
    day = words[index]
    return day

def day_game():
    day = select_a_word()
    first_letter = 1
    min_try = 3

    while min_try > 0:
        for i in range(first_letter):
            print(day[i], end='')

        for i in range(first_letter, len(day)):
            print("_", end='')

        print("\nGuess the word:\n")

        guessed = input()

        if guessed == day:
            print("Congrats! You have guessed the right word.\n")
            break
        else:
            for i in range(len(guessed)):
                if day[i] == guessed[i]:
                    first_letter = i+1
                else:
                    break
            
            min_try -= 1
            print(f"Bad luck! Tries left: {min_try}")

            if min_try == 0:
                print("Game Over!\n")
    
    return 


day_game()


















#Rock paper scissor
def check_winner(p1, p2):
    condition = ["rock", "paper", "scissor"]

    if p1 not in condition or p2 not in condition:
        return "Enter the correct value"

    if p1 == p2:
        return "draw"
    
    if p1 == "rock":
        if p2 == "paper":
            return "Player 2 won"
        else:
            return "Player 1 won" #when p1 = rock, p2 = scissor
    
    if p1 == "paper":
        if p2 == "rock":
            return "Player 1 won"
        else:
            return "Player 2 won"  #when p1 = paper, p2 = scissor
    
    if p1 == "scissor":
        if p2 == "rock":
            return "Player 2 won"
        else:
            return "Player 1 won" #when p1 = scissor, p2 = paper


player1 = input("Player 1 : Enter rock, paper or scissor \n")
player2 = input("Player 2 : Enter rock, paper or scissor \n")

print(check_winner(player1, player2), "\n\n")









#Guess Game
import random

def guess_game():
    score = 0
    print("Game Rules:\nIf you guess the right number (1-5) you will get 5 points, \nOne wrong guess and the score will be deducted by one.\nEnter 'q' to quit the game.")
    while True:
        random_num = random.randint(1, 5)
        guess = input("\n\nEnter any number between 1 to 5:\n")

        if guess == 'q' or guess == 'Q':
            print("Thanks for playing the game.\n")
            break
        elif random_num == int(guess):
            score += 5
            print(f"You guessed the right number!!!\n The right number is {guess}.\nYour new score is = {score}\n\n")
        else:
            if score > 0:
                score -= 1
            print(f"Sad!!! You guess was not right, the actual number is {random_num}\nYour score is ", score, "\n")


guess_game()






#Queries:
# what is print(f"") --- an f inside the parenthesis of print function
# Know about the keyword---- is --

#Important Notes:
# You can also run a statement like --- if variable_name is True: ----- the keyword -- is -- 