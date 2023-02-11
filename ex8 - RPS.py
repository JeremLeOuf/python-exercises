import random
import time

print("Welcome to PyRPS Game! Designed by JeremLeOuf during his bored working hours.")
time.sleep(1)

def rematch():
    while True:
        rematch = input("Rematch? (Y or N) ").lower()
        if rematch == "y":
            RPSgame()
        elif rematch == "n":
            print("Thanks for playing! Exiting.")
            exit()
        else: 
            print("Wrong input!")
        
def gamemodeChoice():
    while True:
        try:
            gamemode = input("Do you want to play against another (P)layer or against (IA) ? ").lower()
        except ValueError:
            print("Wrong selection!")
        return gamemode
            
def RPSgame():
    gamemode = gamemodeChoice()   
    if gamemode == 'p':
                print("You're now playing against a second player.")
                p1_choice = input("P1: (R)ock, (P)aper or (S)cissors? ").lower() 
                p2_choice = input("P2: (R)ock, (P)aper or (S)cissors? ").lower()
                
                if p1_choice == "r" and p2_choice == "r":
                    result("P1 chose Rock.", "P2 chose Rock.", "Draw!")
                elif p1_choice == "r" and p2_choice == 'p':
                    result("P1 chose Rock.", "P2 chose Paper.", "P2 wins!")
                elif p1_choice == "r" and p2_choice == 's':
                    result("P1 chose Rock.", "P2 chose Scissors.", "P1 wins!")
                elif p1_choice == 'p' and p2_choice == 'r':
                    result("P1 chose Paper.", "P2 chose Rock.", "P2 wins!")
                elif p1_choice == 'p' and p2_choice == 'p':
                    result("P1 chose Paper.", "P2 chose Paper.", "Draw!")
                elif p1_choice == 'p' and p2_choice == 's':
                    result("P1 chose Paper.", "P2 chose Scissors.", "P2 wins!")
                elif p1_choice == 's' and p2_choice == 'r':
                    result("P1 chose Scissors.", "P2 chose Rock.", "P1 lost! P2 wins.")
                elif p1_choice == 's' and p2_choice == 'p':
                    result("P1 chose Scissors.", "P2 chose Paper.", "P2 lost! P1 wins.")
                elif p1_choice == 's' and p2_choice == 's':
                    result("P1 chose Scissors.", "P2 chose Scissors.", "Draw!")
                else: 
                    print("Wrong input!")
                    RPSgame()

    elif gamemode == 'i':
        print("You're now playing against IA.")
        outcomes = ["R", "P", "S"]
        AI_choice = random.choice(outcomes)
        player_choice = input("Your choice: (R)ock, (P)aper or (S)cissors? ")
        if player_choice == 'r':
            if AI_choice == "R":
                result("You chose Rock.", "AI chose Rock.", "Draw!")
            elif AI_choice == "P":
                result("You chose Rock.", "AI chose Paper.", "You lost!")
            elif AI_choice == "S":
                result("You chose Rock.", "AI chose Scissors.", "You won!")
        elif player_choice == 'p':
            if AI_choice == "R":
                result("You chose Paper.","AI chose Rock.", "You won!")
            elif AI_choice == "P":
                result("You chose Paper.","AI chose Paper.", "Draw!")
            else:
                result("You chose Paper.","AI chose Scissors.", "You lost!")
        elif player_choice == 's':
            if AI_choice == "R":
                result("You chose Scissors.","AI chose Rock.", "You lost!")
            elif AI_choice == "P":
                result("You chose Scissors.","AI chose Paper.", "You won!")
            else:
                result("You chose Scissors.","AI chose Scissors.", "Draw!")
        else: 
            print("Wrong player input!")
            rematch()
            
    else: 
        print("Wrong gamemode choice!")
        RPSgame()

def result(arg0, arg1, arg2):
    print(arg0)
    time.sleep(1)
    print(arg1)
    time.sleep(1)
    print(arg2)
    rematch()
           
RPSgame()