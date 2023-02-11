num = int(input('How many numbers to generate? '))


def fibonacci(x):
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    else:      
        fib = [1,1]  
        i = 1
        while i < (num-1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(fibonacci(num))
        