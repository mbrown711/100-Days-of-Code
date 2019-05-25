# After refactor:

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make a move: ")
print("*** NO CHEATING!!\n\n" * 20)
player2 = input("Player 2, make a move: ")

if player1 == player2:
    print("It's a tie")

elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins")
    elif player2 == "paper":
        print("Player 2 wins")

elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Player 2 wins")

elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins")
    elif player2 == "rock":
        print("Player 2 wins")

else:
    print("Something went wrong")

# another portential solution below:

    # p1 = input("Player 1: rock, paper, or scissors ")
    # p2 = input("Player 2: rock, paper, or scissors ")
     
    # if p1 == p2:
    #     print("Draw")
    # elif p1 == "rock" and p2 == "scissors":
    #     print("p1 wins")
    # elif p1 == "paper" and p2 == "rock":
    #     print("p1 wins")
    # elif p1 == "scissors" and p2 == "paper":
    #     print("p1 wins")
    # else:
    #     print("p2 wins")