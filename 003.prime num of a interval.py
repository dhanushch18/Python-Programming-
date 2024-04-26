#print prime num of a limit

n1=int(input("Enter the first limit:"))
n2=int(input("Enter the second limit:"))

for num in range(n1,n2 +1):
    if num>1:
        for i in range (2,num):
            if num%i == 0:
                break

        else:
            print(n
