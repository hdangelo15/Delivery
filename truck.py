# this class creates the truck object and the methods to load and deliver packages

from csvreader import all_packages


class Truck:
    # truck constructor
    def __init__(self, truck_id, packages, departure, hub_return, miles_traveled):
        self.truck_id = truck_id
        self.packages = packages
        self.departure = departure
        self.hub_return = hub_return
        self.miles_traveled = miles_traveled

    # display the truck object as a string
    def __str__(self):
        return "%s %s %s %s %s" % (self.truck_id, self.packages, self.departure, self.hub_return, self.miles_traveled)

    # add packages to the truck from a list of package IDs  --> O(n)
    def load_packages(self, id_list):
        for package_id in id_list:
            all_packages.search(package_id).status = 'EN ROUTE'
            all_packages.search(package_id).delivery_truck = self
            self.packages.append(all_packages.search(package_id))


