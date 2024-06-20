import random

ROCK = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

PAPER = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

SCISSORS = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
'''

hands = ["ROCK", "PAPER", "SCISSORS"]

name = input("WELCOME!!!\nTo start the game enter your name... ")

def open():
    print("\nFirstly, choose the number of games (Best of):\n\tThree\t\t\tFive\t\t\tSeven")
    while True:  # added a while loop to handle invalid inputs
        try:
            num = int(input("Enter the option (3,5,7): "))
            if num not in [3, 5, 7]:
                print("Invalid input. Please enter 3, 5 or 7.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("LET'S STARTTT!!!")
    global score
    score = 0
    for i in range(num):
        opt = random.choice(hands)
        while True:  # added a while loop to handle invalid inputs
            user_opt = input("Choose Rock, Paper or Scissors: ").upper()
            if user_opt not in hands:
                print(f"Valid inputs should only be {hands}")
                continue
            break
        if opt == "ROCK":
            if user_opt == "ROCK":
                print(f"You choose: {ROCK}")
                print(f"The computer choose: {ROCK}")
                print("It is a TIE!")
                score += 0.5
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "PAPER":
                print(f"You choose: {PAPER}")
                print(f"The computer choose: {ROCK}")
                print("YOU WON!!!")
                score += 1
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "SCISSORS":
                print(f"You choose: {SCISSORS}")
                print(f"The computer choose: {ROCK}")
                print("You lost...")
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
        elif opt == "PAPER":
            if user_opt == "ROCK":
                print(f"You choose: {ROCK}")
                print(f"The computer choose: {PAPER}")
                print("You lost...")
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "PAPER":
                print(f"You choose: {PAPER}")
                print(f"The computer choose: {PAPER}")
                print("It is a TIE!")
                score += 0.5
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "SCISSORS":
                print(f"You choose: {SCISSORS}")
                print(f"The computer choose: {PAPER}")
                print("YOU WON!!!")
                score += 1
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
        else:
            if user_opt == "SCISSORS":
                print(f"You choose: {SCISSORS}")
                print(f"The computer choose: {SCISSORS}")
                print("It is a TIE!")
                score += 0.5
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "ROCK":
                print(f"You choose: {ROCK}")
                print(f"The computer choose: {SCISSORS}")
                print("YOU WON!!!")
                score += 1
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
            elif user_opt == "PAPER":
                print(f"You choose: {PAPER}")
                print(f"The computer choose: {SCISSORS}")
                print("You lost...")
                print(f"\t\t\t\t\tYOUR SCORE IS {score}\n\n")
    com_score = num - score
    print(f"Your score {score} VS computer's score {com_score}")
    if score > com_score:
        print("YOU HAVE WON THE MATCH!!!")
    else:
        print("YOU HAVE LOST THE MATCH...")

while True:  # added a while loop to ask the user if they want to play again
    open()
    while True:  # added a while loop to handle invalid inputs
        again = input("Want to play again? (Yes or No)").upper()
        if again not in ["YES", "NO"]:
            print("Invalid input. Please enter Yes or No.")
            continue
        break
    if again == "YES":
        continue
    else:
        print("See you later!")
        break
