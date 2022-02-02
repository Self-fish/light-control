from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from domain.model.LightMode import LightMode


def get_light_preferences():
    line_number = 0
    starting_hour = ""
    finishing_hour = ""
    mode = ""
    file = open('lights.conf', 'r')
    lines = file.readlines()
    for line in lines:
        print(line)
        split_line = line.split('=')
        print(split_line)
        if line_number == 0:
            starting_hour = str(split_line[1])
        elif line_number == 1:
            finishing_hour = str(split_line[1])
        else:
            mode = str(split_line[1])
        line_number += 1
    print(starting_hour)
    print(finishing_hour)
    print(mode)
    return LightPreferencesDataModel(starting_hour, finishing_hour, LightMode[mode[:-1]])
