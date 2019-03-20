import csv
categories = ['Price', 'Body Style', 'Fuel Type', 'City MPG', 'Highway MPG', 'DriveTrain',
              'Transmission', 'Engine']

def init_data():
    with open('../Data/cars.csv', mode='w') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)

        car_writer.writerow(categories)

def write_car(values):
    with open('../Data/cars.csv', mode='a') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)

        car_writer.writerow(filterCar(values))


def filterCar(values):
    new_car = []
    for i in values:
        if i[0] in categories:
            new_car.append(i[1])
    return new_car
