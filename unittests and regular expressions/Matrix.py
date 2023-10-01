# -*- coding: utf-8 -*-
import numpy.linalg
import numpy


class Matrix:
    def __init__(self, n, m):
        self.A = None
        if not isinstance(n, int) or not isinstance(m, int):
            raise TypeError("Wymiary macierzy powinny byc liczbami calkowitymi")
        elif n <= 0 or m <= 0:
            raise ValueError("Wymiary macierzy powinny byc dodatnie")
        else:
            self.n = n
            self.m = m
    
    def fill_matrix(self, *args):
        self.A = numpy.asarray(args).reshape(self.n, self.m)

