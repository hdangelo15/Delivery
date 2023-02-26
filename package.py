# This class creates the package object

class Package:
    # package constructor
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, status, time_delivered, delivery_truck):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.time_delivered = time_delivered
        self.delivery_truck = delivery_truck

    # display the package object as a string
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status,
            self.time_delivered, ('Truck ' + str(self.delivery_truck.truck_id)))
