from datetime import date#,datetime

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
# dob = datetime.date(int(input("Enter year:")),int(input( "Enter month:")), int(input("Enter date:")))
dob = date(2020,10,1)
print(dob)
print("Your birthday is on:",dob.strftime("%B %d, %Y"))
# get the current date and time
age = today  - dob 
print(today)
print(age)


