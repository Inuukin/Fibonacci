#!/usr/bin/env python

## Fibonacci

number1 = input("Enter a number that represents a lower range of Fibonacci sequence: ")
number2 = input("Enter a number that represents a upper range of Fibonacci sequence: ")

## generate fibonacci for 250 numbers
table = [-1 for _ in range(250)]
 
def fibonacci(n):
    if n == 0:
        table[0] = 0
        return 0
    if n == 1:
        table[0] = 0
        table[1] = 1
        return 1
    if table[n] != -1:
        return table[n]
    table[n] = fibonacci(n-1) + fibonacci(n-2)
    return table[n]


## check if input is numeric:
if number1.lstrip('-').isnumeric() and number2.lstrip('-').isnumeric():
    ## define variables as integers:
    n = int(number1)
    m = int(number2)
    ## check if input is in range:
    if (1 <= n <= 250) and (1 <= m <= 250):
        if (n < m):
            ## print Fibonacci for a given range (including upper value)
            for i in range(n,m+1):
                print(fibonacci(i))            
        else:
            print("Second number must be higher than the first one")
    elif (1 > n < 250):
        print("First number is out of range")
    else:
        print("Second number is out of range")
elif number2.lstrip('-').isnumeric():
    print("First number is not numeric")
elif number1.lstrip('-').isnumeric():
    print("Second number is not numeric")
else:
    print("Input is not numeric")

