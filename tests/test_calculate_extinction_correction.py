import pytest

import numpy as np

from BlackWidowPipeline import calculate_extinction_correction as calc_ext

import importlib
importlib.reload(calc_ext)

def test__calculate_ebv_from_halpha_hbeta_ratio__halpha_input():
    # test that the function raises an error when the input is not a numpy array
    Hbeta_map = np.array([[1, 2, 3], [4, 5, 6]])

    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio("not a numpy array", Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(123, Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio([1, 2, 3], Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio((1, 2, 3), Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio({1: 2, 3: 4}, Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(None, Hbeta_map)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(True, Hbeta_map)

def test__calculate_ebv_from_halpha_hbeta_ratio__hbeta_input():
    # test that the function raises an error when the input is not a numpy array
    Halpha_map = np.array([[1, 2, 3], [4, 5, 6]])

    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, "not a numpy array")
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, 123)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, [1, 2, 3])
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, (1, 2, 3))
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, {1: 2, 3: 4})
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, None)
    with pytest.raises(TypeError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, True)

def test__calculate_ebv_from_halpha_hbeta_ratio__same_input_shape():
    # test that the function raises an error when the input arrays do not have 
    # the same shape
    Halpha_map = np.array([[1, 2, 3], [4, 5, 6]])
    Hbeta_map = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)
