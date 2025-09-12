import numpy as np

def get_ratios(data:dict) -> dict:
    '''
    Calculate emission line ratios from input data dictionary.
    
    Parameters:
    ----------------
    data : dict
        Dictionary containing emission line fluxes with line names as keys.
        
    Returns:
    ----------------
    dict
        Dictionary containing log10 of calculated line ratios.
    '''
    
    ratios = {}
    try:
        ratios['N2'] = np.log10(data['NII'] / data['Halpha'])
        ratios['O2'] = np.log10(data['OII'] / data['Hbeta'])
        
    except KeyError as e:
        raise KeyError(f"Missing required emission line for ratio calculation: {e}")
    
    return ratios