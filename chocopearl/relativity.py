import numpy as np

def calculate_gamma_beta_momentum(energy, mass):
    '''
    Energy and mass must be in the same units (in natural units). For example, if energy is in GeV, mass must be in GeV. 
    The function outputs momentum also in that same units.
    '''
    gamma= (energy/mass)
    momentum= np.sqrt(energy**2 - mass**2)
    beta=momentum/energy
    return float(gamma),float(beta),float(momentum)
