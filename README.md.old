# Machine Learning Framework



## reading data

It's important for you to be agile with your data sources. MLF provides several 
ways of importing data.

### cli

Any additional arguments that you pass to MLF will be preferred first as arguments.
The first argument you name for `load` or `run` will trump all other sources and 
come from these arguments.

```
    python -m mlf 123
```

will translate into

```
class YourModel(MlfBase):
    def run(self, one_two_three):
```

#### files

On the command line, all arguments after `--` will be interpreted as files, and 
read in as `panda` csvs.

```
    python -m mlf 123 -- data.csv
```

### data.py module

After the preceeding sources, the source for arguments will be the
`data.py` file which is next to your model file in the same module.

```
|-> data.py
|-> your_model.py
```

`data.py` will be loaded, and it will find methods or varibles by using the
name of the variable in your method.

```
# data.py
# -------

def some_data():
    for data in datum:
      yield data

def other_data():
    return 1

# your_model.py
# -------------
class YourModel(MlfBase):

    def run(self, some_data, other_data):
        pass
```

## loading data

Frequently the data you read isn't in the format your model needs it to be in.
This is where the `load` method comes in.

The `load` method is reserved for taking in your data arguments and transforming them 
into the specification that your model needs.

`load` will receive arguments exactly as run would (stated above), and whatever it returns will 
be directly fed to the run method.


```
class YourModel:

    def load(self, some_data, other_data):
        some_join_other = zip(some_data, other_data)

        return (some_join_other, ['weird', 'array', 'i', 'made', 'up'])
    
    def run(self, some_join_other, weird):
        # do things!
        pass

```

### LOAD_MODULE

Lastly, if you wish to have more choices over `data.py` you can specify the module you want the data to be pulled from.

```
import your_data

class YourModel(MlfBase):
    LOAD_MODULE = your_data

    def run(self, from_your_data):
        pass
```

# caching `load`

# considerations

* data set separation
* *running*
* encapsulation
* testing
* telemetry
* deployment

## play

## train

## evaluate

## predict

## visualize

look at output of load and try to auto generate? give levers?

## MLF Delegate

Pick a module or notebook to delegate method calls to. 
You may place this inline in a notebook to experiment
with your notebook.


```
from mlf import delegate as mlf

DATASET = 'some/data.tsv'

def features(df):
    ... do feature stuff
    return features_df


# change `features` to stage of your choosing.
mlf.features(DATASET)
```
