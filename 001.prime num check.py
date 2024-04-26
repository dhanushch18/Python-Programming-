#prime no.

num=int(input("Enter the number:"));

if(num==1):
    print("It is not a prime number");
if num > 1:
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number");
            break
    else:
        print("It is a prime number")



#function method

def prime(n):

  if n<=1:
    print("not prime");
  if(n>1):
    for i in range (2,n):
      if n%i==0:
        print("not prime");
        break
   else:
    print("prime num");

n=int(input)


#ai math method

import math

def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Enter the number: "))
    if is_prime(num):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()
