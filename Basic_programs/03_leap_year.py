def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def check_leap_year():
    year = int(input("Enter a year to check "))
    while year < 1000 or year > 9999:
        print("Year must be a 4 digit number.")
        year = int(input("Enter a year to check "))
    
    if leap_year(year):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")

check_leap_year()
