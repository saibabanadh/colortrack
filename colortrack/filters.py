#!/usr/bin/env python

import numpy as np
import cv2
# TODO import argparse?

def color_filter(image, lower=[0, 0, 0], upper=[255, 255, 255]): 
    """Filter image for a range of colors. Return pixels matching the color criteria unaffected; 
    return other pixels as RGB 0,0,0. Returns color-adjusted input and output images. Function
    accepts all pixels by default, but can be adjusted by changing  BGR (blue-green-red) values 
    in upper and lower.
    """
    # generate mask. a blue value of 80 captures most bright blues in the mask.
    array_lower = np.array(lower, dtype = "uint8")
    array_upper = np.array(upper, dtype = "uint8")
    color_mask = cv2.inRange(image, array_lower, array_upper)

    # filter image with mask and change color mapping to RGB.
    output = cv2.bitwise_and(image, image, mask = color_mask)
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    return(output_rgb) 

def blue_filter(image, blue_lower=[80, 60, 0], blue_upper=[255, 255, 100]):
    """A convenience function to pick out bright blue/cyan pixels."""
    output_rgb = color_filter(image, lower=blue_lower, upper=blue_upper)
    return(output_rgb)
