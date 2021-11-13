import pytest
import ujqtvms

def test_import():
    assert "ujqtvms/__init__.py" in ujqtvms.__file__
