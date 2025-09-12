import numpy as np

def get_ratios(data:dict, err:dict) -> dict:
    '''
    Calculate emission line ratios from input data dictionary.
    
    Parameters:
    ----------------
    data : dict
        Dictionary containing emission line fluxes with line names as keys.
    err : dict
        Dictionary containing emission line flux errors with line names as keys.
        
    Returns:
    ----------------
    dict
        Dictionary containing log10 of calculated line ratios and their errors.
    '''
    
    ratios = {}
    try:
        ratios['N2'] = np.log10(data['NII'] / data['Halpha'])
        ratios['O2'] = np.log10(data['OII'] / data['Hbeta'])
        
        ratios['err_N2'] = 1/np.log(10) * np.sqrt( (data['err_NII']/data['NII'])**2 + (data['err_Halpha']/data['Halpha'])**2)
        ratios['err_O2'] = 1/np.log(10) * np.sqrt( (data['err_OII']/data['OII'])**2 + (data['err_Hbeta']/data['Hbeta'])**2)
    except KeyError as e:
        raise KeyError(f"Missing required emission line for ratio calculation: {e}")
    
    return ratios