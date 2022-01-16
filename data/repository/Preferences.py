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
