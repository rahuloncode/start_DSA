# Factorial with Recursion

def factorial( sum ,n):
    if n ==1 :
        print(sum)
        return 
    print(sum)
    factorial(sum*n, n-1)


factorial(0,5)