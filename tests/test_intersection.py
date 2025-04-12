import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from src.pytemplate.domain.entities import Intersection


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
        assert intersection != None
        assert intersection != 123
        assert intersection != {"id": "F", "connected_roads": ["road5", "road6"]}

    def test_representation(self):
        intersection = Intersection(id="G", connected_roads=["road7", "road8"])
        expected = f"Intersection(id={repr(intersection.id)}, connected_roads={repr(intersection.connected_roads)})"
        assert repr(intersection) == expected

    @pytest.mark.parametrize(
        "id_value,roads",
        [
            ("", []),
            ("A", []),
            ("", ["road1"]),
            ("Very_Long_ID_Value_For_Testing", ["road1", "road2"]),
            ("Special@#$%^&*", ["road1", "road2", "road3"]),
            ("İntersec✨", ["🚗road1"]),
        ],
    )
    def test_edge_cases(self, id_value, roads):
        intersection = Intersection(id=id_value, connected_roads=roads)
        assert intersection.id == id_value
        assert intersection.connected_roads == roads

        expected = f"Intersection(id={repr(id_value)}, connected_roads={repr(roads)})"
        assert repr(intersection) == expected

    @given(
        id=st.text(min_size=1, max_size=10),
        connected_roads=st.lists(st.text(min_size=1, max_size=10), min_size=0, max_size=5),
    )
    def test_properties_with_hypothesis(self, id, connected_roads):
        intersection = Intersection(id=id, connected_roads=connected_roads)
        assert intersection == intersection  # reflexivity
        repr_str = repr(intersection)
        assert repr(id) in repr_str
        assert repr(connected_roads) in repr_str

    @given(
        id1=st.text(min_size=1, max_size=10),
        id2=st.text(min_size=1, max_size=10),
        roads=st.lists(st.text(min_size=1, max_size=10), min_size=0, max_size=5),
    )
    def test_inequality_different_ids_property(self, id1, id2, roads):
        assume(id1 != id2)
        intersection1 = Intersection(id=id1, connected_roads=roads)
        intersection2 = Intersection(id=id2, connected_roads=roads)
        assert intersection1 != intersection2

    @given(
        id=st.text(min_size=1, max_size=10),
        roads1=st.lists(st.text(min_size=1, max_size=10), min_size=0, max_size=5),
        roads2=st.lists(st.text(min_size=1, max_size=10), min_size=0, max_size=5),
    )
    def test_inequality_different_roads_property(self, id, roads1, roads2):
        assume(roads1 != roads2)
        intersection1 = Intersection(id=id, connected_roads=roads1)
        intersection2 = Intersection(id=id, connected_roads=roads2)
        assert intersection1 != intersection2

    def test_empty_initialization(self):
        intersection = Intersection(id="", connected_roads=[])
        assert intersection.id == ""
        assert intersection.connected_roads == []

    def test_invalid_types(self):
        with pytest.raises(TypeError):
            Intersection(id=123, connected_roads=["r1"])  # id not string

        with pytest.raises(TypeError):
            Intersection(id="A", connected_roads=None)  # connected_roads not list

        with pytest.raises(TypeError):
            Intersection(id="A", connected_roads=[1, 2, 3])  # elements not str
