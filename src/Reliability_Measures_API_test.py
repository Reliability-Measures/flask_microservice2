from . import Reliability_Measures_API

def test_Reliability_Measures_API():
    assert Reliability_Measures_API.apply("Jane") == "hello Jane"
