---
layout: page
title: "TensorFlow on Pi"
within: machine_learning
---

We will tour the code that you have just downloaded with some explanations of what each part does.  We include links to more details to help you understand the concepts in a broader context

{: .keypoint}
Code lives a different life to documenation - these notes _will_ be out of date.  We keep them as close to current as possible, but you will find small differences for sure.  We still think it is useful to discuss though and you are welcome to let us know of any differences you find.
# What libraries are required?

~~~~~
import argparse
import subprocess
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import time
import glob
~~~~~

`argparse` will help us with command line parameters, `subprocess` is used to run the camera when we don't have a python binding, `PIL` helps us convert a jpeg image to a format that can go in the predictor.  `tflite_runtime.interpreter` is where the action occurs.  We don't import all of tflite since we are not traning or building models, only loading them and running them.

# Which model or source will be run?

~~~~~
argparser = argparse.ArgumentParser(description="Run a Model on a set of images or a camera feed and generate predictions.")
argparser.add_argument("--model", metavar="M", type=int, help="the index of the model to use.")
argparser.add_argument("--source", metavar="S", type=int, help="the index of the source to use.")
args = argparser.parse_args()

models = [("MobileNet V1 224","models/mobilenet_v1_1.0_224_quant"),
          ("MobileNet V1 128","models/mobilenet_v1_0.25_128_quant"),
          ("Custom: Is the camera covered?", "models/covered_quant")
         ]

sources = [("Example Images",["images/224x224/*",
                              "images/room.jpg", 
                              "images/239x215/*", 
                              "images/128x128/*",
                              "images/imagenet_examples/*"
                              ]),
           ("Camera","")
          ]

if args.model is None:
  print("Which model would you like to run?")
  for i, mod in enumerate(models):
    print(f"({i}) {mod[0]}")
  model_i = int(input())
else:
  model_i = args.model

if args.source is None:
  print("Which source would you like predict from?")
  for i, src in enumerate(sources):
    print(f"({i}) {src[0]}")
  src_i = int(input())
else:
  src_i = args.source
~~~~~

At the end of this block of code, we have an array of models and the index of the model we want to use - similarly for sources.  If the user put in a command line option to pick the model or source, the `args` variable will contain their choices.  Thus, we have two `if` blocks, one for models and one for sources, which first looks to see if an option was given on the command line and asks the user for their choice if none was given.  

We use two arrays-of-tuples (`models` and `sources`) to keep track of what models/sources are available and where they can be found in the file system.  The first parameter of the tuple is a human-readable name and the second is the path in the file system.  Images can be in multiple paths, so we give an array of paths.  As you add new images that you want processed, you can either put them in a folder already represented or you can add your new folder here.  If you add a new model, it will need its own directory and that directory will need to be added to `models`.

Note that "Camera" is a special source since there is no file associated with it.  We provide a function `feed` that will make the image source and the camera source look the same to the rest of the code.

~~~~~
def feed(lst_globs):
  if lst_globs == "":
    while True:
      subprocess.run(["libcamera-jpeg", "-o","images/camera-feed.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      yield "images/camera-feed.jpg"
  else:
    for img_glob in sources[src_i][1]:
      for img_path in glob.glob(img_glob):
        yield img_path
~~~~~

{: .keypoint}
This is an early and inefficient version, we have probably improved it but the overall idea is the same

This function is a special type of Python function, a generator.  It can be put on the range section of a loop and will give items one-by-one until it runs out.  This generator gives back file locations, looping thrhough each image until it runs out.  If the source feed is the camera instead, it takes a new picture each time and puts it in a special file location, giving that back each time.  The file location never changes, but there will be new image from the camera each time it is generated.  In this case, there is no end to the list of images generated, it goes until the user hits `Ctrl-C`.

# Load a TensorFlow Lite Interpreter and name its input and output tensors

A model is actually a _series of tensors_ which feed numbers through.  A tensor is (pretty much) a matrix.

First we load the model tensor from the file it is stored in

~~~~~
interpreter = tflite.Interpreter(models[model_i][1]+"/model.tflite")
interpreter.allocate_tensors()
~~~~~

To _run_ a tensor is to simply fill the input tensor with the data from your image, execute it, and read the data that appears in the output tensor.

We output some information about our input tensor to help debug if things go wrong.  This code assumes certain things about the "shape" of this tensor so we can check here to see any custom models match what is expected.

~~~~~
inputs = interpreter.get_input_details()[0];
outputs = interpreter.get_output_details()[0];
width  = inputs["shape"][2]
height = inputs["shape"][1]
dtype = inputs["dtype"]
scale, zero = outputs['quantization']
print(f"Predicting with model:  {models[model_i][0]} ({width}x{height}) {dtype}")
~~~~~

There are multiple variants of TensorFlow.  Standard TensorFlow processes floating numbers.  TensforFlow _Lite_ processes integers instead.  This is less-precise but much faster.  Any mention of _quantization_ is a reference to the fact that the floating point numbers from a normal TensorFlow model have been converted to integers for this version. 


# Go through each source frame

We rely on the `feed` generator to send us images one at a time, from whichever source was chosen

~~~~~
for img_path in feed(sources[src_i][1]):
~~~~~

and the rest of the processing is done once for each.

# Run the model to create a prediction

The image is loaded, converted to the right data format for this model, and resized to match the shape of the input tensor

~~~~~
  img = Image.open(img_path).convert('RGB').resize((width, height))

  # we need another dimension
  input_data = np.expand_dims(img, axis=0)
~~~~~

That data is put into the input tensor

~~~~~
  interpreter.set_tensor(inputs["index"], input_data)
~~~~~

and the model is "run"

~~~~~
  interpreter.invoke()
~~~~~

This will populate all the tensors in the model with integers, including the one we are interested it for our prediction - the output tensor.  We read the values from this tensor to get our prediction (`squeeze` flattens an extra nested array we didn't need).

~~~~~
  output_data = interpreter.get_tensor(outputs["index"]).squeeze()
~~~~~

The output data represents a percentage confidence in the prediction, but because we are working with integers, not floats, we need to convert those back to a number between zero and one, which is done based on how the model was quantized.

~~~~~
  output_data = (scale*100) * (output_data - zero)
~~~~~

And we now have our prediction!  It is in a strange form though.  We have an array of numbers between 0 and 1.

# Convert the output Tensor to a prediction

We firstly need to know what the output tensor represents.  Every model is trained on a set of possible outputs. ImageNet has 1 thousand ("bird", "mug", "rifle", "plane", etc), the cutom `covered` model has just two ("covered" or "uncovered").  Each slot in output tensor is the confidence that that category is the right one.  Take a look in the `labels.txt` of your model to see what each index corresponds to.  The output tensor just gives an integer, we need the `labels.txt` to turn that number (index) into the category that the model was trained with.

Thus, each number (in position 'i') represents the confidence that the prediction `i` is the right one.  To find out what prediction is the most likely, we need to find the index with the highest value.  So we sort the array by value, keeping track of which index was attached to each value

~~~~~
ordered_indexes = np.flip(output_data.argsort())
~~~~~

The index at the start of this list will be the one with the highest confidence.

If we look that index up in the labels file, we will get the category name and if we look it up in the original output tensor we will get the confidence.

~~~~~
  best_index = ordered_indexes[0]
  print(f"  * {img_path} = {labels[best_index]} %0.0f%%" % output_data[best_index])
~~~~~
