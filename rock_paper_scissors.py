import random




# Functions
def computer_game():
    player_Move = input("Select rock, paper or scissors: ")
    computer_Move = random.choice(choices)
    player_Count = 0
    computer_Count = 0
    # Rock Checks
    if player_Move == "rock" and computer_Move == "rock":
        print("Tie.")
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "rock" and computer_Move == "paper":
        print("The computer won.")
        computer_Count = computer_Count + 1
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "rock" and computer_Move == "scissors":
        print("The player won.")
        player_Count = player_Count + 1
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()


    # Paper Checks
    if player_Move == "paper" and computer_Move == "rock":
        print("The player won.")
        player_Count = player_Count + 1
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "paper" and computer_Move == "paper":
        print("Tie.")
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "paper" and computer_Move == "scissors":
        print("The computer won.")
        computer_Count = computer_Count + 1
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()


    # Scissor checks
    if player_Move == "scissors" and computer_Move == "rock":
        print("The computer won.")
        computer_Count = computer_Count + 1
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "scissors" and computer_Move == "paper":
        print("The player won.")
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()
    if player_Move == "scissors" and computer_Move == "scissors":
        print("Tie.")
        print("The current score is " + str(player_Count) + "-" + str(computer_Count))
        computer_game()



def player_Game():
    player_1_move = input("Player 1, select rock, paper or scissors: ")
    player_2_move = input("Player 2, select rock, paper or scissors: ")
    player_1_count = 0
    player_2_count = 0
    # Rock Checks

    if player_1_move == "rock" and player_2_move == "rock":
        print("Tie.")
        print("The current score is " + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    if player_1_move == "rock" and player_2_move == "paper":
        print("Player 2 wins.")
        player_2_count = player_2_count + 1
        print("The current score is " + str(player_1_count) + "-" + str(player_1_count))
        player_Game()
    if player_1_move == "rock" and player_2_move == "scissors":
        print("Player 2 wins.")
        player_2_count = player_2_count + 1
        print("The current score is " + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    
    # Paper Checks

    if player_1_move == "paper" and player_2_move == "rock":
        print("Player 1 wins.")
        player_1_count + player_1_count
        print("The current score is " + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    if player_1_move == "paper" and player_2_move == "paper":
        print("Tie.")
        print("The current score is " + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    if player_1_move == "paper" and player_2_move == "rock":
        print("Player 1 wins.")
        player_1_count = player_1_count + 1
        print("The current score is" + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    # Scissor checks

    if player_1_move == "scissors" and player_2_move == "rock":
        print("Player 2 wins.")
        player_2_count = player_2_count + 1
        print("The current score is" + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    if player_1_move == "scissors" and player_2_move == "paper":
        print("Player 1 wins.")
        player_1_count  = player_1_count + 1
        print("The current score is" + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
    if player_1_move == "scissors" and player_2_move == "scissors":
        print("Tie.")
        print("The current score is" + str(player_1_count) + "-" + str(player_2_count))
        player_Game()
# Start Game






print("Rock Paper Scissors | Python Edition")

choices = ["rock" , "paper", "scissors"]
type_game = input("Would you like to play against computer or player? (C or P)")
if type_game == ["C", "c"]:
    computer_game()
if type_game == ["P", "p"]:
    player_Game()

