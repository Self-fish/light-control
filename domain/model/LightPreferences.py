
from domain.model.LightMode import LightMode
from domain.model.LightPreferencesSource import LightPreferencesSource


class LightPreferences:

    def __init__(self, starting_hour, finishing_hour, light_mode: LightMode, source: LightPreferencesSource):
        self.__starting_hour = starting_hour
        self.__finishing_hour = finishing_hour
        self.__light_mode = light_mode
        self.__source = source

