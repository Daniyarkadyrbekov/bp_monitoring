from matan import *
import os
folders = ['Temirlan', 'Angelina', 'Lev', 'Sofa', 'Deniska', 'Yarik', 'Lera', 'Dimon']
BP = ['130', '100', '120', '110', '120', '100', '110', '110']
i = 0
for folder in folders:
    pressure = BP[i]
    print(folder)
    with open(folder + '_summary' + '.txt', 'w') as f:
        for file in os.listdir(folder):
            # print(os.path.abspath(folder))
            print(file)
            print('GOOD JOB !!!')
            # path = os.path.(folder)
            sig1, sig2 = read_file('.\\' + folder + '\\' + file)
            new_ppg = invertation(np.array(sig1[:len(sig1)]))
            ppg_x, ppg_y = ppg_sistolic_peaks(new_ppg)
            ppg_sist_peaks, ppg_sist_ind = top_peaks(ppg_y, ppg_x)
            ecg_peaks_ind, ecg_peaks = get_indices_of_R_peaks(sig2)
            shift = get_shift_by_peaks(ecg_peaks, ppg_sist_peaks, 300)
            beats = BPM_calculation(new_ppg)
            attitude = get_attitude(new_ppg)
            row = str(shift) + '\t' + str(beats) + '\t' + str(attitude) + '\t' + pressure + '\r'
            f.write(row)
        i += 1   
                          


         


