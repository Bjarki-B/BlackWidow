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

def test__calculate_ebv_from_halpha_hbeta_ratio__correct_output_shape():
    # test that the function returns an array with the same shape as the input 
    # arrays
    Halpha_map = np.array([[1, 2, 3], [4, 5, 6]])
    Hbeta_map = np.array([[1, 2, 3], [4, 5, 6]])
    ebv_map = calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)
    assert ebv_map.shape == Halpha_map.shape
    assert ebv_map.shape == Hbeta_map.shape

def test__calculate_ebv_from_halpha_hbeta_ratio__ratio_less_than_intrinsic():
    # test that the function returns an array with values of 0.01 when the ratio
    # of Halpha to Hbeta is less than the intrinsic ratio of 2.86
    Halpha_map = np.array([[1, 1, 1], [1, 1, 1]])
    Hbeta_map = np.array([[1, 1, 1], [1, 1, 1]])
    ebv_map = calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)
    assert np.all(ebv_map == 0.0)

def test__calculate_ebv_from_halpha_hbeta_ratio__ratio_equal_to_intrinsic():
    # test that the function returns an array with values of 0.0 when the ratio
    # of Halpha to Hbeta is equal to the intrinsic ratio of 2.86
    Halpha_map = np.array([[2.86, 2.86, 2.86], [2.86, 2.86, 2.86]])
    Hbeta_map = np.array([[1, 1, 1], [1, 1, 1]])
    ebv_map = calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)
    assert np.all(ebv_map == 0.0)

def test__calculate_ebv_from_halpha_hbeta_ratio__ratio_greater_than_intrinsic():
    # test that the function returns an array with values greater than 0.0 when 
    # the ratio of Halpha to Hbeta is greater than the intrinsic ratio of 2.86
    Halpha_map = np.array([[5, 5, 5], [5, 5, 5]])
    Hbeta_map = np.array([[1, 1, 1], [1, 1, 1]])
    ebv_map = calc_ext.calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)
    assert np.all(ebv_map > 0.0)

