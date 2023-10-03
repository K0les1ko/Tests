import pytest


from Tests.utils.arrs import get, my_slice

def test_get():
    assert get([1, 2, 3], 1) == 2
    assert get([1, 2, 3], 5, default="Not Found") == "Not Found"

def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]