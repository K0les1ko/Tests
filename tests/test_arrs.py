from Tests.utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 1) == 2
    assert get([1, 2, 3], 5, default="Not Found") == "Not Found"


def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_my_slice_negative_indices():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, start=-3, end=-1) == [3, 4]

def test_my_slice_start():
    array = [1, 2, 3, 4, 5]
    assert my_slice(array, start=3, end=2) == []

def test_my_slice_empty():
    assert my_slice([], start=1, end=3) == []

def test_my_slice_indices():
    array = [1, 2, 3]
    assert my_slice(array, start=0, end=10) == [1, 2, 3]