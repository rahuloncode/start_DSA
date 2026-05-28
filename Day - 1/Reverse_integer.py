x = int(input("Enter the number \n" ));


while x > 0:
    last_digit = x % 10 ;
    print(last_digit, end="");
    x= x//10;