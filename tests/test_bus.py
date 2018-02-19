import pytest

from evntbus import evntbus, Event, listen


class MyEvent(Event):
    def __init__(self, v1=None, v2=None):
        self.data = {
            'v1': v1,
            'v2': v2,
        }

    def set_v1(self, val):
        self.data['v1'] = val

    def set_v2(self, val):
        self.data['v2'] = val

    def get_v1(self):
        return self.data['v1']

    def get_v2(self):
        return self.data['v2']


@pytest.fixture
def event():
    return MyEvent(1, 2)


def test_event(event):
    assert event.get_v1() is 1
    assert event.get_v2() is 2


def test_listen(event):
    def increment_v1(event):
        event.set_v1(2)
    evntbus.listen(type(event), increment_v1)
    assert event.get_v1() is 1
    evntbus.emit(event)
    assert event.get_v1() is 2


def test_decorator(event):
    @listen(type(event))
    def increment_v1(event):
        event.set_v1(2)
    assert event.get_v1() is 1
    evntbus.emit(event)
    assert event.get_v1() is 2
