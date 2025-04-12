from typing import List


class Intersection:
    """
    Represents a traffic intersection in the traffic management system.

    Attributes:
        id (str): Unique identifier for the intersection.
        connected_roads (List[str]): List of road identifiers connected to this intersection.
    """

    def __init__(self, id: str, connected_roads: List[str]):
        """
        Initialize a new Intersection.

        Args:
            id (str): Unique identifier for the intersection.
            connected_roads (List[str]): List of road identifiers connected to this intersection.
        """
        self.id = id
        self.connected_roads = connected_roads

    def __eq__(self, other):
        """
        Check if two intersections are equal.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        if not isinstance(other, Intersection):
            return False
        return self.id == other.id and self.connected_roads == other.connected_roads

    def __repr__(self):
        """
        Return a string representation of the intersection.
        Returns:
            str: String representation.
        """
        return f"Intersection(id={self.id!r}, connected_roads={self.connected_roads})"
