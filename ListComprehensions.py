x, y, z, n = map(int,input("Enter the numbers: ").split(" "))
print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)  ])

#Following loops will explain how the list comprehension actually works
"""
l= []
for a in range(x):
    for b in range(y):
        for c in range(z):
            if a+b+c!= n:
                l.append([a,b,c])
print(l)
"""