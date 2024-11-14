#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import vivid7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

print("""Waveshare 7.3 inch e-Paper: Color Test

This script will display six colors on the screen in vertical sections.

""")

# Initialize the display
epd = epd7in3e.EPD()
epd.init()
epd.Clear()

# Define the colors based on the display's color capabilities
colors = [epd.RED, epd.BLACK, epd.YELLOW, epd.GREEN, epd.BLUE, epd.WHITE]
color_names = ["Red", "Black", "Yellow", "Green", "Blue", "White"]

# Create a new image to display all colors in separate sections
img = Image.new("RGB", (epd.width, epd.height), epd.WHITE)
draw = ImageDraw.Draw(img)

# Calculate the width of each color section
section_width = epd.width // len(colors)

# Draw each color in a vertical section
for i, color in enumerate(colors):
    x_start = i * section_width
    x_end = (i + 1) * section_width
    draw.rectangle((x_start, 0, x_end, epd.height), fill=color)
    draw.text((x_start + 10, 10), color_names[i], fill=epd.BLACK)  # Label each section

# Display the image
epd.display(epd.getbuffer(img))
print("Displaying six colors. Check the screen.")
time.sleep(10)  # Keep the image on the screen for 10 seconds

# Clear and put the display to sleep
epd.Clear()
epd.sleep()
print("Color test complete. Display cleared and put to sleep.")
