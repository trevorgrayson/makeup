import pathlib
import setuptools
from distutils.core import setup

ROOTDIR = pathlib.Path(__file__).parent
README = (ROOTDIR / "README.md").read_text()


setup(
      name='makeup',
      version='0.1.0',
      packages=setuptools.find_packages(),
      description='Make your models look pretty.',
      long_description=README,
      author='trevor grayson',
      author_email='trevor@dave.com',
      url='https://github.com/trevorgrayson/mlf',
      py_modules=['makeup'],
      keywords=[
            'machine learning', 'data science', 'make', 'models'
      ],
      # license='',
      # packages=['distutils', 'distutils.command'],
      # scripts=['bin/makeup']
)
