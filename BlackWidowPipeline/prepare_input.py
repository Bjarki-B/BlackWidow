import numpy as np
from astropy.io import fits

def flatten_input(path: str, ext_dict = None) -> dict:
    '''
    Open a FITS file, flatten its data, and return the flattened array. 
    path: str
        Path to the FITS file.
    ext_dict: dict
        Dictionary of emission lines and their corresponding extensions in the HDUList.
        
    returns:
        data_dict: dict
            Dictionary with emission lines as keys and flattened arrays as values.
    '''
    data_dict = {"Halpha":None, "Hbeta":None, "OII":None, "NII":None} # Dictionary for holding arrays
    if  ext_dict is None:
        ext_dict = {"Halpha":0, "Hbeta":1, "OII":2, "NII":3} # Defult extensions
        
    with fits.open(path) as hdul: # Open the FITS file
        for line, ext in ext_dict.items(): # Loop over the emission lines
            data_dict[line] = np.array((hdul[ext].data).flatten()) # Flatten and store in dictionary
    
    return data_dict

def check_input(data = None):
    '''
    Check whether the input is a dictionary of numpy arrays or a path to a FITS file.
    If it's a dictionary, validate its contents. If it's a path, process the FITS file with flatten_input.
    data: dict or str
        Either a dictionary with emission lines as keys and numpy arrays as values, or a path to a FITS file.
    returns:
        If input is a dictionary, returns the same dictionary after validation.
        If input is a FITS file path, returns a dictionary with flattened arrays.
    '''
    if type(data) is dict:
        assert all(isinstance(v, np.ndarray) for v in data.values()), "All values in the dictionary must be numpy arrays."
        assert {"Halpha", "Hbeta", "OII", "NII"} <= data.keys(), "Dictionary must contain keys: 'Halpha', 'Hbeta', 'OIII', 'NII'."
        return data
    elif type(data) is str:
        return flatten_input(data)
    else:
        raise ValueError("Input must be either a dictionary of numpy arrays or a path to a FITS file.")