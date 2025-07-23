'''DateTime -> Provides classes to handle date and time

from datetime import date, datetime

Get current date:

today = date.today()
print(f"Today is: {today}")

now= datetime.now()
print(f"Now: {today}")

Formatting date as string

formatted_date = today.strftime("%d/%m/%Y , %H:%M:%S")
print(f"Formatted date & time: {formatted_date}")

Calculate days until a future date

futureDate = date(2025, 7, 31)

Days = (futureDate - today).days
print(f"Days until 31st december are: {Days}")

Example program to find the day of the week for your birthday this year

birthday = datetime(2025, 7, 23)
dayOfWeek = birthday.strftime("%A")
print(f"Birthday this year is on : {dayOfWeek}")

import time  #Offer time relevant operations

get current time

currtime = time.time()

print(currtime)

Sleep for 2 seconds


print("Sleep for 5 seconds....")
time.sleep(5)
print(("Awake!!!"))

Format current time
times= time.strftime("%H:%M:%S")
print(f"Current time: {times}")


Example program to create a countdown from 10 to 0

for i in range(10, -1,-1):
    print(i)
    time.sleep(1)
    
print("Done!")
'''