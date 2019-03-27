from Utilities import *
from Data.Constants import *
import Write


def write_make(make_index, models_per_year, file_name, sk_id=SkTypeID.All):
    num_models = len(MODELS[make_index])
    for i in range(0, num_models):
        write_model(make_index, i, models_per_year, file_name, sk_id)


def write_model(make_index, model_index, models_per_year, file_name, sk_id=SkTypeID.All):
    make = MAKES[make_index] # make[0] = Name, make[1] = id
    model = MODELS[make_index][model_index] # model[0] = Name, model[1] = id
    years = get_years(make[1], model[1], sk_id)

    print(make[0])
    print(model[0])
    print(years)

    for year in years:
        # Links for car with certain make, model, year
        links = get_car_links(make[1], model[1], YEAR_IDS[year], sk_id)
        links = links[0:models_per_year]
        print(year + " " + make[0] + " " + model[0] + ": Writing")
        for url in links:
            print(url)
            Write.write_car(make[0], model[0], year, get_car(url), file_name)
