#!/usr/bin/python

# Create a text file with the output coming from Gemini API

# Create a function  that check for the file on the directorys
import glob
import os

current_dir = os.getcwd()
local_dir = glob.glob(current_dir + "/*.py")

print(local_dir)

print(os.listdir())