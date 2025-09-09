import pytest

import numpy as np

from BlackWidowPipeline import calculate_extinction_correction as calc_ext

def test__calculate_extinction_correction__input():
    # test that the function raises an error when the input is not a numpy array
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction("not a numpy array")
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction(123)
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction([1, 2, 3])
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction((1, 2, 3))
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction({1: 2, 3: 4})
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction(None)
    with pytest.raises(TypeError):
        calc_ext.calculate_extinction_correction(True)
