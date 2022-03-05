# Light Control
The purpose of this code is to be able to handle de lights in two different ways:

## From remote preferences
It handles the light by reading the starting and finishing hour from the [preferences-api](https://github.com/Self-fish/preferences-api-py) by asking each minute what is the correct status and updating a local cache:

```python
def handle_lights(use_case: HandleLightsUseCase):
    while True:
        use_case.check_from_preferences()
        time.sleep(60)
```

If for whatever reason the [preferences-api](https://github.com/Self-fish/preferences-api-py) is not available, it gets the preferences from the local cache:

```python
def get_light_preferences():
    try:
        preferences = ApiDataSource.get_light_preferences()
        update_local_light_preferences(preferences)
        return LightPreferences(preferences.starting_hour, 
                                preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.API)
    except NoApiPreferenceException:
        try:
            preferences = LocalDataSource.get_light_preferences()
            return LightPreferences(preferences.starting_hour, 
                                    preferences.finishing_hour, preferences.light_mode,
                                    LightPreferencesSource.LOCAL)
        except NoLocalPreferencesException:
            raise HandleLightsException
 ```
        
## From remote actions
We are able to send remote actions by using sockets. The messages are received by the [actions-api](https://github.com/Self-fish/actions-api-py) who acts as a client sending those in the port 2021

```python
def check_from_action(self):
    self.__socket_server.listen_messages(self.__handle_action)

def __handle_action(self, action):
    if action.decode("UTF-8") == LIGHTS_ON:
        self.__turn_on_lights()
    elif action.decode("UTF-8") == LIGHTS_OFF:
        self.__turn_off_lights()
```

It's done by creating a socket service listening in the port 2001

```python
class SocketServer:

    def __init__(self, port):
        self.__service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__service.bind(("", port))
        self.__service.listen(1)

    def listen_messages(self, handle_message):
        while True:
            client, address = self.__service.accept()
            try:
                while True:
                    message = client.recv(1024)
                    if message:
                        handle_message(message)
                    else:
                        break
            finally:
                client.close()
```
