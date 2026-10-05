#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graph as gr
import math
import numpy

def divided_differences(xn, yn):
    
    n = len(xn)
    div = yn
    div.reverse()
    xn.reverse()
    for i in xrange(n-1):
        i += 1
        for j in xrange(n-i):
            div[j] = (div[j] - div[j+1]) / (xn[j] - xn[j+i])
    
    div.reverse()
    xn.reverse()
    return div
    
def evaluation(div, x, xn):
    
    poly = 0
    n = len(div)
    for i in xrange(n):
        prod = 1
        for j in xrange(i):
            prod = prod*(x - xn[j])
        poly = poly + (div[i])*prod
       
    return poly
 
def sin(x):
    return math.sin(x)
    
def get_eval(x):
    return evaluation(divg, x, xng)
    
   
def main():
    global xng; xng = numpy.linspace(0, 2*math.pi, 50)
    xng = [i for i in xng]
    yn = [sin(i) for i in xng]
    global divg; divg = divided_differences(xng, yn)
    gr.fonction(sin, 0, 2*math.pi)
    gr.fonction(get_eval, 0, 2*math.pi, 50)
    gr.save("question3")
if __name__ == "__main__":
    main()