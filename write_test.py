from solar_input import *

space_objects = read_space_objects_data_from_file('solar_system.txt')

write_space_objects_data_to_file('solar_system_new.txt', space_objects)
