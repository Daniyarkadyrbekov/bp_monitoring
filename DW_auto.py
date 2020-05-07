from data_grabber import *
from file_saver import *
import numpy as np
from matplotlib import pylab as plt
import time
import os

ser = serial.Serial('COM4', 115200)
time.sleep(5)
ser.write(b'i')
time.sleep(5)
answer = ser.read(10)
if answer == b'contactyes':
	print('Contact is done!')

	


for chelovek in range(1, 20):
    print("Name: ")
    folder_name = input()
    folder_name = "./" + folder_name
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


    fileName = folder_name + "/" + folder_name + ".txt"
    sig1, sig2 = one_measurement_procedure(ser)
    write_file(fileName, sig1, sig2)

    sig1, sig2 = read_file(fileName)
    x = np.arange(0, len(sig1))
    y = np.array(sig1[:len(sig1)])
    plt.plot(x, y)
    plt.show()

    a = np.arange(0, len(sig2))
    b = np.array(sig2[:len(sig2)])
    plt.plot(a, b)
    plt.show()

   
    


