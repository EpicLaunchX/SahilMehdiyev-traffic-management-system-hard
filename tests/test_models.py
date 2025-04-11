import pytest

from pytemplate.domain.models import TrafficLightState

def test_traffic_light_state_values():
    assert TrafficLightState.RED.value == "red"
    assert TrafficLightState.YELLOW.value == "yellow"
    assert TrafficLightState.GREEN.value == "green"


def test_traffic_light_state_str_representation():
    assert str(TrafficLightState.RED) == "red"
    assert str(TrafficLightState.YELLOW) == "yellow"
    assert str(TrafficLightState.GREEN) == "green"


def test_traffic_light_state_comparison():
    assert TrafficLightState.RED == TrafficLightState.RED
    assert TrafficLightState.YELLOW != TrafficLightState.RED
    assert TrafficLightState.GREEN != TrafficLightState.RED
    assert TrafficLightState.GREEN != TrafficLightState.YELLOW


def test_traffic_light_state_from_string():
    assert TrafficLightState("red") == TrafficLightState.RED
    assert TrafficLightState("yellow") == TrafficLightState.YELLOW
    assert TrafficLightState("green") == TrafficLightState.GREEN


def test_traffic_light_state_invalid_value():
    with pytest.raises(ValueError):
        TrafficLightState("invalid")