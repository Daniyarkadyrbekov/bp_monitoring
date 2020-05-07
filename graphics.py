import numpy as np
import biosppy
from matan import *

sig1, sig2 = read_file('Temirlan6.txt')

out = biosppy.signals.ecg.ecg(signal=sig2, sampling_rate=300.0, show=False)
ecg_peaks_ind, ecg_peaks = get_indices_of_R_peaks(out[1])

new_ppg = invertation(np.array(sig1[:len(sig1)]))
new_ppg = butter_bandpass_filter(new_ppg, 0.1, 5, 300, 3)
ppg_x, ppg_y = ppg_sistolic_peaks(new_ppg)
ppg_sist_peaks, ppg_sist_ind = top_peaks(ppg_y, ppg_x)
time_new_ppg = np.linspace(0, (len(new_ppg)/300), len(new_ppg))

peaks_min_ind, peaks_min = ppg_min_peaks(new_ppg)
ppg_min, ppg_min_peaks_ind = top_min_peaks(peaks_min, peaks_min_ind)



time_new = np.linspace(0, (len(new_ppg)/300), len(new_ppg))

a = np.array(range(len(sig2)))
b = out[1]

y = np.array(new_ppg[:len(new_ppg)])

plt.xlabel('Номер отсчета')
plt.ylabel('Амплитуда, у.е.')
plt.title('Синхронная регистрация сигналов')
plt.plot(a, b)
plt.plot(a, y)
plt.plot(ppg_sist_ind, ppg_sist_peaks, 'o')
# plt.plot(ppg_min_peaks_ind, ppg_min, 'o')
plt.plot(ecg_peaks_ind, ecg_peaks, 'o')
plt.show()

