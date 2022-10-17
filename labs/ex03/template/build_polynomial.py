# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    poly = np.ones(shape=(len(x), degree+1))
    poly[:,0] = 1
    for i in range(degree):
        poly[:,i+1] = np.power(x, i+1)
    
    return poly
