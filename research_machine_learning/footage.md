---
layout: page
title: "Getting Footage"
within: machine_learning
---

# Transfer Learning

We have been running existing models so far.  We would like to be able to create our own models.  Unfortunately that requires _a deep understanding of tensor networks_ and _thousands of labelled images_.  

unless....

If we use a technique called ["transfer learning"](https://youtu.be/kRpZ5OqUY6Y) we can adjust an existing model to perform a specialised task.  Watch the first six minutes of [this video](https://youtu.be/kRpZ5OqUY6Y) to get an idea of what we will be doing.

This all works much better if we use the same camera to capute the training data that we will use to run the predictor, so we need to capture data with the Pi camera and that is what we will do here

# Choose a specialised task.

Think of something you would like your Pi to detect for you, a simple on/off categorisation is easiest.  Here are some suggestions:
  * Is there someone with a red shirt?
  * Is there a coffee cup?
  * Is it day or night?
  * Has the Pi been inverted?
  * Is the Pi on its side?

# Capture footage that includes the "yes" and "no" state in multiple contexts

Since we have enabled the legacy camera support, we can use the `raspistill` command to capture images.  `raspistill` has the following options that will help us:
  * `-awb greyworld` helps to improve the color in images from our camera (which has no IR filter so lots of extra red gets introduced, particularly outside)
  * `-tl 1000` take a new image every 1000 milliseconds
  * `-t 0` don't timeout, just keep taking images
  * `-o captures/img%04d` is a code for the image file names that will be used 

The full command is

~~~~~
raspistill -awb greyworld -tl 1000 -t 0 -o captures/img%04d.jpg
~~~~~

if your camera is upside down, you might want to add `-rot 180` to rotate the images

## Stopping the capture

This capture will run forever.  You can stop it with `Ctrl-C`.  If you lost access to the terminal, you can run `ps` and look for the process, then kill it by hand.

# Get the images off the Pi

Use SFTP to download all the images that were captured.

# Separate the images into "yes" and "no" categories.

Use whatever operating system help you can to preview hte images. On a mac, using Finder with a large icon size works well for me.  I can quickly identify most of the negative images and move them into a special folder.  I can look more carefully at the others to decide whether they are positive or negative.  Once you have them separated into folders, you can train a new model.
