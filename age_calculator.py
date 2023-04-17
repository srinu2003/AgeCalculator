from datetime import date,datetime
#hehheheee
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
        months = 12 - birthMonth
    else:
        months = 13 - birthMonth

print(months,'months')

#To get days
def remainingdays(birthMonth, birthday):
    months_days = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    return months_days[birthMonth] - birthday
leap_year = CurrentYear/4 == 0
if CurrentDay > birthday:
    days = CurrentDay - birthday
else:
    days = remainingdays(birthMonth,birthday) + CurrentDay + 1 + leap_year
print(days,'days')