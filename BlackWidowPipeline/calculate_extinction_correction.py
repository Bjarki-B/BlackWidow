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

    Raises
    ------
    TypeError
        If either input is not a numpy array
    ValueError
        If the input arrays do not have the same shape
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
    # from Calzetti 2001 PASP 113 we have L_Halpha/L_Hbeta = 2.87
    intrinsic_halpha_hbeta_ratio = 2.87

    # set the expected differential extinction [k(hgamma)-k(hbeta)]=0.465
    diff_ext = 0.465

    # for each pixel, calculate the ebv value
    # create an array full of small values to start with - this will be the
    # default value for pixels where the observed ratio is less than the
    # intrinsic ratio
    ebv = np.full_like(Halpha_map, 0.0, dtype=np.double)

    # only calculate ebv for the pixels where the observed ratio is greater than 
    # or equal to the intrinsic ratio
    ebv_mask = halpha_hbeta_ratio_obs >= intrinsic_halpha_hbeta_ratio

    ebv[ebv_mask] = (2.5*np.log10(halpha_hbeta_ratio_obs[ebv_mask]/intrinsic_halpha_hbeta_ratio)) / diff_ext

    return ebv

def calculate_Alambda_from_ebv(ebv_map : np.ndarray, wavelength : float) -> np.ndarray:
    """Calculates the A(lambda) map from the ebv map and a wavelength or array of
    wavelengths, or a map of the same wavelength the same shape as the ebv map

    Parameters
    ----------
    ebv_map : np.ndarray
        The E(B-V) map
    wavelength : float
        The wavelength at which to calculate the extinction correction, in 
        Angstroms. 

    Returns
    -------
    np.ndarray
        The A(lambda) map(s) at the specified wavelength(s). If a single 
        wavelength is provided, the output will have the same shape as the input
        ebv_map. If an array of wavelengths is provided, the output will be a 3D
        array with shape (n_wavelengths, height, width)

    Raises
    ------
    TypeError
        If the ebv_map is not a numpy array
    TypeError
        If the wavelength is not a float
    """
    # check that the ebv_map is a numpy array
    if not isinstance(ebv_map, np.ndarray):
        raise TypeError("Input must be a numpy array")
    
    # check that the wavelength is a float
    if not isinstance(wavelength, float):
        raise TypeError("Wavelength must be a float")
    
    # define the constant (using MW expected curve)
    Rv = 3.1

    # use that to calculate Av
    Av = ebv_map * Rv

    # convert lamdas from Angstroms into micrometers
    wavelength = wavelength/10000

    #define the equations from the paper
    y = wavelength**(-1) - 1.82
    a_x = 1.0 + 0.17699*y - 0.50447*(y**2) - 0.02427*(y**3) + 0.72085*(y**4) + 0.01979*(y**5) - 0.77530*(y**6) + 0.32999*(y**7)
    b_x = 1.41338*y + 2.28305*(y**2) + 1.07233*(y**3) - 5.38434*(y**4) - 0.62251*(y**5) + 5.30260*(y**6) - 2.09002*(y**7)

    # find A(lambda)
    Alambda = (a_x + b_x/Rv)*Av
    
    return Alambda

def calc_extinction_correction(Halpha_map : np.ndarray, Hbeta_map : np.ndarray, wavelength : float|np.ndarray) -> np.ndarray:
    """Takes the Halpha and Hbeta maps and a wavelength (or array of wavelengths)
    and calculates the extinction correction map(s) at that wavelength

    Parameters
    ----------
    Halpha_map : np.ndarray
        A numpy array of the Halpha fluxes
    Hbeta_map : np.ndarray
        A numpy array of the Hbeta fluxes, same shape as Halpha_map
    wavelength : float or np.ndarray
        The wavelength(s) at which to calculate the extinction correction, in 
        Angstroms. If a numpy array is provided, it must be either 1D or have 
        the same spatial shape as the input maps but all the same value.

    Returns
    -------
    np.ndarray
        The extinction correction map(s) at the specified wavelength(s). If a 
        single wavelength is provided, the output will have the same shape as 
        the input maps. If an array of wavelengths is provided, the output will 
        be a 3D array with shape (n_wavelengths, height, width)
    """
    # first calculate the ebv map from the halpha and hbeta maps
    ebv_map = calculate_ebv_from_halpha_hbeta_ratio(Halpha_map, Hbeta_map)

    # then calculate the Alambda map from the ebv map and the wavelength
    Alambda_map = calculate_Alambda_from_ebv(ebv_map, wavelength)

    return Alambda_map
