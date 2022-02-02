from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from domain.model.LightMode import LightMode


def get_light_preferences():
    line = 0
    starting_hour = ""
    finishing_hour = ""
    with open('lights.conf') as file:
        file_contents = file.read()
        row_line = file_contents.split('=')
        if line == 0:
            starting_hour = str(row_line[1])
        else:
            finishing_hour = str(row_line[1])
        line += 1
    print(starting_hour)
    print(finishing_hour)
    return LightPreferencesDataModel(starting_hour, finishing_hour, LightMode.AUTOMATIC)
