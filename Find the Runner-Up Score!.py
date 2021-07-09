n=int(input())

numbers=map(int,input("Enter: ").split())
print (sorted(set(numbers))[-2])
#set() will convert the iterable list into a set. Set doesn't contain two similar numbers, therefore the second one in the ascending order will the the Runner-Up.