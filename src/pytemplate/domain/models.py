from enum import Enum


class TrafficLightState(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

    def __str__(self) -> str:
        """
        Returns the string representation of the traffic light state.

        Returns:
            str: The string value of the enum member.
        """
        return self.value
