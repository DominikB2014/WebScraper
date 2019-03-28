from typing import List, Any, Union

from Utilities import *
from Data.Constants import *
import Write
import multiprocessing


def write_all_makes(models_per_year: int, file_name: str, sk_id=SkTypeID.All):
    for i in range(0, len(MAKES)):
        write_make(i, models_per_year, file_name, sk_id)


def write_makes_range(make1: int, make2: int, models_per_year, file_name, sk_id=SkTypeID.All):
    for i in range(make1, make2):
        write_make(i, models_per_year, file_name, sk_id)


def write_make(make_index, models_per_year, file_name, sk_id=SkTypeID.All):
    num_models = len(MODELS[make_index])
    for i in range(0, num_models):
        write_model(make_index, i, models_per_year, file_name, sk_id)


def write_model(make_index, model_index, models_per_year, file_name, sk_id=SkTypeID.All):
    make = MAKES[make_index]  # make[0] = Name, make[1] = id
    model = MODELS[make_index][model_index]  # model[0] = Name, model[1] = id
    years = get_years(make[1], model[1], sk_id)

    print(make[0])
    print(model[0])
    print(years)

    for year in years:
        # Links for car with certain make, model, year
        links = get_car_links(make[1], model[1], YEAR_IDS[year], sk_id)
        links = links[0:models_per_year]
        print(year + " " + make[0] + " " + model[0] + ": Writing")
        inputs = []

        for url in links:
            inputs.append((make[0], model[0], year, url, file_name))
        pool = multiprocessing.Pool()
        pool.map(__multi_process, inputs)
        pool.close()


def __multi_process(args):
    """helper function to allow passing multi-arguments to functions using multi-cores"""
    Write.write_car(*args)
