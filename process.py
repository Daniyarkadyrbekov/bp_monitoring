from scipy.signal import correlate
import numpy as np
from matplotlib import pylab as plt
from scipy.signal import correlate
import math

def read_file(file_name):
    ch1 = []
    ch2 = []
    with open(file_name, 'r') as f:
        for row in f:
            row_str = row[:-1]
            row_splt = row_str.split('\t')
            ch1.append(float(row_splt[0]))
            ch2.append(float(row_splt[1]))
    offset = int(abs(len(ch1)-3000)/2)
    offset = 5
    return ch1[offset:-offset-1], ch2[offset:-offset-1]

sig1, sig2 = read_file('Deniska3.txt')

xs = []
sin_vals = []
cos_vals = []
x = 0.0
while x < 10.0:
	sin_vals += [math.sin(x)]
	cos_vals += [math.cos(x)]
	xs += [x]
	x += 0.1



cross_corr = correlate(sin_vals, cos_vals, 'full', 'direct')
shift = np.argmax(cross_corr) - len(sin_vals)
print(shift)


