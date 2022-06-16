import matplotlib.pyplot as plt
import matplotlib.axes as axes
from matplotlib.lines import Line2D
import matplotlib.gridspec as gridspec
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
        return

    x = filldata(0, 24 * np.pi, 512)
    y = np.sin(x)

    def fftlog(x):
        window = 0.5*(1+np.sin(filldata(-np.pi/2, np.pi*3/2, len(x))))
        _ = np.abs(np.fft.rfft(x*window))
        return np.log10(_)

    fg = plt.figure(figsize=(20, 6), constrained_layout=True)
    gs = fg.add_gridspec(2, 2)
    ax1 = fg.add_subplot(gs[0, :])
#    line1, = ax1.plot(x, y)  # plot возвращает список. Запятая заствляет распаковать его
    line1 = ax1.plot(x, y)[0]  # аналог
    ffty = fftlog(y)
    fftx = np.linspace(0, len(ffty)-1, len(ffty))
    ax2 = fg.add_subplot(gs[1, :])
    ax2.set_xlim(0, 50)
    ax2.set_ylim(0, ffty.max())
    ax2.bar(fftx, ffty)
    plt.ion()

    top = 1.0,
    bottom = 0.045,
    left = 0.04,
    right = 0.985,
    hspace = 0.1,
    wspace = 0.2

    def update(i):
        y = np.sin((i + 1) / 30. * x)
        line1.set_data(x, y)
        y2 = fftlog(y)
        line2.set_data(range(len(y2)), y2)

    # ani = matplotlib.animation.FuncAnimation(fg, update, frames=60, repeat=True)

    plt.ioff()
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



if __name__ =='__main__':
    ex1()
