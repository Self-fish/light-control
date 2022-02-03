from dependency_injector.wiring import inject, Provide

from datetime import datetime
from pytz import timezone

from HandleLightsContainer import HandleLightsContainer
from data.driver.RelayStatus import RelayStatus
from data.repository import Preferences
from data.repository.LightStatus import LightStatusRepository
from domain.model.LightMode import LightMode
from domain.model.LightPreferences import LightPreferences
from domain.model.LightPreferencesSource import LightPreferencesSource


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
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        self.__light_repository = light_repository

    def handle_lights(self):
        print("Manejamos luces")
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        preferences = Preferences.get_light_preferences()
        print(preferences.starting_hour)
        print(preferences.finishing_hour)
        print(preferences.source)
        if should_turn_on_lights(current_time, preferences):
            print("Encendemos las luces")
            self.__light_repository.update_light_status(RelayStatus.ON)
        else:
            print("Apagmos las luces")
            self.__light_repository.update_light_status(RelayStatus.OFF)

    def turn_on_lights(self):
        print("Evento de encender luces")
        preferences = LightPreferences("00:00", "00:00", LightMode.MANUAL_ON, LightPreferencesSource.API)
        if Preferences.update_light_preferences(preferences) == 0:
            self.__light_repository.update_light_status(RelayStatus.ON)

    def turn_off_lights(self):
        print("Evento de apagar luces")
        preferences = LightPreferences("00:00", "00:00", LightMode.MANUAL_OFF, LightPreferencesSource.API)
        if Preferences.update_light_preferences(preferences) == 0:
            self.__light_repository.update_light_status(RelayStatus.OFF)

