from dependency_injector.wiring import inject, Provide

from datetime import datetime
from pytz import timezone

from HandleLightsContainer import HandleLightsContainer
from data.datasource.SocketServer import SocketServer
from data.driver.RelayStatus import RelayStatus
from data.repository import Preferences
from data.repository.LightStatus import LightStatusRepository
from domain.exception.HandleLightsException import HandleLightsException
from domain.model.LightMode import LightMode
from domain.model.LightPreferences import LightPreferences
from domain.model.LightPreferencesSource import LightPreferencesSource

LIGHTS_ON = "LIGHTS_ON"
LIGHTS_OFF = "LIGHTS_OFF"
DEFAULT_TIME = "00:00"


def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    if light_preferences.light_mode == LightMode.MANUAL_ON:
        return True
    elif light_preferences.light_mode == LightMode.MANUAL_OFF:
        return False
    else:
        return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    @inject
    def __init__(self,
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository],
                 socket_server: SocketServer = Provide[HandleLightsContainer.socket_server]):
        self.__light_repository = light_repository
        self.__socket_server = socket_server

    def check_from_preferences(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        try:
            preferences = Preferences.get_light_preferences()
            if should_turn_on_lights(current_time, preferences):
                self.__light_repository.update_light_status(RelayStatus.ON)
            else:
                self.__light_repository.update_light_status(RelayStatus.OFF)
        except HandleLightsException:
            pass

    def check_from_action(self):
        self.__socket_server.listen_messages(self.__handle_action)

    def __handle_action(self, action):
        if action.decode("UTF-8") == LIGHTS_ON:
            self.__turn_on_lights()
        elif action.decode("UTF-8") == LIGHTS_OFF:
            self.__turn_off_lights()

    def __turn_on_lights(self):
        preferences = LightPreferences(DEFAULT_TIME, DEFAULT_TIME, LightMode.MANUAL_ON, LightPreferencesSource.API)
        if Preferences.update_remote_light_preferences(preferences) == 0:
            self.__light_repository.update_light_status(RelayStatus.ON)

    def __turn_off_lights(self):
        preferences = LightPreferences(DEFAULT_TIME, DEFAULT_TIME, LightMode.MANUAL_OFF, LightPreferencesSource.API)
        if Preferences.update_remote_light_preferences(preferences) == 0:
            self.__light_repository.update_light_status(RelayStatus.OFF)

