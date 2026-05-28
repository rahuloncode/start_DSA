x = int(input("Enter the number \n" ));

num = x

result = 0;
while num>0:
    last_digit = num%10;
    result = (result * 10) + last_digit;
    num = num //10;
   

print(x == result)

