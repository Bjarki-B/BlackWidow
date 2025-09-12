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


def log_likelihood(metallicity, line_ratio_obs, line_ratio_err):
    """
    Simple Gaussian likelihood function for a given metallicity and observed 
    line ratios with their uncertainties. Assumes that the line ratios are in 
    log space (i.e., log(R)).
    Parameters
    ----------
    metallicity : float
        The value of 12 + log(O/H).
    line_ratios_obs : dict
        Dictionary of observed line ratios. Keys must be consistent with those 
        in scaling_relations_Curti2020.py. Line ratios should be in log space.
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
        log_prob = np.log10(((10**line_ratio_obs[key] - 10**line_ratios_model[key]) / 10**line_ratio_err[key]) ** 2)

        # append to the list
        log_likelihoods.append(log_prob)

    # convert to a numpy array
    log_likelihoods = np.array(log_likelihoods)

    # return the total log-likelihood
    total_log_likelihood = -0.5*np.sum(log_likelihoods)

    return total_log_likelihood

def log_posterior(metallicity, line_ratio_obs, line_ratio_err):
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
    total_log_likelihood = log_likelihood(metallicity, line_ratio_obs, line_ratio_err)

    # return the log posterior
    return log_prior + total_log_likelihood


def run_mcmc(line_ratio_obs, line_ratio_err, n_walkers=50, n_steps=1000, n_burn=200, initial_metallicity=8.5):
    """
    Run the MCMC sampler to estimate the distribution of metallicities
    given observed line ratios and their uncertainties.
    
    Parameters
    ----------
    line_ratios_obs : dict
        Dictionary of observed line ratios. Keys must be consistent with those 
        in scaling_relations_Curti2020.py
    line_ratios_err : dict
        Dictionary of uncertainties in the observed line ratios, same shape as 
        line_ratios_obs.
    n_walkers : int, optional
        Number of MCMC walkers, by default 50.
    n_steps : int, optional
        Number of MCMC steps, by default 1000.
    n_burn : int, optional
        Number of burn-in steps to discard, by default 200.
    initial_metallicity : float, optional
        Initial guess for metallicity (12 + log(O/H)), by default 8.5, which is 
        solar metallicity.
        
    Returns
    -------
    samples : ndarray
        Array of shape (n_walkers * (n_steps - n_burn),) containing the 
        posterior samples of metallicity.
    """
    # Initialize walkers in a small Gaussian ball around the initial guess
    initial_pos = initial_metallicity + 1e-4 * np.random.randn(n_walkers)

    # Set up the MCMC sampler
    sampler = emcee.EnsembleSampler(
        n_walkers, 
        1,  # single parameter: metallicity
        log_posterior, 
        args=(line_ratio_obs, line_ratio_err)
    )

    # Run the MCMC sampler
    sampler.run_mcmc(initial_pos, n_steps, progress=True)

    # Discard burn-in samples and flatten the chain
    samples = sampler.get_chain(discard=n_burn, flat=True)

    return samples.flatten()