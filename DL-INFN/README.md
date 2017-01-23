
# Setup

## Anaconda Python setup

- Download [Anaconda Python](https://www.continuum.io/downloads)
- Install it on your system
- from a terminal run:
```bash
conda env create 
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


