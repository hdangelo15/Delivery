# Hayley D'Angelo Student ID: #000455324
import datetime
import sys
import time

from csvreader import all_packages
from delivery import total_distance

# This is the user interface of the program. It lets the user find the information for a single package at a particular
# time or the information for all the packages at a particular time.

print('***************************************')
print('WGUPS Package Delivery System')
print('***************************************\n')
# Display the total distance traveled by all the trucks. --> O(1)
print('The current route can be completed in ' + str("%.1f" % total_distance) + ' miles.\n')

# Loop through the interface. The user can exit at any point or to return to the beginning at the end. --> O(n^2)
finished = False
while finished is False:
    # Prompt the user to pick an option
    display_choice = input("Choose one of the following options:\n" +
                           "Enter '1' to view data for a single package at a given time\n" +
                           "Enter '2' to view data for all packages at a given time\n" +
                           "Enter 'e' to exit\n\n" +
                           "Input your choice to continue: ").lower()
    print('\n')
    # Prompt the user to pick again if input isn't valid
    while display_choice not in ('1', '2', 'e'):
        print("Please try again with a valid input.\n")
        display_choice = input("Choose one of the following options:\n" +
                               "Enter '1' to view data for a single package\n" +
                               "Enter '2' to view data for all packages\n" +
                               "Enter 'E' to exit\n" +
                               "Input your choice to continue: ")
        print('\n')
    # Display a single package's data at a particular time
    if display_choice == '1':
        package_id = input('Please enter the id of the package or "e" to exit: ').lower()
        package = None
        valid_id = False
        # Look for 'e' to exit or catch any invalid package ids and prompt the user again
        while valid_id is False:
            if package_id == 'e':
                print('Have a great day!')
                sys.exit()
            try:
                package_id = int(package_id)
                package = all_packages.search(package_id)
                if package is None:
                    valid_id = False
                    package_id = input('Please enter a valid package id or enter "e" to exit: ').lower()
                else:
                    valid_id = True
            except ValueError:
                valid_id = False
                package_id = input('Please enter a valid package id or enter "e" to exit: ').lower()
        # Prompt for the time to search for
        print('Enter the time you would like a status for:')
        input_hour = input('Enter an hour value (0 - 23) or enter "e" to exit: ').lower()
        valid_hour = False
        # Look for 'e' to exit or catch any invalid time values and prompt the user again
        while valid_hour is False:
            if input_hour == 'e':
                print('Have a great day!')
                sys.exit()
            try:
                input_hour = int(input_hour)
                if input_hour not in range(0, 24):
                    valid_hour = False
                    input_hour = input('Please enter a valid hour value (0 - 23) or enter "e" to exit: ').lower()
                else:
                    valid_hour = True
            except ValueError:
                valid_hour = False
                input_hour = input('Please enter a valid hour value (0 - 23) or enter "e" to exit: ').lower()

        input_minutes = input('Enter a minutes value (0 - 59) or enter "e" to exit: ').lower()
        valid_minutes = False
        while valid_minutes is False:
            if input_minutes == 'e':
                print('Have a great day!')
                sys.exit()
            try:
                input_minutes = int(input_minutes)
                if input_minutes not in range(0, 60):
                    valid_minutes = False
                    input_minutes = input('Please enter a valid minutes value (0 - 60) or enter "e" to exit: ').lower()
                else:
                    valid_minutes = True
            except ValueError:
                valid_minutes = False
                input_minutes = input('Please enter a valid minutes value (0 - 60) or enter "e" to exit: ').lower()

        input_time = datetime.datetime.combine(datetime.date.today(), datetime.time(input_hour, input_minutes, 0, 0))
        # Find the status of the package at the input time
        if input_time < package.delivery_truck.departure:
            package.status = 'AT HUB'
            estimated_time = ' NOTE: Displayed time is delivery estimate.'
        elif package.delivery_truck.departure <= input_time < package.time_delivered:
            package.status = 'EN ROUTE'
            estimated_time = ' NOTE: Displayed time is delivery estimate.'
        elif input_time >= package.time_delivered:
            package.status = 'DELIVERED'
            estimated_time = ''

        # Display the package data
        print('Calculating...')
        time.sleep(0.5)
        print('Status at ' + str(input_time) + ':')
        print(package, estimated_time)

    # Display the data for all packages at a particular time
    elif display_choice == '2':
        # Prompt for a time to search for
        print('Enter the time you would like package statuses for:')
        input_hour = input('Enter an hour value (0 - 23) or enter "e" to exit: ')
        # Look for 'e' to exit or catch any invalid time values and prompt the user again
        valid_hour = False
        while valid_hour is False:
            if input_hour == 'e':
                print('Have a great day!')
                sys.exit()
            try:
                input_hour = int(input_hour)
                if input_hour not in range(0, 24):
                    valid_hour = False
                    input_hour = input('Please enter a valid hour value (0 - 23) or enter "e" to exit: ')
                else:
                    valid_hour = True
            except ValueError:
                valid_hour = False
                input_hour = input('Please enter a valid hour value (0 - 23) or enter "e" to exit: ')

        input_minutes = input('Enter a minutes value (0 - 59) or enter "e" to exit: ')
        valid_minutes = False
        while valid_minutes is False:
            if input_minutes == 'e':
                print('Have a great day!')
                sys.exit()
            try:
                input_minutes = int(input_minutes)
                if input_minutes not in range(0, 60):
                    valid_minutes = False
                    input_minutes = input('Please enter a valid minutes value (0 - 60) or enter "e" to exit: ')
                else:
                    valid_minutes = True
            except ValueError:
                valid_minutes = False
                input_minutes = input('Please enter a valid minutes value (0 - 60) or enter "e" to exit: ')

        input_time = datetime.datetime.combine(datetime.date.today(), datetime.time(input_hour, input_minutes, 0, 0))

        # Display the data of the packages at the input time
        print('Calculating...')
        time.sleep(0.5)

        packages_to_list = []
        i = 1
        while i <= 40:
            package = all_packages.search(i)
            packages_to_list.append(package)
            i += 1

        print('Status at ' + str(input_time) + ':')

        for package in packages_to_list:
            if input_time < package.delivery_truck.departure:
                package.status = 'AT HUB'
                estimated_time = ' NOTE: Displayed time is delivery estimate.'
            elif package.delivery_truck.departure <= input_time < package.time_delivered:
                package.status = 'EN ROUTE'
                estimated_time = ' NOTE: Displayed time is delivery estimate.'
            elif input_time >= package.time_delivered:
                package.status = 'DELIVERED'
                estimated_time = ''
            print(package, estimated_time)
    # Exit the program if 'e' input
    elif display_choice == 'e':
        print('Have a great day!')
        sys.exit()

    print('\n')
    # Prompt the user to exit or search again
    end_input = input('Enter "1" to perform another action or "e" to exit: ').lower()
    while end_input not in ('1', 'e'):
        print('Please enter a valid input.')
        end_input = input('Enter "1" to perform another action or enter "e" to exit: ').lower()

    if end_input == '1':
        print('\n')
        finished = False
    elif end_input == 'e':
        finished = True
# Exit the program when finished
print('Have a great day!')
sys.exit()

