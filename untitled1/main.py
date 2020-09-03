
# изучаем matplotlib

import PlotThread
from matplotlib import pyplot as plt


import numpy as np
import threading as th
import time


fig,ax=plt.subplots()  # один график по умолчанию?
plt.ion()

Sema=th.BoundedSemaphore()
StopEvent=th.Event()

def ThreadPlt():
    print('Start of Thread')
    x = np.linspace(0, 2, 100)

    ax.plot(x, x + 1, label='Добавка')

    plt.plot(x, x, label='linear')
    plt.plot(x, x ** 2, label='quadratic')
    plt.plot(x, x ** 3, label='cubic')
    plt.plot(x, np.sin(x * 10), label='sin')

    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()

    Sema.release()

    kstart=0.1;  kend=1; kdelta=0.01; kdelay=0.2
    k=kstart
    while True:
        plt.plot(x,np.sin(x*10)*k) #создает новую линию графика
        k += kdelta
        if k>kend :
            k=kstart
        time.sleep(kdelay)
        if  StopEvent.isSet():
            break



# похоже, что show можно запускать только в основном потоке
plt.show()

StopEvent.clear()
Sht=th.Thread( target=ThreadPlt )
Sema.acquire()
Sht.start()
#ждем семафора от запущеного потока
Sema.acquire()

Sht.join(10.0)
if Sht.is_alive():
    print('поток не остановлен');

# сигнал на остановку потока
StopEvent.set()
Sht.join(5.0)
if Sht.is_alive():
    print('поток не остановлен');

# plt.show()
print('End of program')