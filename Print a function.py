
n=int(input())
for i in range(1,n+1):
    print (i,end='')

"""By default python’s print() function ends with a newline.
Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character. You can end a print statement with any character/string using this parameter.
"""

print(*range(1, int(input())+1), sep='')
# * is passing an  entire list