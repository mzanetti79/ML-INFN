
# Setup

## Anaconda Python setup

- Download [Anaconda Python](https://www.continuum.io/downloads)
- Install it on your system
- from a terminal run:
```bash
cd deeplearnweekend
conda env create -f setup/environment.yml
```

### Testing the environment

Now you should be able to run a simple test script that learns a shallow model on dummy data as well as plots it.

Start IPython notebook:
```bash
jupyter notebook
```
and open and run `Test_Installation.ipynb`.

### Change Keras backend

When you ran Keras in the test script, it created a configuration file located at `~/.keras/keras.json` that probably looks like this:

```json
{"epsilon": 1e-07, "floatx": "float32", "backend": "theano"}
```

It specifies the backend that it uses. Let's switch `"theano"` to `"tensorflow"`. When you rerun the test script, you should now see it print out that it is using the Tensorflow backend.


## Alternative to Anaconda: Setup from scratch

If you prefer not to use Anaconda python, below are the instructions to set up a virtual environment using the python provided in your system. We do not recommend using this option. For simplicity and to avoid conflicts with other libraries installed on your system, we will use virtualenv to create a python environment and then set up Tensorflow, Keras, and IPython Notebook.

Install virtualenv with pip if you don't have it:
```bash
pip install virtualenv
```

With virtualenv, create a new environment in the `~/deeplearn` directory. We will be using python 2.7.
```bash
virtualenv ~/deeplearn
```

Enter the new environment (you might want to make an alias for this - alias=):
```bash
source ~/deeplearn/bin/activate
```

Install tensorflow for Mac OS X. If you are using another OS, refer to https://www.tensorflow.org/versions/r0.7/get_started/os_setup.html#pip-installation to find the correct package for your system):

```bash
pip install https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py2-none-any.whl
```

Install Keras, IPython notebook, scikit-learn, matplotlib
```bash
pip install keras
pip install Jupyter
pip install sklearn
pip install matplotlib
pip install h5py
```

NOTE: With this installation, you will only be able to use matplotlib inline in IPython Notebooks. See http://matplotlib.org/faq/virtualenv_faq.html for alternatives. One easy option (though it opens you to possibly hard to debug environment problems) is to create the virtualenv with `virtualenv --system-site-packages ~/deeplearn` and pip install matplotlib in your system python, outside of the virtualenv.
