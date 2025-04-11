import pytest
from hypothesis import given
from hypothesis import strategies as st

from pytemplate.domain.entities import Intersection


class TestIntersection:

    def test_initialization(self):
        intersection = Intersection(id="A", connected_roads=["road1", "road2"])

        assert intersection.id == "A"
        assert intersection.connected_roads == ["road1", "road2"]

    def test_equality(self):
        intersection1 = Intersection(id="B", connected_roads=["road2", "road3"])
        intersection2 = Intersection(id="B", connected_roads=["road2", "road3"])

        assert intersection1 == intersection2

    def test_inequality_different_id(self):
        intersection1 = Intersection(id="C", connected_roads=["road3", "road4"])
        intersection2 = Intersection(id="D", connected_roads=["road3", "road4"])

        assert intersection1 != intersection2

    def test_inequality_different_roads(self):
        intersection1 = Intersection(id="E", connected_roads=["road4", "road5"])
        intersection2 = Intersection(id="E", connected_roads=["road4", "road6"])

        assert intersection1 != intersection2

    def test_inequality_different_type(self):
        intersection = Intersection(id="F", connected_roads=["road5", "road6"])

        assert intersection != "not an intersection"

    def test_representation(self):
        intersection = Intersection(id="G", connected_roads=["road7", "road8"])

        assert repr(intersection) == "Intersection(id='G', connected_roads=['road7', 'road8'])"

    @given(id=st.text(min_size=1, max_size=10), connected_roads=st.lists(st.text(min_size=1, max_size=10), min_size=0, max_size=5))
    def test_properties_with_hypothesis(self, id, connected_roads):
        intersection = Intersection(id=id, connected_roads=connected_roads)

        assert intersection == intersection

        repr_str = repr(intersection)
        assert id in repr_str
        assert str(connected_roads) in repr_str
