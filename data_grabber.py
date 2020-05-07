import serial
import time



def read_com_data_by_byte(work_port):
    while work_port.in_waiting == 0:
        pass

    answer = work_port.read(3)
    time.sleep(5)
    while answer[-3:] != b'end':
        while work_port.in_waiting == 0:
            pass
        answer += work_port.read()
    return answer

def data_parser(data):
    data_str = data.decode( 'utf-8')
    data_str = data_str[:-4]
    count_splt = data_str.split('|')
    ch1 = []
    ch2 = []
    for count in count_splt:
        ch_split = count.split('/')
        ch1.append(float(ch_split[0]))
        ch2.append(float(ch_split[1]))
    return ch1, ch2


def one_measurement_procedure(port):
    port.write(b'm')
    time.sleep(5)
    data = read_com_data_by_byte(port)
    channel1, channel2 = data_parser(data)
    return channel1, channel2


