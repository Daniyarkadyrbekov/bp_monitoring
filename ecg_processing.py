from biosppy import storage
from biosppy.signals import ecg
from processing import *

sig1, sig2 = read_file('Temirlan5.txt')


signal = sig2

out = ecg.ecg(signal=signal, sampling_rate=300., show=True)

rp = ecg.engzee_segmenter(signal=signal, sampling_rate=300.0, threshold=0.48)

print(rp)