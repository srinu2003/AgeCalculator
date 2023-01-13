from datetime import date#,datetime
#dictionary months
'''
def leap(year):
    year=12
    pass
month={
    January : 31,
    February : 29 if leap(year) else 28,
    March : 31,
    April : 30, 
    May : 31, 
    June : 30, 
    July : 31, 
    August : 31, 
    September : 30, 
    October : 31,
    November : 30, 
    December : 31,
}'''
# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
print(today)
print("Simple Age Calculator")

# asking user to enter birth year, birth month, and birth date
birthYear = int(input("Enter the birth year: "))
birthMonth = int(input("Enter the birth month: "))
birthDay = int(input("Enter the birth day: "))

# converting integer values to date format using the date() method
dateOfBirth = date(birthYear, birthMonth, birthDay)  
# dob = datetime.date(int(input("Enter year:")),int(input( "Enter month:")), int(input("Enter date:")))
print("Your Date of birth is:",dateOfBirth.strftime("%d %B, %Y"))

# a bool representing if today's day, or month precedes the birth day, or month
day_check = ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))

# calculating the difference between the current year and birth year
year_diff  = today.year - dateOfBirth.year

age_in_years = year_diff - day_check  

# calculating the remaining months
remaining_months = abs(today.month - dateOfBirth.month)

# calculating the remaining days
remaining_days = abs(today.day - dateOfBirth.day)

# printing the age for the users  
print("Age:", age_in_years, "Years", remaining_months, "Months and", remaining_days, "days")