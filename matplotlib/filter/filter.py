import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def construct():
    b = signal.iirfilter(2, Wn=0.2, rp=5, rs=40, btype='lowpass', ftype='ellip')#, output='sos' )
    w, h = signal.freqz(b, a)
    plt.title('Digital filter frequency response')
    plt.plot(w, 20*np.log10(np.abs(h)))
    plt.title('Digital filter frequency response')
    plt.ylabel('Amplitude Response [dB]')
    plt.xlabel('Frequency (rad/sample)')
    plt.grid()
    plt.ion()
    plt.show()


if __name__ == "__main__":
    construct()