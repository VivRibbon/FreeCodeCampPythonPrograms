# Time Calculator
# By Moira Campbell

def add_time(start, duration, day=None):
    start_time = ""
    time_add = ""
    start_hours = ""
    start_minutes = ""
    hours_total = ""
    minutes_total = ""
    minutes_quotient = ""
    hours_quotient = ""
    PM_status = ""
    day_index = ""
    result = ""

    start = start.split(":")
    start += start[1].split()
    start.pop(1)

    duration = duration.split(":")

    if start[2].casefold() == "pm" or "p.m.":
        PM_status = True
    elif start[2].casefold() == "am" or "a.m.":
        PM_status = False

    hours_total = int(start[0]) + int(duration[0])
    minutes_total = int(start[1]) + int(duration[1])


    if minutes_total > 60:
       minutes_quotient = minutes_total // 60
       hours_total += minutes_quotient
       minutes_total = minutes_total - (minutes_quotient * 60)

    if PM_status == True:
        hours_total += 12

    if hours_total > 24:
        hours_quotient = hours_total // 24
        hours_total = hours_total - (hours_quotient * 24)

    if hours_total < 12:
        PM_status = False
    else:
        hours_total -= 12

    if day is not None:
        if day.casefold() == "monday":
            day_index = 1  
        elif day.casefold() == "tuesday":
            day_index = 2
        elif day.casefold() == "wednesday":
            day_index = 3
        elif day.casefold() == "thursday": 
            day_index = 4
        elif day.casefold() == "friday":   
            day_index = 5
        elif day.casefold() == "saturday": 
            day_index = 6
        elif day.casefold() == "sunday":   
            day_index = 7

        day_index += hours_quotient

        if day_index > 7:
            day_index -= 7

        if day_index == 1:
            day = "Monday"
        elif day_index == 2:
            day = "Tuesday"
        elif day_index == 3:
            day = "Wednesday"
        elif day_index == 4:
            day = "Thursday"
        elif day_index == 5:
            day = "Friday" 
        elif day_index == 6:
            day = "Saturday"
        elif day_index == 7:
            day = "Monday"

    if PM_status == True:
        results = str(hours_total) + ":" + str(minutes_total) + " PM, " + day
    else:
        results = str(hours_total) + ":" + str(minutes_total) + " AM, " + day
    arranged_dates = results
    return arranged_dates

add_time("11:50 PM", "983:50", "Sunday")
