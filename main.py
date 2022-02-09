import socket
import sys
import threading
import time

from HandleLightsContainer import HandleLightsContainer
from domain.usecase.UseCase import HandleLightsUseCase


def handle_lights(use_case: HandleLightsUseCase):
    while True:
        use_case.handle_lights()
        time.sleep(60)


if __name__ == '__main__':
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])
    handle_light_use_case = HandleLightsUseCase()
    handle_lights_thread = threading.Thread(target=handle_lights, args=(handle_light_use_case,))
    handle_lights_thread.start()

    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", 2001))
    service.listen(1)
    client, address = service.accept()
    while client:
        while True:
            message = client.recv(1024)
            print("Recibimos:")
            print(message)
            del message[0]
            del message[0]
            if message.decode("UTF-8") == "LIGHTS_ON":
                print("Aqui")
                handle_light_use_case.turn_on_lights()
            elif message.decode("UTF-8") == "LIGHTS_OFF":
                print("Alla")
                handle_light_use_case.turn_off_lights()
    print("Cerramos")
    client.close()
    service.close()
