import sys
import threading
import time
from HandleLightsContainer import HandleLightsContainer
from data.datasource.SocketServer import SocketServer
from domain.usecase.UseCase import HandleLightsUseCase

LIGHTS_ON = "LIGHTS_ON"
LIGHTS_OFF = "LIGHTS_OFF"


def handle_lights(use_case: HandleLightsUseCase):
    while True:
        use_case.handle_lights()
        time.sleep(60)


def handle_message(message):
    if message.decode("UTF-8") == LIGHTS_ON:
        handle_light_use_case.turn_on_lights()
    elif message.decode("UTF-8") == LIGHTS_OFF:
        handle_light_use_case.turn_off_lights()


if __name__ == '__main__':
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])
    handle_light_use_case = HandleLightsUseCase()
    handle_lights_thread = threading.Thread(target=handle_lights, args=(handle_light_use_case,))
    handle_lights_thread.start()

    socket_server = SocketServer()
    socket_server.listen_messages(handle_message)
