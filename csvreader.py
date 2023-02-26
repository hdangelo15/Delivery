# this file reads in the csv files containing the data for the packages, distances, and addresses

import csv
from hashtable import PackageHashTable
from package import Package

# creates a hash table to hold the packages
all_packages = PackageHashTable()
# reads the data for the packages --> O(n)
with open('packageFile.csv') as file:
    package_data = csv.reader(file, delimiter=',')
    next(package_data)
    for row in package_data:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = row[6]
        status = "AT HUB"
        time_delivered = "TBD"
        delivery_truck = "TBD"

        # creates a package object and inserts that object into the hash table
        p = Package(package_id, address, city, state, zipcode, deadline, weight, status, time_delivered, delivery_truck)
        all_packages.insert(package_id, p)

# creates a list of all the address data
all_addresses = []
# reads the data for the addresses  --> O(n)
with open('addressFile.csv') as file:
    address_data = csv.reader(file, delimiter=',')
    for row in address_data:
        all_addresses.append(row[0])

# creates a list of all the distance data
all_distances = []
# reads the data for the distances  --> O(n)
with open('distanceFile.csv') as file:
    distance_data = csv.reader(file, delimiter=',')
    for row in distance_data:
        all_distances.append(row)
