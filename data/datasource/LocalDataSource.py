from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from domain.model.LightMode import LightMode
import os


def get_light_preferences():
    line_number = 0
    starting_hour = ""
    finishing_hour = ""
    mode = ""
    file = open('lights.conf', 'r')
    lines = file.readlines()
    for line in lines:
        split_line = line.split('=')
        if line_number == 0:
            starting_hour = str(split_line[1])
        elif line_number == 1:
            finishing_hour = str(split_line[1])
        else:
            mode = str(split_line[1])
        line_number += 1
    return LightPreferencesDataModel(starting_hour, finishing_hour, LightMode[mode[:-1]])


def update_light_preferences(starting_hour, finishing_hour, mode:LightMode):
    file = open("lights.conf2", "w")
    file.write("starting_hour=" + starting_hour + "\nfinishing_hour=" + finishing_hour + "\nmode=" + mode.name)
    file.close()
    print("Updating local source")
