import csv
from Utilities import get_car
from Data.Constants import CATEGORIES, NUM_CAT


def init_data(file_name):
    """Resets/Sets the data"""
    with open('../Data/' + file_name, mode='w', newline='') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)

        car_writer.writerow(['Make', 'Model', 'Year'] + CATEGORIES)


def write_car(make: str, model: str, year: str, url, file_name):
    categories = get_car(url)
    """Adds a car to the database"""
    if categories is None:
        return None
    with open('../Data/' + file_name, mode='a', newline='') as cars_file:
        car_writer = csv.writer(cars_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        car_writer.writerow([make, model, year] + filter_car(categories))


def filter_car(values):
    """Filters out un-needed categories"""
    new_car = []
    i, j = 0, 0
    while i < NUM_CAT:
        j = 0
        while j < len(values):
            if CATEGORIES[i] == values[j][0]:
                new_car.append(values[j][1])
                i += 1
                break
            else:
                j += 1
        if j >= len(values):
            new_car.append('')
            i += 1

    return new_car
