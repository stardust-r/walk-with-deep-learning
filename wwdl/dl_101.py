# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_dl_101_pytorch_fastai.ipynb (unless otherwise specified).

__all__ = ['linear_function_dataset', 'LinRegModel', 'train', 'validate', 'nonlinear_function_dataset', 'MLP3']

# Cell
import torch
from torch.utils.data import TensorDataset
import matplotlib.pyplot as plt
import torch.nn as nn
from .utils import *

# Cell
def linear_function_dataset(a, b, n=100, show_plot=False):
    r"""
        Creates a Pytorch's `TensorDataset` with `n` random samples of the
        linear function y = `a`*x + `b`. `show_plot` dcides whether or not to
        plot the dataset
    """
    x = torch.randn(n, 1)
    y = a*x + b + 0.1*torch.randn(n, 1)
    if show_plot:
        show_TensorFunction1D(x, y, marker='.')
    return TensorDataset(x, y)

# Cell
class LinRegModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.a = nn.Parameter(torch.randn(1))
        self.b = nn.Parameter(torch.randn(1))

    def forward(self, x): return self.a*x + self.b

# Cell
def train(model, device, train_dl, loss_func, opt_func, epoch_idx):
    r"""
        Train `model` for one epoch, whose index is given in `epoch_idx`. The
        training loop will iterate through all the batches of `train_dl`, using
        the the loss function given in `loss_func` and the optimizer given in `opt_func`
    """
    running_loss = 0.0
    batches_processed = 0
    for batch_idx, (x, y) in enumerate(train_dl, 1):
        x, y = x.to(device), y.to(device) # Push data to GPU

        opt_func.zero_grad() # Reset gradients
        # Forward pass
        output = model(x)
        loss = loss_func(output, y)
        # Backward pass
        loss.backward()
        # Optimizer step
        opt_func.step()

        # print statistics
        running_loss += loss.item()
        batches_processed += 1
    print(f'Train loss [Epoch {epoch_idx}]: {running_loss/batches_processed : .2f})')

# Cell
def validate(model, device, dl):
    running_loss = 0.
    total_batches = 0
    with torch.no_grad():
        for x, y in valid_dl:
            x, y = x.to(device), y.to(device)
            output = model(x)
            loss = loss_func(output, y)
            running_loss += loss.item()
            total_batches += 1

    print(f'Valid loss: {running_loss/total_batches : .2f}')

# Cell
def nonlinear_function_dataset(n=100, show_plot=False):
    r"""
        Creates a Pytorch's `TensorDataset` with `n` random samples of the
        nonlinear function y = (-1/100)*x**7 -x**4 -2*x**2 -4*x + 1 with a bit
        of noise. `show_plot` decides whether or not to plot the dataset
    """
    x = torch.rand(n, 1)*20 - 10 # Random values between [-10 and 10]
    y = (-1/100)*x**7 -x**4 -2*x**2 -4*x + 1 + 0.1*torch.randn(n, 1)
    if show_plot:
        show_TensorFunction1D(x, y, marker='.')
    return TensorDataset(x, y)

# Cell
class MLP3(nn.Module):
    r"""
        Multilayer perceptron with 3 hidden layers, with sizes `nh1`, `nh2` and
        `nh3` respectively.
    """
    def __init__(self, n_in=1, nh1=200, nh2=100, nh3=50, n_out=1):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(n_in, nh1),
            nn.ReLU(),
            nn.Linear(nh1, nh2),
            nn.ReLU(),
            nn.Linear(nh2, nh3),
            nn.ReLU(),
            nn.Linear(nh3, n_out)
        )

    def forward(self, x): return self.layers(x)