from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from domain.model.LightMode import LightMode


def get_light_preferences():
    with open('lighs.conf') as file:
        file_contents = file.read()
        print(file_contents)
    return LightPreferencesDataModel("14:00", "23:59", LightMode.AUTOMATIC)
