#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3e
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
print("""Waveshare 7.3 inch e-Paper: Clean

Displays solid blocks of color to clean the display of any ghosting or residual colors.

""")

# Initialize the display
epd = epd7in3e.EPD()
epd.init()

# Command line arguments to determine number of cycles to run
parser = argparse.ArgumentParser()
parser.add_argument("--number", "-n", type=int, required=False, help="number of cycles")
args, _ = parser.parse_known_args()

# Set the number of cycles to run
cycles = args.number if args.number else 3

# Define the colors based on the display's color capabilities
colors = [epd.RED, epd.BLACK, epd.YELLOW, epd.GREEN, epd.BLUE, epd.WHITE]
color_names = ["Red", "Black", "Yellow", "Green", "Blue", "White"]

# Run the cleaning cycles
for i in range(cycles):
    print(f"Starting cleaning cycle {i + 1}\n")
    for color, color_name in zip(colors, color_names):
        print(f"- Updating with {color_name}")
        
        # Create a new image filled with the current color
        img = Image.new("RGB", (epd.width, epd.height), color)
        
        # Display the image on the e-ink display
        epd.display(epd.getbuffer(img))
        time.sleep(2)  # Pause to allow the color to fully display
    
    print("\nCycle complete!\n")

# Clear and put the display to sleep
print("Cleaning complete! Clearing and putting the display to sleep.")
epd.Clear()
epd.sleep()
