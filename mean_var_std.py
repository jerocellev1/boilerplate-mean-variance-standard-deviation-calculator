import numpy as np
import pandas as pd
import random

def calculate(list):

list = np.array([random.randint(1,10)for _ in range(9)])
list = {
    'mean': [np.mean(list[0]).item(), np.mean(list[1]).item(), np.mean(list.flatten()).item()],
    'variance': [np.var(list[0]).item(), np.var(list[1]).item(), np.var(list.flatten()).item()],
    'standard deviation': [np.std(list[0]).item(), np.std(list[1]).item(), np.std(list.flatten()).item()],
    'max': [np.max(list[0]).item(), np.max(list[1]).item(), np.max(list.flatten()).item()],
    'min': [np.min(list[0]).item(), np.min(list[1]).item(), np.min(list.flatten()).item()],
    'sum': [np.sum(list[0]).item(), np.sum(list[1]).item(), np.sum(list.flatten()).item()]
}

print(list)

    return calculations
