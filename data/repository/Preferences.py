from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from data.datasource import ApiDataSource, LocalDataSource
from data.datasource.NoApiPreferencesException import NoApiPreferenceException
from data.datasource.NoLocalPreferencesException import NoLocalPreferencesException
from domain.exception.HandleLightsException import HandleLightsException
from domain.model.LightPreferences import LightPreferences
from domain.model.LightPreferencesSource import LightPreferencesSource


def get_light_preferences():
    try:
        preferences = ApiDataSource.get_light_preferences()
        update_local_light_preferences(preferences)
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.API)
    except NoApiPreferenceException:
        try:
            preferences = LocalDataSource.get_light_preferences()
            return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                    LightPreferencesSource.LOCAL)
        except NoLocalPreferencesException:
            raise HandleLightsException


def update_remote_light_preferences(light_preferences: LightPreferences):
    try:
        preferences = LightPreferencesDataModel(light_preferences.starting_hour, light_preferences.finishing_hour,
                                                light_preferences.light_mode)
        ApiDataSource.update_light_preferences(preferences)
        update_local_light_preferences(preferences)
        return 0
    except NoApiPreferenceException:
        return -1


def update_local_light_preferences(preferences: LightPreferencesDataModel):
    LocalDataSource.update_light_preferences(preferences.starting_hour, preferences.finishing_hour,
                                             preferences.light_mode)
