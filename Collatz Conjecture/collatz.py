import random

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def collatz(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    return n


def conjecture(num):
    step_lst = [0]
    value_lst = [num]
    counter = 0
    while num != 1:
        counter += 1
        num = collatz(num)
        step_lst.append(counter)
        value_lst.append(num)
    # print(step_lst, value_lst)
    return step_lst, value_lst


if __name__ == "__main__":
    i = int(input("What's the number? : "))

    xpoints, ypoints = conjecture(i)

    red = random.random()
    blue = random.random()
    green = random.random()
    plt.plot(xpoints, ypoints, c=(red, blue, green))
    plt.show()
    # x = []
    # y = []
    #
    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 105)
    # ax.set_ylim(0, 105)
    # line, = ax.plot(0, 0)
    #
    #
    # def update(i):
    #     x.append(i * 100)
    #     y.append(i * 10)
    #
    #     line.set_xdata(x)
    #     line.set_ydata(y)
    #     return line
    # ani = FuncAnimation(fig, func=update, interval=100, blit=False)
    # plt.show()
