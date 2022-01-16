import wiringpi

from data.driver.RelayStatus import RelayStatus


class RelayController:

    def __init__(self, pin):
        self.__io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.__pin = pin
        self.__io.pinMode(self.__pin, self.__io.OUTPUT)

    def update_relay_status(self, relay_status: RelayStatus):
        if relay_status == RelayStatus.ON:
            self.__io.digitalWrite(self.__pin, self.__io.LOW)
        else:
            self.__io.digitalWrite(self.__pin, self.__io.HIGH)

    def get_current_relay_status(self):
        return self.__io.digitalRead(self.__pin)
