from external.Interface import *
from Write import init_data

file_name = "newCars.csv"
make = 24

init_data(file_name)
write_make(make - 1, 5, file_name, SkTypeID.New)
