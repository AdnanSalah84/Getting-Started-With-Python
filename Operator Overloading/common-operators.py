"""Modules"""
import numpy as np
import pandas as pd

print([1, 2, 3] * 2)

print(np.array([1, 2, 3]) * 2)

food = pd.Series({
    'apples': 2,
    'oranges': 4,
    'grapes': 6,
})

print(food * 2)

items = pd.DataFrame({
    'qty': pd.Series({
        'apples': 2,
        'oranges': 4,
        'grapes': 6,
    }),
     'amt': pd.Series({
        'apples': 1.49,
        'oranges': 0.99,
        'grapes': 2.49,
    })
})

print(items * 2)

