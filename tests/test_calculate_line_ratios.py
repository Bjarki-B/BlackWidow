import pytest
import numpy as np
from BlackWidowPipeline import calculate_line_ratios



def test__calculate_line_ratios():
    '''
    Test calculation of line ratios
    '''
    
    test_dict = {'Halpha': np.array([1,2,3]), 'Hbeta': np.array([4,5,6]), 'OII': np.array([7,8,9]), 'NII': np.array([10,11,12])}
    ratios = calculate_line_ratios.get_ratios(test_dict)
    
    assert 'N2' in ratios
    assert 'O2' in ratios
    
    assert np.array_equal(ratios['N2'], np.log10(np.array([10.0, 5.5, 4.0])))
    assert np.array_equal(ratios['O2'], np.log10(np.array([1.75, 1.6, 1.5])))