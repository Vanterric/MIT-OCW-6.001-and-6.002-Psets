# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:08:43 2020

@author: derri
"""

import pylab
x = [1,2,3,4,5]
y = [2,4,6,8,10]
pylab.plot(x,y)
pylab.plot(y,x)
pylab.title('test')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.show()