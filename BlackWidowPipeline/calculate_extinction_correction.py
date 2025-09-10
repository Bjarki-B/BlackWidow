import numpy as np

def calculate_ebv_from_halpha_hbeta_ratio(Halpha_map : np.ndarray, Hbeta_map : np.ndarray) -> np.ndarray:
    """Takes the Halpha and Hbeta maps and calculates the extinction correction 
    maps

    Parameters
    ----------
    Halpha_map : np.ndarray
        A numpy array of the Halpha fluxes
    Hbeta_map : np.ndarray
        A numpy array of the Hbeta fluxes, same shape as Halpha_map

    Returns
    -------
    np.ndarray
        The extinction correction map, same shape as input maps
    """
    # Check that the input is a numpy array
    if not isinstance(Halpha_map, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if not isinstance(Hbeta_map, np.ndarray):
        raise TypeError("Input must be a numpy array")
    
    # Check that the input arrays have the same shape
    if Halpha_map.shape != Hbeta_map.shape:
        raise ValueError("Input arrays must have the same shape")
    

