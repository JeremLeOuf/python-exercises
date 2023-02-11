import random
import time
import "Ex8 - RPS.py"

def rematch():
    rematch = input("Rematch? (Y or N)")
    if rematch in ("Y", "y"):
        
    

while True:
    try:
        gamemode = input("Do you want to play against another (P)layer or against (IA) ? ")
        if gamemode in ("p", "i" , "P" , "I" , "IA" , "ia" , "Ia"):
            if gamemode in ("p", "P"):
                print("You're now playing against a second player.")
                p1_choice = input("(R)ock, (P)aper or (S)cissors? ")
                p2_choice = input("(R)ock, (P)aper or (S)cissors? ")
                
                if p1_choice in ("R", "r"):
                    print("P1 chose Rock.")
                    if p2_choice in ("R", "r"):
                        print("P2 chose Rock.")
                        time.sleep(1)
                        print("Draw!")
                        rematch = input("Rematch? (Y or N)")
                        
                        
                    elif p1_choice in ("P", "p"):
                        print("P2 chose Paper.")  
                        time.sleep(1)
                        print("P1 lost! P2 wins.")
                        rematch = input("Rematch? (Y or N)")
                        
                    elif p1_choice in ("S", "s"):
                        print("P2 chose Scissors.")   
                        time.sleep(1)
                        print("P2 lost! P1 wins.")
                        rematch = input("Rematch? (Y or N)")

                    
                if p1_choice in ("P", "p"):
                    print("P1 chose Paper.")
                    if p2_choice in ("R", "r"):
                        print("P2 chose Rock.")
                        time.sleep(1)
                        print("P1 lost! P2 wins.")
                        rematch = input("Rematch? (Y or N)")
                        
                    elif p1_choice in ("P", "p"):
                        print("P2 chose Paper.")  
                        time.sleep(1)
                        print("Draw!")
                        rematch = input("Rematch? (Y or N)")
                        
                    elif p1_choice in ("S", "s"):
                        print("P2 chose Scissors.")   
                        time.sleep(1)
                        print("P1 lost! P2 wins.")
                        rematch = input("Rematch? (Y or N)")  
                    
                if p1_choice in ("S", "s"):
                    print("P1 chose Scissors.")   
                    if p2_choice in ("R", "r"):
                        print("P2 chose Rock.")
                    if p1_choice in ("P", "p"):
                        print("P2 chose Paper.")  
                    if p1_choice in ("S", "s"):
                        print("P2 chose Scissors.")   
                    
                
                
                
                
    
            else:
                print("You're now playing against IA.")
                
                
                
                
                
            break
        else:
            print("Wrong selection!")
    except ValueError:
        print("Wrong selection!")
        
        

