import numpy as np
import emcee 

from BlackWidowPipeline import scaling_relations_Curti2020 as scalrel

def uniform_log_metallicity_prior(metallicity):
    """Calculate the uniform log prior for metallicity.

    Parameters
    ----------
    metallicity : float
        metallicity values (12 + log(O/H)).

    Returns
    -------
    0.0 or -inf : float
        log of the prior value, 0.0 if within bounds, -inf if outside bounds.
    """
    if -1.0 < metallicity < 1.0:
        return 0.0
    return -np.inf


def log_likelihood(metallicity, line_ratios_obs, line_ratios_err):
    """
    Simple Gaussian likelihood function.
    """
    # either loop over the line ratios or use a vectorized approach
    model = scalrel.line_ratios(metallicity)
    return -0.5 * np.sum(((line_ratios_obs - model) / line_ratios_err) ** 2)