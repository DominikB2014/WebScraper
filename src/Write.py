import csv

categories = ['Body Style', 'Fuel Type', 'City MPG', 'Highway MPG', 'DriveTrain',
              'Transmission', 'Engine']
file_name = "cars.csv"    # Name of file


# Resets/Creates the file
def init_data():
    with open('../Data/' + file_name, mode='w', newline='') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)

        car_writer.writerow(['Make', 'Model', 'Year', 'Price'] + categories)


# Adds a car to the databse
def write_car(make:str, model:str , year: str, values):
    with open('../Data/cars.csv', mode='a', newline='') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        car_writer.writerow([make, model, year] + filter_car(values))


# Filters out un-needed categories
def filter_car(values):
    new_car = []
    i, j = 0, 0
    while i < 7:
        j = i
        while j < len(values):
            if categories[i] == values[j][0]:
                new_car.append(values[j][1])
                i += 1
                break
            else:
                j += 1
        if j == len(values):
            new_car.append('')
            i += 1

    return new_car
