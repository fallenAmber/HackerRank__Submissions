# With Function
"""def check(n):
    if n%2==0:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        elif n>20:
            print("Not Wierd")
    else:
        print("Weird")

n=int(input('Enter the number: '))
check(n)"""

#Without Function
n=int(input("Enter the number: "))
if n % 2 == 0:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Wierd")
else:
    print("Weird")

#More Straightforward Approach
"""n=int(input("Enter the number: "))
check={True:"Not Weird", False:"Weird"}

print(check[n%2==0 and n in range (2,6) or n>21])"""
