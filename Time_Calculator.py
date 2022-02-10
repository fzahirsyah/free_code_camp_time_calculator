
from posixpath import split

def time_calculator(current_time, added_time, day = None):
    period = None 
    meridian = ('AM' , 'PM')
    later = ''

    # splitting current time
    ct = current_time.split()
    period = ct[1]
    t = ct[0].split(':')
    shour = t[0]
    sminutes = t[1]
    hour = int(shour)
    minutes = int(sminutes)

    # splitting the added time 
    at = added_time.split(":")
    shour_added = at[0]
    sminutes_added = at[1]
    hour_added = int(shour_added)
    minutes_added = int(sminutes_added)
    

    carry, minutes = divmod(minutes + minutes_added, 60)
    hour = hour + carry
    cycles, hour = divmod(hour + hour_added, 12)

    period = abs(meridian.index(period)-(cycles % 2))
    passed = (period + cycles) // 2

    if hour == 0:
        hour = 12

    if minutes < 10:
        minutes = f"0{minutes}"

    if day:
        week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
        new_day = f',{week[(week.index(day.capitalize()) + passed) % 7]}'

    if passed == 1:
        later = 'Next Day'
    elif passed != 0:
        later = f'({passed} Days Later)'
    
    return f'{hour}:{minutes} {meridian[period]} {new_day} {later}'



    
        


    

# print(time_calculator("11:30 PM", "122:32", "Monday"))

""" 
current_timez = '3:40 AM'
added_timez =  '3:00'
day_namez  = 'monday'

print(time_calculator(current_timez, added_timez, day_namez))
""" 




