hour = int(input('Enter the hour: '))
mins = int(input('Enter the minute: '))

if (hour == 0):
    print ('12:'    + str(mins).zfill(2) + ' AM')

if (0 < hour < 12):
    print (str(hour) + ':' + str(mins).zfill(2) + ' AM')

if (24 > hour > 12 and hour != 0):
    hour -= 12
    print (str(hour) + ':' + str(mins).zfill(2) + ' PM')
else:
    print ('Invalid time.')
