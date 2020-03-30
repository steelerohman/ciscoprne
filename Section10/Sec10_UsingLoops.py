#
# Section 10 Using Loops
# Quarantine
# Requires devices txt file

from pprint import pprint

devices_list = [] # Create the outer list for all devices

# Read in the devices from the file
file = open('devices','r')
for line in file:

    device_info_list = line.strip().split(',') # Get device info into list
    devices_list.append(device_info_list)

file.close() # Close the file since we are done with it


print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
                                         device[2],device[3])

                                         
