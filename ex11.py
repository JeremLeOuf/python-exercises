while True:
    try:
        num = int(input('Choose a number: '))
        break
    except Exception:
        print('Enter numerical value!')
        continue
    
def checkIfPrime(num):
    if num == 2:
        return "Number is prime!"
    elif num > 1:
        for x in range(2, num):
            return "Number is not prime!" if num % x == 0 else "Number is prime!"
    else:
        return "Number is not prime"

    
print(checkIfPrime(num))