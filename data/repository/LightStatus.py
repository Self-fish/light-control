from data.driver.RelayController import RelayController
from data.driver.RelayStatus import RelayStatus


class LightStatusRepository:

    def __init__(self, light_controller: RelayController):
        self.__light_controller = light_controller
        self.current_light_status = self.__light_controller.get_current_relay_status()
        self.__light_controller.update_relay_status(RelayStatus.OFF)

    def update_light_status(self, light_status):
        if light_status != self.current_light_status:
            self.__light_controller.update_relay_status(light_status)
            self.current_light_status = light_status
