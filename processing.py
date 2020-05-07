
import numpy as np
from matplotlib import pylab as plt
from matan import *


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

sig1, sig2 = read_file('Temirlan5.txt')

new_ppg = invertation(np.array(sig1[:len(sig1)]))

x = np.arange(0, len(new_ppg))
y = np.array(new_ppg[:len(new_ppg)])

a = np.arange(0, len(sig2))
b = np.array(sig2[:len(sig2)])

# fig, ppg = plt.subplots()
# ppg.plot(x, -y)
# ppg.grid()
# ppg.set_xlabel('samples')
# ppg.set_ylabel('U, mV')
# plt.title('PPG')

# fig, ecg = plt.subplots()
# ecg.plot(a, b)
# ecg.grid()
# ecg.set_xlabel('samples')
# ecg.set_ylabel('U, mV')
# plt.title('ECG')
# print(len(sig1), len(sig2))

plt.plot(x, y)
plt.plot(a, b)

plt.show()



