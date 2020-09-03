# -*- coding: utf8 -*-

import time
import sys
import random
from collections import deque


class Cashe:
    def __init__(self,maxlen=0):
        self.cashe_mem={None:None}
        self.maxlen=maxlen

    def reset(self):
        self.cashe_mem={None:None}

    def get(self,fun,arg):
        if arg in self.cashe_mem:
            result=self.cashe_mem[arg]
        else:
            result=fun(arg)
            if len(self.cashe_mem)>=self.maxlen:
                self.cashe_mem.popitem()
            self.cashe_mem[arg]=result


def main():
    pass

def func(arg):
    time.sleep(0.1)
    return(arg+0.1)

def test():
    numb_of_cashe=0

    for i in range(10000):
        t=time.time()
        arg=random.randint(0, 1000)
        res=func(arg)
        if time.time()-t <0.05:
            print("Cashed: ",arg)
            numb_of_cashe+=1
    print('Total=',numb_of_cashe)



if __name__=="__main__":
    main()
