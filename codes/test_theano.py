# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:54:02 2020

@author: dante
"""

import theano
from theano import tensor

a = tensor.dscalar()
b = tensor.dscalar()

c = a+b
# define a function that a and b as input, c as output
f = theano.function([a,b], c)
# f = theano.function([a,b], c)
# bind 1.5 to 'a', 2.5 to 'b',# bind 1.5 to a and 2.5 to b, and evaluate c
result = f(1.5, 2.5)
print(result)
