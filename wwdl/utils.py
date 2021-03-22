# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/utils.ipynb (unless otherwise specified).

__all__ = ['show_TensorFunction1D']

# Cell
from fastcore.all import *
import torch
import matplotlib.pyplot as plt

# Cell
@delegates(plt.Axes.scatter)
def show_TensorFunction1D(x, y, y_hat=None, return_fig=False, **kwargs):
    r"""
        Displays the 1D function `y`(`x`), with optional predictions `y_hat`
    """
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(x, y, **kwargs)
    if y_hat is not None: ax.scatter(x, y_hat, **kwargs)
    if return_fig: return figure