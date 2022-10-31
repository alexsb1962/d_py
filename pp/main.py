import numpy as np
import math
import turtle

class BiFilter:

    def __init__(self, b: np.ndarray=[1.0, 0.0, 0.0], a: np.ndarray=[1.0, 0.0, 0.0], gain: float=1):
        self.a = a
        self.b = b
        self.gain = gain
        self._reset_filter = True
        self._in = np.array([0.0, 0.0, 0.0])
        self._out = np.array([0.0, 0.0, 0.0])

    def reset(self):
        self._reset_filter = True
        for i in range(0, 3):
            self._in[i] = 0
            self._out[i] = 0

    def sample(self, s):
        self._reset_filter = False

        part_sum = self.b[2] * self._in[2]; self._in[2] = self._in[1]
        part_sum += self.b[1] * self._in[1]; self._in[1] = self._in[0]
        self._in[0] = s * self.gain
        part_sum += self.b[0] * self._in[0];

        part_sum -= self.a[2] * self._out[2]; self._out[2] = self._out[1]
        part_sum -= self.a[1] * self._out[1]; self._out[1] = self._out[0]
        part_sum -= self.a[0] * self._out[0]; self._out[0] = part_sum
        return part_sum


def main():



    f0 = BiFilter(b=np.array([0.1, 0.0 , 0.0 ]),
                  a=np.array([-0.9, -0.0, 0.0]),  gain=1)
    f0.reset()

    for i in range(0,100):
        part0 = f0.sample(1.0)
        print(f"part0={part0}    i={i}")

#        part1 = f1.sample(part0,nom[2,0])
#        print(f"part1={part1}    w/g={part1*nom[2,0] }")




if __name__ == '__main__':
    main()
