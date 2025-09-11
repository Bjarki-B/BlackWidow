import pytest
import os
from BlackWidowPipeline import prepare_input
from astropy.io import fits

def test__open_fits():
    '''
    Test opening a FITS file using astropy.io.fits
    '''
    # Create a sample FITS file for test
    test_path = 'tests/sample.fits' 
    test_hdu = fits.PrimaryHDU()
    test_hdul = fits.HDUList([test_hdu])
    test_hdul.writeto(test_path)
    
    file = prepare_input.open_fits(test_path)
    assert isinstance(file, fits.HDUList) # Ensure file is HDUList
    assert len(file) > 0  # Ensure the file has at least one HDU
    
    # Deletes the testing file
    os.remove(test_path)
    
    
def test__flatten_array():
    '''
    Test flattening a given 2D array to 1D
    '''
    array_2d = [[1, 2, 3,],[4, 5, 6], [7, 8, 9]]
    flattened = prepare_input.flatten_array(array_2d)
    assert isinstance(flattened, list) # Ensure output is a list
    assert flattened == [1, 2, 3, 4, 5, 6, 7, 8, 9] # Ensure correct flattening