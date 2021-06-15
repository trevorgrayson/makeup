## Overrides

Data sets need to be easy to swap out for testing, production, or retraining.

Adding an optional argument named `load` (`--load`) with a URL value will override the `def load` method.

```sh
python3 -m makeup examples.iris train --load file://./datafolder/data.csv
```