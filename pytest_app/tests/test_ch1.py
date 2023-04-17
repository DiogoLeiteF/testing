from pytest_app.app.app import vouel_count, shortLong
import pytest

def test_first_name():
    assert vouel_count("carlos") == 2
    assert vouel_count("KIDMAN") == 2


def test_name():
    assert vouel_count("carlos lkasnd") == 3
    assert vouel_count("KIDMAN     123654") == 2



def test_string():
    assert shortLong("A cow jumped over the moon") == ["A", "jumped"]
    assert shortLong("A") == ["A","A"]
    assert shortLong("") == None
    assert shortLong("1 cow jumped over the moonland") == ["1", "moonland"]