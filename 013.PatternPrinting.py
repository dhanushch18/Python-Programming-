#for loop
1
12
123
1234
12345

num=int(input("Enter the no. of rows:"))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
   print()



1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 


n=int(input("Enter the no. of rows:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#for loop

* 
* * 
* * * 
* * * * 
* * * * *

n=int(input("Enter the no. of rows:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


*
**
***
****
  
#while loop

n=int(input())
i=1
while i<=n:
  j=1
  while(j<=i):
    print("*",end="")
    j=j+1
  print()
  i=i+1



1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


n=int(input("Enter the no. of rows:"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
