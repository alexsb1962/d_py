#! utf-8


import sys,os
import time 

print('hello!',' os=',os.name)
class parent(object):
    a=0
    b=0
    def __init__(self):
        self.a=1
        self.b=2
    def method1(self):
        self.a=3
        return(5)
        
class children(parent):
        def __init__(self):
            parent.__init__(self)
            self.b=5
        def mmethod1(self):
            parent.method1(self)
            self.b=6
            return(self.b)
            
def wait1sec():
    stime=time.perf_counter()
    ctime=stime
    while (ctime-stime)<1:
        ctime=time.perf_counter()
    return(ctime-stime)        
    
ex=parent()
exc=children()
    
for i in range(3):
    s=time.perf_counter()
    time.sleep(1.0)
    print(time.perf_counter()-s)
    