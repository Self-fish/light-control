from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from domain.model.LightMode import LightMode


def get_light_preferences():
    return LightPreferencesDataModel("14:00", "23:59", LightMode.AUTOMATIC)
