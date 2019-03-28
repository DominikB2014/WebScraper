from external.Interface import *
from Write import init_data

file_name = "newCars.csv"
make = 24 #honda

# init_data(file_name)
# write_make(make - 1, 5, file_name, SkTypeID.New)
if __name__ == '__main__':
    write_makes_range(0, 10, 5, file_name, SkTypeID.New)
# write_makes_range(10, 20, 5, file_name, SkTypeID.New)
# write_makes_range(20, 30, 5, file_name, SkTypeID.New)
# write_makes_range(30, 40, 5, file_name, SkTypeID.New)
# write_makes_range(40, 50, 5, file_name, SkTypeID.New)
# write_makes_range(50, 60, 5, file_name, SkTypeID.New)
# write_makes_range(60, 70, 5, file_name, SkTypeID.New)
# write_makes_range(70, 72, 5, file_name, SkTypeID.New)

