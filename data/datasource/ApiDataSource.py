import requests

from requests.exceptions import ConnectionError, ConnectTimeout

from data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from data.datasource.NoApiPreferencesException import NoApiPreferenceException
from domain.model.LightMode import LightMode

API_URI = "http://localhost:8081/preferences?deviceId=sf-000000009df9b724"


MANUAL_OFF = "MANUAL_OFF"
MANUAL_ON = "MANUAL_ON"


def get_light_preferences():
    try:
        preferences = requests.get(API_URI)
        if preferences.status_code != 200:
            raise NoApiPreferenceException
        else:
            if preferences.json()['lightsPreferences']['mode'] == MANUAL_OFF:
                light_mode = LightMode.MANUAL_OFF
            elif preferences.json()['lightsPreferences']['mode'] == MANUAL_ON:
                light_mode = LightMode.MANUAL_ON
            else:
                light_mode = LightMode.AUTOMATIC
            return LightPreferencesDataModel(preferences.json()['lightsPreferences']['range']['starting'],
                                             preferences.json()['lightsPreferences']['range']['finishing'],
                                             light_mode)

    except (ConnectionError, ConnectTimeout):
        raise NoApiPreferenceException
