from machine import RTC
from time import sleep_ms


"""
Date is a tuple of the form:
(year, month, day, weekday, hours, minute, seconds, subseconds)
weekday and subseconds can be left 0

"""
week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
rtc = RTC()

rtc.datetime((2023, 4, 7, 4, 13, 54, 00, 0)) # set specific date and time. if not specified, 
                                            #then take the real time/date information.
while True:
    date_time = rtc.datetime()
    print(date_time)
    print("Curren date (year, month, day, day of week): ", date_time[0], "/",
                                                           date_time[1], "/",
                                                           date_time[2], "|",
                                                           week_day[date_time[3]])
    print("Current time (hour:minute:second): ",           date_time[4], ":",
                                                           date_time[5], ":",
                                                           date_time[6])
    sleep_ms(1000)