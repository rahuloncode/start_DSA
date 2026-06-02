# Recursion with Parameter

def raja(x, n):
    if n == 0:
        return
    print(x)            #-- Head Recusion  as Job perform first then fucntion called
    raja(x ,  n-1);

raja(15,3);


# Parameteriszed and Fucntional Recursions

    # sum iof 1 - n 

def Sumarize (sum, i, n):
    if i> n:
        print(sum);
        return;
    Sumarize(sum + i, i+1, n)


Sumarize(0, 1, 4)