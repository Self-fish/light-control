
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
