
import numpy as np
import matplotlib.pyplot as plt
import time



def exp():
    with plt.ion():
        fig = plt.figure(figsize=(2,2), dpi=300)
        ax = fig.add_axes([0, 0, 0.92, 0.8])
        # ax = fig.add_subplot(1, 1, 1)
        x = np.linspace(0, 10.0*np.pi, num=1000)
        y = np.sin(x)
        ax.set_ylim(1.5)
        line, = ax.plot(x, y)
        fig.show()
        time.sleep(10)

def plot():
    exit(100)


if __name__ == '__main__':
    exp()

