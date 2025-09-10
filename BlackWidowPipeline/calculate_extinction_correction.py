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
    
    # Calculate the Halpha/Hbeta ratio observed
    halpha_hbeta_ratio_obs = Halpha_map / Hbeta_map

    # set the intrinsic ratio
    intrinsic_halpha_hbeta_ratio = 2.86

    # set the expected differential extinction [k(hgamma)-k(hbeta)]=0.465
    diff_ext = 0.465

    # for each pixel, calculate the ebv value
    # create an array full of small values to start with - this will be the
    # default value for pixels where the observed ratio is less than the
    # intrinsic ratio
    ebv = np.full_like(Halpha_map, 0.01, dtype=np.double)

    # only calculate ebv for the pixels where the observed ratio is greater than 
    # or equal to the intrinsic ratio
    ebv_mask = halpha_hbeta_ratio_obs >= intrinsic_halpha_hbeta_ratio

    ebv[ebv_mask] = (2.5*np.log10(halpha_hbeta_ratio_obs[ebv_mask]/intrinsic_halpha_hbeta_ratio)) / diff_ext

    return ebv

    

