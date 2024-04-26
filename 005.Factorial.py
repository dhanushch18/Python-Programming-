#factorial using loop

n= int(input("Enter a number:"))
f=1;

if(n<1):
    print("factorial does not exist ");
if(n==0):
    print ("Fact is ",1)
if(n>1):
    for i in range(1,n+1):
        f=f*i
print("Factorial is ",f)


#factorial using recursion method

def fact(a):
    if (a==0):
        return 1
    else:
        return (a*fact(a-1))

num=int(input("Enter the number :"))
result=fact(num)
print("Factorial:",result)
