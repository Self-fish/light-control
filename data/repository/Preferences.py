from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from data.datasource import ApiDataSource, LocalDataSource
from data.datasource.NoApiPreferencesException import NoApiPreferenceException
from domain.model.LightPreferences import LightPreferences
from domain.model.LightPreferencesSource import LightPreferencesSource


def get_light_preferences():
    try:
        preferences = ApiDataSource.get_light_preferences()
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.API)
    except NoApiPreferenceException:
        preferences = LocalDataSource.get_light_preferences()
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.LOCAL)


def update_light_preferences(light_preferences: LightPreferences):
    try:
        preferences = LightPreferencesDataModel(light_preferences.starting_hour, light_preferences.finishing_hour,
                                                light_preferences.light_mode)
        ApiDataSource.update_light_preferences(preferences)
        return 0
    except NoApiPreferenceException:
        return -1
