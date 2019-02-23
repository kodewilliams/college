from locations import location_dict

# Write your code below this line.
place = input('Enter location: ')
    
if place not in location_dict:
    if place in location_dict.values():
        print (place)
    else:
        print ('Location not found.')
else:
    print (place, end='')
    while (place in location_dict):
        place = location_dict[place]
        print (',', place, end='')

