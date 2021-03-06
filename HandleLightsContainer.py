from dependency_injector import containers, providers

from data.datasource.SocketServer import SocketServer
from data.driver.RelayController import RelayController
from data.repository.LightStatus import LightStatusRepository


class HandleLightsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    light_controller = providers.Factory(RelayController, 6)
    light_status_repository = providers.Singleton(LightStatusRepository, light_controller)
    socket_server = providers.Factory(SocketServer, 2001)
