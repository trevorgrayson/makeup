# Data Science Notebooks 

Jupyter Notebooks and alike are first class citizens in this framework.

```python
from obviate import workflow, run

def load():
    """load data"""
    return [
        (1, 'whiskey'),
        (2, 'foxtrot'),
        (3, 'tango')
    ]

def features(data):
    """transform data"""
    return [(row[0]*10, row[1]) for row in data]

def train(data):
    """train it too!"""
    return data

workflow({
    features: load,
    train: features
})

run(__name__, 'train')
```
