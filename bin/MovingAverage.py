###############################################################################
# Python Script to Calcualte Moving Average
###############################################################################
# Written by Mario Muscarella
# Last Update 22 Mar 2019

# Directions:

import numpy
from numpy import convolve, ones, linspace

def movingaverage(data_in, window_size):
	window = numpy.ones(int(window_size))/float(window_size)
	return numpy.convolve(data_in, window, 'same')
