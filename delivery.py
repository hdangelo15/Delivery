# this file contains all the functions relating to the delivery of the packages
from csvreader import all_addresses, all_distances, all_packages
import datetime
from truck import Truck


# finds the distance between two addresses --> O(1)
def find_distance_between(address1, address2):
    index1 = all_addresses.index(address1)
    index2 = all_addresses.index(address2)
    return all_distances[index1][index2]


# uses the distance traveled to calculate delivery time  --> O(1)
def calculate_delivery_time(distance, current_time):
    hours = datetime.timedelta(hours=distance / 18)
    delivery_time = current_time + hours
    return delivery_time


# finds the first package to be delivered by choosing package closest to the hub  --> O(n)
def find_first_package(package_list):
    hub_address = all_addresses[0]
    min_distance = find_distance_between(hub_address, package_list[0].address)
    first_package = package_list[0]
    for package in package_list:
        current_distance = find_distance_between(hub_address, package.address)
        if current_distance < min_distance:
            min_distance = current_distance
            first_package = package
    return first_package


# returns the package that is the shortest distance away from the current package being delivered  --> O(n)
def find_next_package(package_list, current_package):
    if package_list.__contains__(current_package):
        package_list.remove(current_package)
    first_package = package_list[0]
    next_package = package_list[0]
    min_distance = find_distance_between(current_package.address, first_package.address)
    for package in package_list:
        current_distance = find_distance_between(current_package.address, package.address)
        if current_distance < min_distance:
            min_distance = current_distance
            next_package = package
    return next_package


# creates a list of priority packages  --> O(n)
def find_priority_packages(package_list):
    priority_packages = []
    priority_addresses = []
    priority_ids = []

    for package in package_list:
        if package.deadline != 'EOD':
            priority_packages.append(package)
            priority_ids.append(package.package_id)
            priority_addresses.append(package.address)
    for package in package_list:
        if priority_addresses.__contains__(package.address) and not priority_ids.__contains__(package.package_id):
            priority_packages.append(package)
            priority_ids.append(package.package_id)
    return priority_packages


# deliver packages using the nearest neighbor algorithm  --> O(n^2)
def deliver_packages(truck, starting_package_id):
    packages_to_deliver = truck.packages
    priority_packages = find_priority_packages(packages_to_deliver)
    first_package = truck.packages[0]

    if len(priority_packages) > 0:
        if starting_package_id is not None:
            for package in priority_packages:
                if package.package_id == starting_package_id:
                    first_package = package
        else:
            first_package = find_first_package(priority_packages)

    else:
        if starting_package_id is not None:
            for package in packages_to_deliver:
                if package.package_id == starting_package_id:
                    first_package = package
        else:
            first_package = find_first_package(packages_to_deliver)

    first_distance = float(find_distance_between(all_addresses[0], first_package.address))
    truck.miles_traveled += first_distance
    first_delivery_time = calculate_delivery_time(first_distance, truck.departure)
    first_package.status = "DELIVERED"
    first_package.time_delivered = first_delivery_time
    all_packages.update(first_package.package_id, first_package)

    current_time = first_delivery_time
    current_package = first_package

    while len(priority_packages) > 1:
        packages_to_deliver.remove(current_package)
        next_package = find_next_package(priority_packages, current_package)
        next_distance = float(find_distance_between(current_package.address, next_package.address))
        truck.miles_traveled += next_distance
        next_delivery_time = calculate_delivery_time(next_distance, current_time)
        next_package.status = "DELIVERED"
        next_package.time_delivered = next_delivery_time
        all_packages.update(next_package.package_id, next_package)
        current_time = next_delivery_time
        current_package = next_package

    while len(packages_to_deliver) > 1:
        next_package = find_next_package(packages_to_deliver, current_package)
        if next_package.package_id == 9 and current_time > (datetime.datetime.combine(datetime.date.today(), datetime.time(10, 20, 0, 0))):
            next_package.address = '410 S State St'
            next_package.city = 'Salt Lake City, UT'
            next_package.zipcode = '84111'
        next_distance = float(find_distance_between(current_package.address, next_package.address))
        truck.miles_traveled += next_distance
        next_delivery_time = calculate_delivery_time(next_distance, current_time)
        next_package.status = "DELIVERED"
        next_package.time_delivered = next_delivery_time
        all_packages.update(next_package.package_id, next_package)
        current_time = next_delivery_time
        current_package = next_package

    distance_to_hub = float(find_distance_between(all_addresses[0], current_package.address))
    truck.miles_traveled += distance_to_hub
    truck.hub_return = calculate_delivery_time(distance_to_hub, current_time)


# create all truck objects and package lists  --> O(1)
truck1_packages = []
truck1 = Truck(1, truck1_packages, datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0, 0, 0)), "TBD", 0)

truck2_packages = []
truck2 = Truck(2, truck2_packages, datetime.datetime.combine(datetime.date.today(), datetime.time(9, 5, 0, 0)), "TBD", 0)

truck3_packages = []
truck3 = Truck(3, truck3_packages, datetime.datetime.combine(datetime.date.today(), datetime.time(11, 0, 0, 0)), "TBD", 0)

# manually load all the packages onto the trucks  -- O(1)
truck1_packageIDs = [13, 14, 15, 16, 19, 20, 39, 34, 21, 40, 4, 1, 2, 33, 29, 7]
truck1.load_packages(truck1_packageIDs)

truck2_packageIDs = [18, 36, 3, 38, 6, 30, 31, 37, 5, 26, 8, 25, 32, 23, 11]
truck2.load_packages(truck2_packageIDs)

truck3_packageIDs = [10, 12, 17, 22, 24, 27, 28, 35, 9]
truck3.load_packages(truck3_packageIDs)

# deliver the packages
deliver_packages(truck1, 15)
deliver_packages(truck2, 6)
deliver_packages(truck3, None)

# calculate the distance traveled by all the trucks
total_distance = (truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled)







