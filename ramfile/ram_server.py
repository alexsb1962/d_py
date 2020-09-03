#

import sys
import os
import mmap
import numpy as np
import scipy.fft


class FFTRamServer:
    def __init__(self,path='temp.ram',size=1024):
        self.fft_data=np.zeros(size,dtype=float)
        self.f =open(path,'r+b')
        self.map_obj=mmap.mmap(self.f.fileno(), sys.getsizeof(self.fft_data), access='w+b')

    def __del__(self):
        self.map_obj.flush()
        del(self.map_obj)
        self.f.close()
        del(self.fft_data)


def main():
    lendata = 10
    filename = 'temp.ram'
    data = np.zeros(lendata, float)
    f = open(filename, 'wb')
    dt = mmap.mmap(f.fileno(), sys.getsizeof(data))



if __name__ == "__main__":
    main()
else:
    pass
