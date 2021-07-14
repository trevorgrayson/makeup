# makeup Dependency Framework

Run Machine Learning/AI models, reproducibly, from ideation to production.

`makeup` strives to help Data Scientists write model code and not be obliged to much else.
`makeup` is the connective tissue that plugs the different stages of building a model together.

This is not a processor library, it's a code organizational framework made to make your development easier.

Additional features may be developed in this library to provide services, like a web API to host models. 

# Why?

- write less code.
- promote a "model interface" for interoperable models.
- target caching for reproducible and expedient execution. 
- simplified debugging, without hacking code.
- production deployable code that's easy to test.
- artifact rendering, to help with deployments.  


## How?

We're going to try to break our ML code down into smaller functional parts.  These parts will be simple python functions,
and we will refer to them as targets.  How big should we make these targets?  A good rule of thumb is to make a new 
target anywhere you may want to `print`, save, or inspect variables or results.  

Some example targets may be: `load`, `prep` (or `feature` generation), `split`, `train`

## Getting Started

Take an ML project, like the [Sklearn Iris Example](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).
Let's start by making a module called `iris` to name our model.  The following code will be added to `iris/__init__.py`.

### loading data

No matter what you're doing, you'll want to load some data first.  I'm hard pressed to find a example where 
the program should hardcode the data source in the code, but this seems to happen in every jupyter notebook I've ever 
seen, so let's write a method to do it.  This will be our default data, but you will be able to change data 
sources/sets at run time.

To implement that here we will use the `dataset.load_iris` function. Keep in mind, this block of code could just as
easily load a csv, call a database, or load any other data source. More on this later. 

```python
# iris/__init__.py
from sklearn import datasets

def load():
    """Returns reasonable "default data" for executon. Use in Juypter Notebooks.""" 
    iris = datasets.load_iris()
    return iris.data[:, :2], iris.target

# load = "data/yourdataset.tsv"
```

The Iris Example is loading an object and extracts two useful components from it:  
a data frame, and target numbers.

Notice the loaded `iris` variable wasn't returned, though it could've been.  By returning a generic tuple of 
python primatives you can avoid coupling your code to a data object. By explicitly stating your data requirements 
in the function's arguments, it will make it much easier to plug in different data sources, and
unit test method separately.

### training on data

Now that you have your data, you will want to train your model against it.
Rather than procedurally continuing our code, let's make another method which takes the previous
function's returned values. Let's name those returned values sensibly: `data` and `target`. 

```python
def train(data, target):
    """
    Further describing the inputs here will help later.
    data: a DataFrame with x, y, z column requirements.
    target: a list of numbers
    """
    clf = SVC()
    clf.fit(data, target)

    return clf
```

### prediction

You have your `SVC` model at this point.  Here we finish up with making a prediction.

```python
def predict(clf, row):
    return clf.predict(row)
```

This is using a generic row like our example is, but getting more explicit with your parameters may suit you better.


## Running the code...

We've defined three methods: `load`, `train`, and `predict`.  There are implicit dependencies between these functions 
which we could write some code to execute, but that's where `makeup` comes in.

### in a notebook

```python
import iris
from makeup import run, target

target(iris.train, requires=iris.load)
run(iris, 'train')
```

On the command line, this could be executed with:

```sh
python -m makeup iris train
```

You may also [override](docs/OVERRIDES.md) the data source with a URL.

```sh
python -m makeup iris train --load file://./data.csv
``` 

You could imagine dependencies getting more intricate:

```python
from makeup import target
import examples.iris as iris

target(iris.features, requires=iris.load)
target(plot, requires=iris.features)

target(iris.split, requires=iris.features)
target(iris.train, requires=iris.split)
```

```
load -> features |-> plot
                 \-> split -> train
```

OR, in abbreviated form:

```python
from makeup import workflow
import examples.iris as iris

workflow({
    iris.features: iris.load,
    plot: iris.features,
    iris.split: iris.features,
    iris.train: iris.split,
})
```




