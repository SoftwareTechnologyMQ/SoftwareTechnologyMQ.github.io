---
layout: page
title: "Setup"
within: machine_learning
---

basic instructions for getting a RaspbarianLite image and installing the required libraries

We are going to create an embedded "detector" using machine learning techniques.  We will implement it on embedded hardware so real-time detection can be performed anywhere at any time.  Lets call this device the "spot-a-tron" (SaT)

The SaT is a Raspberry Pi  setup with the right libraries, applications, and running our machine learning models.  Much of the initial work is done and you will be working from that starting point.

The embedded hardware we are using is the Raspberry Pi, so our first step is to get a working Pi.

# Background to Raspberry Pi

Raspberry Pi is a small sized computer that can essentailly perform the same tasks as our computers at home. The device can be plugged into a monitor and controlled with a keyboard and mouse to be used as a fully functioning computer. It is low-cost, modular, and high performing, originally developed for teaching purposes for computer science students but growing into much more.

<div style="width:50%; margin:auto">
	<img src="https://upload.wikimedia.org/wikipedia/commons/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg "/>
</div>

Learn more about Raspberry Pi at these links below:
<ol>
	<li><a href="https://en.wikipedia.org/wiki/Raspberry_Pi">https://en.wikipedia.org/wiki/Raspberry_Pi</a></li>
    <li><a href="https://thepihut.com/blogs/raspberry-pi-tutorials/the-raspberry-pi-tutorial-beginners-guide">https://thepihut.com/blogs/raspberry-pi-tutorials/the-raspberry-pi-tutorial-beginners-guide</a></li>
    <li><a href="https://www.edureka.co/blog/raspberry-pi-tutorial/">https://www.edureka.co/blog/raspberry-pi-tutorial/</a></li>
</ol>


# Setting up the Raspberry Pi for SaT

Our Raspberry Pi will use a SD card as the operating system. The SD card normally uses an operating system call 'Raspbarian', which is designed specifically for Raspberry Pi's.   There are actually multiple variants of Raspbarian, the right one for us is "Rasparian Lite (32 bit)". Follow the steps below to set up the mini console onto our Raspberry Pi.
  * [Installing a Fresh Operating System](https://www.raspberrypi.com/software/)
# Using Raspberry Pi

To use Raspberry Pi, we need a monitor to view what we are doing, as well as a keyboard and mouse to control it. Follow the steps below to connect and boot up the Raspberry Pi. Make sure you have read the links at the top of the page and understand what Raspberry Pi is and how it works before completing these steps. 

<ol>
	<li>Insert the SD card into the SD card slot.</li>
	<li>Connect a monitor to the HDMI port. Make sure the monitor is connected to a wall socket and is powered on. The Raspberry Pi is still off, so you won’t see anything yet.</li>
    <li>Connect a keyboard to a USB port.</li>
    <li>If you want to connect to the Internet via Ethernet instead of WiFi, you should also plug in an Ethernet cable. The Raspberry Pi we have provided will allow to connect to Internet wirelessly</li>
    <li>Connect the power supply to a wall socket and plug in the micro USB cable. A red LED will light up on the Raspberry Pi, and on the monitor you will see the Raspberry Pi booting up. In a few moments you will see the login prompt.</li>
</ol>

You boot into any fresh Pi with
  * username: `pi`
  * password: `raspbarian` 

The only way to work in Raspabarian Lite is via the terminal.  In the next worksheet we will learn more about how to work in the terminal, but we will get a sneak preview here as we get the libraries and appliations that we need installed.

<a href="https://projects.raspberrypi.org/en">Here</a> are some resources to show all the other projects you could do with a Raspberry Pi.

## Terminal Preview

One you have logged in, type `ls` exactly as it is written here, then press enter. This will give you a list of files and directories that the Raspberry Pi holds. 

### updated to here

In this list, you will find a directory that is named 'mq_mini_console'.
<div style="width:75%; margin:auto">
	<img src="figs/raspberry_pi_run_mini_console2.png"/>
</div>
<br>

Now we want to navigate to this file. Type `cd mq_mini_console` and press enter. 
<div style="width:75%; margin:auto">
	<img src="figs/raspberry_pi_run_mini_console3.png"/>
</div>
<br>

The only way we have to run the console is via the console and from within this directory. There is a "script" in this directory that we can execute on the terminal.  Type `./run` and wait for the mini console to appear on the screen again.
<div style="width:75%; margin:auto">
	<img src="figs/raspberry_pi_run_mini_console4.png"/>
</div>
<br>

You may have noticed we use Terminal a lot within this project. If everything on this page is complete, go to the 'Terminal Basics' link in the navigation menu to continue with the workshop's day 1 tasks and learn more about terminal. 
 