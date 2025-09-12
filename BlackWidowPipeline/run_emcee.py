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


def log_likelihood_individual_line(metallicity, line_ratio_obs, line_ratio_err):
    """
    Simple Gaussian likelihood function for a given metallicity and observed 
    line ratios with their uncertainties.

    Parameters
    ----------
    metallicity : float
        The value of 12 + log(O/H).
    line_ratios_obs : dict
        Dictionary of observed line ratios. Keys must be consistent with those 
        in scaling_relations_Curti2020.py
    line_ratios_err : dict
        Dictionary of uncertainties in the observed line ratios, same shape as 
        line_ratios_obs.
    """
    # Get all line ratios from the model at the given metallicity
    line_ratios_model = scalrel.line_ratios(metallicity)

    # create a list to add log-likelihoods to for each line ratio
    log_likelihoods = []

    # iterate through the keys and calculate the log-likelihood
    for key in line_ratio_obs.keys():
        if key not in scalrel.coeffitients_dic.keys():
            raise ValueError(f"Key {key} not found in scaling relations dictionary.")
        if key not in line_ratio_err.keys():
            raise ValueError(f"Key {key} not found in line ratio error dictionary.")
        
        # calculate the log-likelihood for each line ratio
        log_prob = ((line_ratio_obs[key] - line_ratios_model[key]) / line_ratio_err[key]) ** 2

        # append to the list
        log_likelihoods.append(log_prob)

    # convert to a numpy array
    log_likelihoods = np.array(log_likelihoods)

    # return the total log-likelihood
    total_log_likelihood = -0.5*np.sum(log_likelihoods)

    return total_log_likelihood

def log_posterior_individual_line(metallicity, line_ratio_obs, line_ratio_err):
    """
    Calculate the log posterior for a given metallicity and observed line ratios
    with their uncertainties.
    
    Parameters
    ----------
    metallicity : float
        The value of 12 + log(O/H).
    line_ratios_obs : dict
        Dictionary of observed line ratios. Keys must be consistent with those 
        in scaling_relations_Curti2020.py
    line_ratios_err : dict
        Dictionary of uncertainties in the observed line ratios, same shape as 
        line_ratios_obs.
    """
    # calculate the log prior
    log_prior = uniform_log_metallicity_prior(metallicity)

    # if the prior is not finite, return -inf
    if not np.isfinite(log_prior):
        return -np.inf
    
    # calculate the log likelihood
    log_likelihood = log_likelihood_individual_line(metallicity, line_ratio_obs, line_ratio_err)

    # return the log posterior
    return log_prior + log_likelihood