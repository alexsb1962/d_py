import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.animation
import numpy as np

# перебираем возможные backend
gui_env = ['Qt5Agg', 'GTKAgg', 'TKAgg', 'WXAgg']
for gui in gui_env:
    try:
        print ("testing", gui)
        matplotlib.use(gui, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
    else:
        print("Not found backend for GUI. Terminate program ")
        exit(1)
print ("Using:", matplotlib.get_backend())



def ex1():

    def filldata(start, end, num):
        _ = np.linspace(start, end-end/(num-1), num)
        return _

    x = filldata(0, 24 * np.pi, 512)
    y = np.sin(x)

    def fftlog(x):
        window = 0.5*(1+np.sin(filldata(-np.pi/2, np.pi*3/2, len(x))))
        _ = np.abs(np.fft.rfft(x*window))
        return np.log10(_)

    fig, (ax1, ax2) = plt.subplots(nrows=2)
    line1, = ax1.plot(x, y)
    ffty = fftlog(y)
    fftx=np.linspace(0, len(ffty)-1, len(ffty))
    line2, = ax2.plot(fftx,ffty)
    ax2.set_xlim(0, 50)
    ax2.set_ylim(0, ffty.max())


    def update(i):
        y = np.sin((i + 1) / 30. * x)
        line1.set_data(x, y)
        y2 = fftlog(y)
        line2.set_data(range(len(y2)), y2)

    ani = matplotlib.animation.FuncAnimation(fig, update, frames=60, repeat=True)
    plt.show()


def ex2():
    x = [1, 1]
    y = [1, 2]

    fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, sharey=True)
    line1, = ax1.plot(x)
    line2, = ax2.plot(y)
    ax1.set_xlim(-1, 17)
    ax1.set_ylim(-400, 3000)
    plt.ion()

    for i in range(150):
        x.append(x[-1] + x[-2])
        line1.set_data(range(len(x)), x)
        y.append(y[-1] + y[-2])
        line2.set_data(range(len(y)), y)

        plt.pause(0.1)

    plt.ioff()
    plt.show()

class ForWith():

    def __init__(self):
        self.data='проинициализирован'
        print(self.data)

    def __enter__(self):
        print('enter........')
        return self

    def __exit__(self, type, value, tb):
        print('exit.....')
        # например файл бы закрыл здесь

    def __del__(self):
        print('вызван __del__')

def ex3():
    with ForWith() as d:
        print('with')
        print(d.data)

    print(d.data)


if __name__ =='__main__':
    ex1()



