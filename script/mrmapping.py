import numpy as np

def map_apsiii():
    pass

def map_lods(score):
     logit = -3.4043 + 0.4173(score)
     return (np.exp(logit)) / (1 + np.exp(logit))

def map_oasis():
    pass

def map_sapsii(score):
    logit = -7.7631 + 0.0737 * (score) + 0.9971 *  (np.log(score+1))
    return (np.exp(logit)) / (1 + np.exp(logit))

def weighted_average():
    pass
