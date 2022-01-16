from domain.model.LightMode import LightMode


class LightPreferencesDataModel:

    def __init__(self, starting_hour, finishing_hour, light_mode: LightMode):
        self.starting_hour = starting_hour
        self.finishing_hour = finishing_hour
        self.light_mode = light_mode
