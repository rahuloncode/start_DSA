import math

# 145 =  1-3, 4-3, 5-3

x = int(input("Enter the number \n" ));

num =x ;
result = 0
power = len(str(num))
print(power);

##loops
while num > 0 :
    last = num %10;
    # result = result + math.pow(last, power);
    result =  result + (last ** power)
    num = num // 10;

print(x == result)