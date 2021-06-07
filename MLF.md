# MLF Dependency Framework

Run your models, reproducibly, from ideation to production.

MLF strives to have Data Scientists write model code and not have to write much else.
MLF is the connective tissue that plugs the different stages together.

This is not a processor library, it's a code organizational framework made to make your development easier.

Additional features may be developed to provide services, like a web API. 

# Why?

- write less code.
- have a "model interface" to help you swap models.
- It caches results to make them reproducible and expedient. 
- It will renders artifacts.  This helps with deployments.  



## Getting Started

Take an ML project, like the [Sklearn Iris Example](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).
We're going to try to break that code down a bit.

Let's start by making a module called `iris` to name this model.  The following code will be added to `iris/__init__.py`.

### loading data

No matter what you're doing, you'll want to load some data first.  I'm hard pressed to find a example where the program should hardcode the data source in the
code.  This is done in every jupyter notebook I've even seen though, so let's write a method to do it.  This will be our 
default data, but you will be able to define data sources/sets at run time.

To implement that here we will use the `dataset.load_iris` function, but you should be able to pass a csv, database call, 
or any other data source at execution time. More on that later. 

`# iris/__init__.py`

```python 
def load():
    """Returns reasonable "default data" for executon. Use in Juypter Notebooks.""" 
    iris = datasets.load_iris()
    return (iris.data[:, :2], iris.target, iris.target_names)

# load = "data/yourdataset.tsv"
```
### training on data

Now that you have your data, you will want to train your model against it.
Rather than procedurally continuing our code, let's make another method.

```python
def train(data, target, target_names):
    clf = SVC()
    clf.fit(data, target)
    clf.fit(data, target_names[target])

    return clf
```

Notice the loaded `iris` variable wasn't passed, though it could be.  By returning a generic tuple or python primatives 
between these methods you can avoid coupling your code to a data object. By explicitly stating your data requirements in the 
function's arguments, it will make it much easier to unit test this method or plug in different data sources.

### prediction

You have your `SVC` model at this point.  Here we finish up with making a prediction.

```python
def predict(clf, row):
    return clf.predict(row)
```

This is using a generic row like our example is, but getting more explicit with your parameters may suit you better.


## Running the code...

We've defined three methods: `load`, `train`, and `predict`.  There are implicit dependencies between these functions 
which we could write some code to execute, but that's where `MLF` comes in.

### in a notebook

```python
import iris
from mlf import run, default_workflow
default_workflow(iris)
run(iris, 'train')
```

On the command line, this would be:

```sh
python -m mlf iris train
```





