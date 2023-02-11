import random
from random_word import RandomWords

def main():
    strength = input('How strong do you want your password to be? ((W)eak or (S)trong) ')
    
    if strength.lower() in('weak','w'): 
        r = RandomWords()
        num = random.randint(0,9)
        mylist = [(r.get_random_word()).capitalize() for _ in range(2)]
        password = f'{mylist[0]}{num}{mylist[-1]}'
        print(password)
           
    elif strength.lower() in ('strong','s'):
        symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-"]
        uppercase_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        lowercase_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        length = random.randint(14,36)
        pwdlist = []
        for _ in range(length):
            char = random.choice([symbol_list,uppercase_list,lowercase_list])
            pwdchar = random.choice(char)
            pwdlist.append(pwdchar)
        password = ''.join(pwdlist)
        print(password)
            
    else:
        print('Wrong input! Only use the ones allowed. Exiting.')
        
        
if __name__ == "__main__":
    main()