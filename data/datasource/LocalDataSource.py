from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from data.datasource.NoLocalPreferencesException import NoLocalPreferencesException
from domain.model.LightMode import LightMode

LIGHTS_CONF_FILE = "lights.conf"


def get_light_preferences():
    try:
        line_number = 0
        starting_hour = ""
        finishing_hour = ""
        mode = ""
        file = open(LIGHTS_CONF_FILE, 'r')
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
        return LightPreferencesDataModel(starting_hour, finishing_hour, LightMode[mode])
    except Exception:
        raise NoLocalPreferencesException


def update_light_preferences(starting_hour, finishing_hour, mode:LightMode):
    file = open(LIGHTS_CONF_FILE, "w")
    file.write("starting_hour=" + starting_hour + "\nfinishing_hour=" + finishing_hour + "\nmode=" + mode.name)
    file.close()
