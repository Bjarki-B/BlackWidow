
from astropy.io import fits

def open_fits(path: str) -> fits.HDUList:
    '''
    Open a FITS file and return the HDU list.
    path: str
        Path to the FITS file.
    '''
    with fits.open(path) as hdul:
        return hdul
    
    