
Enter the num:6
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 



#pyramid pattern
n=int(input("Enter the num:"))
i=1

while i<=n:
    k=1
    while k<=n-i:
        print("",end=" ")
        k=k+1
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
