"""
Topic: Python Modules - datetime and time
Covers:
- Handling current date and time
- Formatting dates
- Calculating date differences
- Countdown using time.sleep()
"""

from datetime import date, datetime
import time

# Get current date
today = date.today()
print(f"Today's date: {today}")

# Get current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Format current date and time as string
formatted_date = now.strftime("%d/%m/%Y , %H:%M:%S")
print(f"Formatted date and time: {formatted_date}")

# Calculate days until a specific future date
future_date = date(2025, 7, 31)
days_remaining = (future_date - today).days
print(f"Days until 31st July 2025: {days_remaining}")

# Determine day of the week for a birthday
birthday = datetime(2025, 7, 23)
day_of_week = birthday.strftime("%A")
print(f"Birthday in 2025 falls on: {day_of_week}")

# Get current timestamp
current_timestamp = time.time()
print(f"Current Unix timestamp: {current_timestamp}")

# Demonstrate sleep function
print("Sleeping for 5 seconds...")
time.sleep(5)
print("Awake now.")

# Get current formatted time
current_time = time.strftime("%H:%M:%S")
print(f"Current time: {current_time}")

# Countdown from 10 to 0
print("Countdown:")
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Done!")
