"""
Code taken from: https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html

It has been modified to encapsulate and label sections of code.
"""
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def load():
    """
    "Get the data" this sparse function allows a framework
    to be able to swap out different data sets easily.
    """
    iris_X, iris_y = datasets.load_iris(return_X_y=True)
    return iris_X, iris_y


def features(iris_X, iris_y):
    """Optional method to transform data, add or remove columns"""
    # if i had pandas here, I would do something!
    return iris_X, iris_y


def split(iris_X, iris_y):
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    return (iris_X_train, iris_y_train),\
           (iris_X_test, iris_y_test)


def train(iris_X, iris_y):
     # Create and fit a nearest-neighbor classifier
    model = KNeighborsClassifier()
    model.fit(iris_X, iris_y)

    return model


def predict(model, X):
    return model.predict(X)


# I propose the following would be handled by a framework

data = load()
X, y = features(*data)
train_data, test_data = split(X, y)
test_X, test_y = test_data
model = train(*train_data)
print(
    predict(model, test_X)
)

