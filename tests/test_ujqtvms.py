import pytest
import ujqtvms

def test_import():
    assert "ujqtvms/__init__.py" in ujqtvms.__file__
    assert 1 == 1
