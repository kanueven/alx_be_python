from datetime import datetime, timedelta
def  display_current_datetime ():
    current_datetime = datetime.now()
    format_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time :", format_datetime)
    return current_datetime


def calculate_future_date (current_datetime,days):
    future_date = current_datetime + timedelta(days = number_of_days)
    #Calculate what the date will be after adding the specified number of days to the current date.
    format_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days} days : {format_future_date}")

#here is the main program
current_date = display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date:"))
calculate_future_date(current_date, number_of_days)