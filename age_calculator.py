from datetime import date,datetime

# date object of today's date
today = date.today() 

CurrentYear = today.year
CurrentMonth = today.month
CurrentDay = today.day
print(f"Today's date:{CurrentDay}/{CurrentMonth}/{CurrentYear}")
dateOfBirth = input("Enter your Date of birth[dd-mm-yyyy]: ")
birthday, birthMonth, birthYear = list(map(int,dateOfBirth.split('-')))
dateOfBirth = date(birthYear,birthMonth,birthday)
print("Your Date of birth is:",dateOfBirth.strftime("%d %B, %Y"))
date_check = ((today.month, today.day) < (birthMonth, birthday)) 
#To get years
years = CurrentYear - birthYear - date_check
print(years,'years')
#To get months
if CurrentMonth > birthMonth:
    months = CurrentMonth - birthMonth
else:
    if CurrentDay < birthday:
        months = CurrentMonth - 1
    else:
        months = CurrentMonth

print(months,'months')

#To get days
