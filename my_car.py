from car import Car

my_new_car = Car('Honda', 'Civic Type R', 2008)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 99000
my_new_car.read_odometer()