'''
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        print(self.name.title() + ' rolled over')
my_dog = Dog('willie', 6)
print("My dog name is", my_dog.name.title())
my_dog.sit()
my_dog.roll_over()
tanya_dog = Dog('steph', 11)
tanya_dog.sit()
print(tanya_dog.name, ' always happy to see Tanya!')
print(tanya_dog.name, 'is', str(tanya_dog.age), 'years old')
'''


class Restaraunt:

    def __init__(self, restaraunt_name, cuisine_type):
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        print('Welcome to restaraunt', self.restaraunt_name, 'with',
        self.cuisine_type, 'kitchen')

    def open_restaraunt(self):
        print('Restaraunt is open from 11am to 2am')

    def increment_number_served(self, people):
        self.number_served += people


class IceCreamStand(Restaraunt):

    def __init__(self, restaraunt_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaraunt_name, cuisine_type)

    def describe_flavors(self, flavors):
        self.flavors = flavors
        print(self.restaraunt_name, 'has', self.flavors, 'types of ice cream')

ice = IceCreamStand('Penguin', 'Desserts')
ice.describe_flavors('strawberrty, cherry, vanila')
italy_res = Restaraunt('Bergamo', 'Italy')
print(italy_res.restaraunt_name)
italy_res.describe_restaraunt()
italy_res.open_restaraunt()
print(italy_res.number_served)
italy_res.number_served = 100
print(italy_res.number_served)
italy_res.increment_number_served(20)
print(italy_res.number_served)


class User:

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('\tGeneral user info:\nname:', self.first_name, self.last_name,
            '\ngender: ', self.gender, '\nage: ', self.age)

    def greet_user(self):
        print('Welcome back', self.first_name, self.last_name)

user1 = User('Nick', 'Pessotto', 'Male', '29')
user2 = User('Maria', 'Ostapuk', 'Female', '25')

print(user1.age)
print(user2.gender)
print(user1.first_name)
print(user2.last_name)
user1.describe_user()
user2.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


class Privileges:

    def __init__(self):
        self.privilages = ['can add messages', 'can delete users', 'can ban!']

    def show_privileges(self):
        print('Admin can:', self.privilages)


class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super(Admin, self).__init__(first_name, last_name, gender, age)
        self.privilage = Privileges()


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def fill_gas_tank(self, tank):
        self.tank = tank
        print('This car has a ' + str(self.tank) + ' liters tank')

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' km on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer')

    def increment_odometer(self, kilometers):
        if kilometers < 0:
            print('You`re trying to fcuk the system)')
        else:
            self.odometer_reading += kilometers

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
my_new_car.fill_gas_tank(70)
administrator = Admin('Admin', 'adminishe', 'n/a', 'n/a')
administrator.privilage.show_privileges()


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range1 = 240
        elif self.battery_size == 85:
            range1 = 270
        message = 'This car can approximarely ' + str(range1)
        message += 'miles on battery'
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, tank):
        self.tank = tank
        print('This car doesnt need a a gas tank!')

my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank(100)
my_tesla.battery.get_range()
print(my_tesla.battery.battery_size)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()