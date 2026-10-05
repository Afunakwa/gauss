#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author Klein Nicolas, Roland Christophe

import matplotlib.pyplot as plot
import numpy
import math
import os

def suite(xn, logy = False, label = None, if_clear = False):
    """ Trace un graphe d'une suite de nombre
    @param xn: la liste des nombres à porter en graphe
    @param logy: boolean déterminant une échelle log ou non
    @param label: détermine le nom d'une courbe """
    
    plot.grid(True)
    if if_clear: plot.clf()
    
    n = range(len(xn))
    plot.plot(n, xn)
    
    if logy:
        plot.yscale('log')
        
    if label:
         plot.plot(n, xn, label = label)
    else:
         plot.plot(n, xn)

def fonction(f, x_min, x_max, label = None, n_points = 50, if_clear = False):
    """ Trace un graphe d'une fonction
    @param f: la fonction à porter en graphe
    @param x_min: borne inférieur du domaine de f représenté
    @param x_max: borne supérieur du domaine de f représenté
    @param label: détermine le nom d'une courbe """
    
    
    
    xn = numpy.linspace(x_min, x_max, n_points)
    
    list_x = []
    list_y = []
    if if_clear: plot.clf()
    plot.grid(True)
    for x in xn:
        y = f(x)
        list_x.append(x)
        list_y.append(y)
    
    if label:
        plot.plot(list_x,list_y, label = label)
    else:
        plot.plot(list_x, list_y)
     
        
def points(list_x, list_y, if_line = False, if_clear = False):
  
    plot.grid(True)
    
    if if_line:
	fig = plot.figure(1)
	if if_clear: fig.clf()
	plot.plot(list_x, list_y)
    else:
    
	fig = plot.figure(1)
	if if_clear: fig.clf()
    
	ax = fig.add_subplot(111)
	#ax.set_aspect(1)

	ax.scatter(list_x, list_y)
    
    

    
def save(name, extension = ".png"):
    print "Sauvegarde du fichier " + name + extension
    plot.savefig(name + extension)
