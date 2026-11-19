---
layout: page
title: "Teachable Machine"
within: machine_learning
---

# Teachable Machine Web Interface

[Experiment with Teachable Machine](https://medium.com/@warronbebster/teachable-machine-tutorial-bananameter-4bfffa765866) using the web interface.

# Train using your custom footage

Now use the data that you collected previously and the teachable machine website to train your custom model.

# Export the Model

To run the model on the Pi, you need to have a a _quantized_, _tensor flow lite_ model.  All the hard work of training and converting the model (these are quite computationally intensive operations that could not reasonably be done on the Pi).

# Put the Model on the Pi

You will have downloaded two files:
  * `labels.txt`: A file that puts a label onto the category numbers that come out from the model
  * `model.tflite`: The layers of tensors that run in the interpreter.

These should both be put into the `models` folder, under a new folder that is just for your model files.

Open `predict.py` on the Pi

~~~~
> nano predict.py
~~~~

Find the part where the `models` are defined. It is a [list](https://www.w3schools.com/python/python_lists.asp) of [tuples](https://www.w3schools.com/python/python_tuples.asp).  Add a new tuple to the end of the list with a name for your model and the directory it is stored in, for example

~~~
models = [fdafsd
          ("New Model", "new_model/")]
~~~

Now you can run the prediction program and test out your new model.