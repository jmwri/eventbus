# eventbus

## Using the event bus
```
from eventbus import bus, Event

class UserSignedInEvent(Event):
    def __init__(self, username):
        self.username = username

def first_listener(event):
    print('First', event.username)

def second_listener(event):
    print('Second', event.username)

bus.listen(UserSignedInEvent, first_listener)  # Default priority is 5
bus.listen(UserSignedInEvent, second_listener, 6)  # Priority is 6

bus.emit(UserSignedInEvent('some_user'))

#  Second some_user
#  First some_user
```

In the above example the second listen is triggered first as it's priority is higher that the first listener.

The priority can be any int, and will default at 5.