import random

user_wins = 0 
computer_wins = 0
winning_score = 3
total_games = 0

while total_games <= 5:
    total_games += 1
    print(f"Player Score: {user_wins} Computer Score: {computer_wins}")

    user_choice = input("rock, paper, scissors ")

    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer_choice = "rock"
    elif rand_num == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    if user_choice == computer_choice:
        print("this round is a tie")
    else:
        if user_choice == "rock":
            if computer_choice == "scissors":
                print("you win this round")
                user_wins += 1
            else:
                print("you lose this round")
                computer_wins += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("you win this round")
                user_wins += 1
            else:
                print("you lose this round")
                computer_wins += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("you win this round")
                user_wins += 1
            else:
                print("you lose this round")
                computer_wins += 1    


    if total_games == 5:
        if user_wins == computer_wins:
            print("you tied")
            break   
        elif user_wins > computer_wins:
            print("you win the game")
            break
        else: 
            print("the computer won the game")
            break

    if user_wins == 3:
        print("you win the game")
        break
    if computer_wins == 3:
        print("the computer won the game")
        break