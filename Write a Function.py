
def is_Leap_year(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False



year=int(input("Enter the year: "))
print(is_Leap_year(year))