#!/usr/bin/python3
# coding=utf-8

"""
A python module to draw ascii line chart in terminal
By : https://jeffprod.com - https://twitter.com/jeffprod
"""

class Graph:

    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            self.data = []
        self.nb_rows = 50
        self.nb_cols = 160
        self.dot = '+'

    def addData(self, val):
        self.data.append(val)

    def setRows(self, nb):
        self.nb_rows = nb

    def setCols(self, nb):
        self.nb_cols = nb

    def setDot(self, char):
        self.dot = char

    def draw(self):
        maxY = max(self.data)
        minY = min(self.data)
        scaleY = (maxY - minY) / self.nb_rows
        xdata = self.data[-self.nb_cols:]
        self.data = xdata
        yval = maxY
        cpt = self.nb_rows
        while cpt>0:
            print("%.2f" % yval, end= ' ')
            for xval in xdata:
                if xval>=yval:
                    print('\033[01;33m' + self.dot + '\033[00m', end='')
                else:
                    print(' ', end='')
            print()
            yval = yval - scaleY
            cpt = cpt - 1


if __name__ == "__main__":

    graph = Graph([0.8251, 0.8254, 0.8253, 0.8254, 0.8253, 0.8253, 0.8253, 0.8254, 0.8254, 0.8254, 0.8254, 0.8254, 0.8251, 0.826, 0.826, 0.826, 0.826, 0.824, 0.824, 0.8245, 0.8258, 0.8258, 0.826, 0.825, 0.8253, 0.8255, 0.827, 0.8272, 0.829, 0.83, 0.8301, 0.829, 0.8291, 0.8291, 0.8272, 0.8272, 0.8272, 0.8266, 0.8269, 0.8269, 0.8285, 0.828, 0.8269, 0.8285, 0.83, 0.8317, 0.8321, 0.8345, 0.8353, 0.8345, 0.8348, 0.8321, 0.8324, 0.8323, 0.8325, 0.8331, 0.8336, 0.8336, 0.8342, 0.8345, 0.835, 0.835, 0.836, 0.8343, 0.834, 0.8341, 0.8341, 0.8341, 0.8342, 0.835, 0.835, 0.836, 0.8362, 0.8358, 0.839, 0.8353, 0.836, 0.8362, 0.84, 0.838, 0.838, 0.838, 0.838, 0.8383, 0.8381, 0.837, 0.837, 0.837, 0.8371, 0.8371, 0.837, 0.837, 0.8372, 0.8311, 0.8325, 0.832, 0.832, 0.832, 0.832, 0.832, 0.83, 0.83, 0.8312, 0.8317, 0.8317, 0.83, 0.8301, 0.83, 0.83, 0.83, 0.83, 0.8302, 0.8301, 0.8302, 0.83, 0.83, 0.83, 0.83, 0.829, 0.8258, 0.826, 0.8252, 0.825, 0.8232, 0.8239, 0.8232, 0.8241, 0.8243, 0.825, 0.8253, 0.8255, 0.824, 0.8228, 0.8222, 0.8221, 0.822, 0.822, 0.8205, 0.82, 0.8186, 0.8129, 0.813, 0.8136, 0.814, 0.8111, 0.8113, 0.8113, 0.8101, 0.81, 0.812, 0.811, 0.8108, 0.8111, 0.812, 0.8087, 0.8102, 0.81, 0.8095, 0.8103, 0.812, 0.812, 0.8102, 0.8077, 0.8077, 0.8064, 0.8055, 0.8061, 0.806, 0.8065, 0.805, 0.8067, 0.8058, 0.805, 0.805, 0.806, 0.8063, 0.812, 0.8112, 0.8112, 0.811, 0.81, 0.8085, 0.8086, 0.8086, 0.806, 0.806, 0.806, 0.805, 0.8037, 0.804, 0.8015, 0.8, 0.8, 0.7954, 0.7934, 0.7901, 0.7905, 0.791, 0.7905, 0.7906, 0.7906, 0.791, 0.7905, 0.79, 0.7911])
    graph.setCols(205)
    graph.setRows(50)
    graph.setDot('|')
    graph.draw()