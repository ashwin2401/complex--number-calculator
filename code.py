# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers(object):

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return '0.00'
        if self.real == 0:
            return '%.2fi' % self.imag
        if self.imag == 0:
            return '%..2f' % self.real
        return '%.2f %s %.2fi' % (self.real,'+' if self.imag >= 0 else '-',abs(self.imag))                
    def __add__(self,other):
        a = self.real + other.real
        b = self.imag + other.imag
        return complex_numbers(a,b)
    
    def __sub__(self,other):
        c = self.real - other.real
        d = self.imag - other.imag
        return complex_numbers(c,d)
    
    def __mul__(self,other):
        e = self.real * other.real - self.imag * other.imag
        f = self.imag * other.real + self.real * other.imag
        return complex_numbers(e,f)
    
    def __truediv__(self,other):
        g = (self.real * other.real + self.imag * other.imag) / (other.real**2 +                        other.imag**2)
        h = (self.imag * other.real - self.real * other.imag) / (other.real**2 +                        other.imag**2)
        return complex_numbers(g,h)
    
    def absolute(self):
        a = math.sqrt(self.real**2 + self.imag**2)
        return a
    
    def argument(self):
        a = np.degrees(np.arctan(self.imag/self.real))
        return a

    def conjugate(self):
        a = self.real
        b = -self.imag
        return complex_numbers(a,b)


comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = complex_numbers.__add__(comp_1,comp_2)
comp_diff = complex_numbers.__sub__(comp_1,comp_2)
comp_prod = complex_numbers.__mul__(comp_1,comp_2)
comp_quot = complex_numbers.__truediv__(comp_1,comp_2)
comp_abs = complex_numbers.absolute(comp_1)
comp_conj = complex_numbers.conjugate(comp_1)
comp_arg = complex_numbers.argument(comp_1)

print(comp_arg)




