# num  ="haary"
num = [1,2,3,4,5,6,7]

# By reverse method

# num.reverse()
# print(num)

# by slicing method

# print(num[::-1])

# recursion se karna hai

# def my_function(num, newAr =[],i =0, ):
#     length =  len(num);
#     if i<0:
#         return newAr;
#     newAr.append(num[length-1 -i]);
#     my_function(newAr, i+1)

def my_function(num, newAr, i=0):
    length = len(num)

    if i == length:
        return newAr

    newAr.append(num[length - 1 - i])

    return my_function(num, newAr, i + 1)


num = [1, 2, 3, 4, 5]
print(my_function(num, []))