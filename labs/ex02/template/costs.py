# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np


def compute_loss(y, tx, w, method="MSE"):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    if method == "MSE":
        loss = np.square((y - tx @ w)).mean()
    elif method == "MAE": 
        loss = np.abs((y - tx @ w)).mean()
    return loss