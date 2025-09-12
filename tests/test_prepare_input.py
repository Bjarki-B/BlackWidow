import pytest
import os
import numpy as np
from BlackWidowPipeline import prepare_input
from astropy.io import fits

def test__flatten_input():
    '''
    Test flattening result from input FITS file
    '''
    array = np.array([[1, 2, 3,],[4, 5, 6], [7, 8, 9]])
    hdu = fits.PrimaryHDU(array, header=fits.Header({'EXTNAME':'Halpha'}))
    hdu1 = fits.ImageHDU(array*2, header=fits.Header({'EXTNAME':'Hbeta'}))
    hdu2 = fits.ImageHDU(array*3, header=fits.Header({'EXTNAME':'OII'}))
    hdu3 = fits.ImageHDU(array*4, header=fits.Header({'EXTNAME':'NII'}))
    hdul = fits.HDUList([hdu, hdu1, hdu2, hdu3])
    hdul.writeto('tests/sample.fits', overwrite=True)
    
    data_dict = prepare_input.flatten_input('tests/sample.fits')
    flattened = data_dict[0]['Halpha']
    print(data_dict)
    assert isinstance(flattened, np.ndarray) # Ensure output is an array
    assert np.array_equal(flattened, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # Ensure correct flattening
    assert np.array_equal(data_dict[0]['Hbeta'], [2, 4, 6, 8, 10, 12, 14, 16, 18])
    assert np.array_equal(data_dict[0]['OII'], [3, 6, 9, 12, 15, 18, 21, 24, 27])
    assert np.array_equal(data_dict[0]['NII'], [4, 8, 12, 16, 20, 24, 28, 32, 36])
    # Cleanup
    os.remove('tests/sample.fits')
    
def test__check_input():
    
    test_dict = {'Halpha': np.array([1,2,3]), 'Hbeta': np.array([4,5,6]), 'OII': np.array([7,8,9]), 'NII': np.array([10,11,12])}
    checked_dict = prepare_input.check_input(test_dict)
    assert checked_dict == test_dict
    
    array = np.array([[1, 2, 3,],[4, 5, 6], [7, 8, 9]])
    hdu = fits.PrimaryHDU(array, header=fits.Header({'EXTNAME':'Halpha'}))
    hdu1 = fits.ImageHDU(array*2, header=fits.Header({'EXTNAME':'Hbeta'}))
    hdu2 = fits.ImageHDU(array*3, header=fits.Header({'EXTNAME':'OII'}))
    hdu3 = fits.ImageHDU(array*4, header=fits.Header({'EXTNAME':'NII'}))
    hdul = fits.HDUList([hdu, hdu1, hdu2, hdu3])
    hdul.writeto('tests/sample.fits', overwrite=True)
    
    checked_fits = prepare_input.check_input('tests/sample.fits')
    assert isinstance(checked_fits, tuple)
    assert isinstance(checked_fits[0], dict)
    assert np.array_equal(checked_fits[0]['Halpha'], array.flatten())
    os.remove('tests/sample.fits')
    