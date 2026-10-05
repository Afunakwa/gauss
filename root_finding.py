#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Nicolas Klein, Chistophe Roland

from __future__ import division
import graph as gr
import math

EPSILON = 10**(-9)
MAX_ITER = 100

class stop_condition:
    """ Classe qui permet à l'utilisateur de
    générer sa propre condition d'arrêt."""
    def __init__(self, max_iter = MAX_ITER, eps = EPSILON, delta = EPSILON):
        self.max_iter = max_iter
        self.eps = eps
        self.delta = delta
        
    def __call__(self, n, a, b, fx):
        if n >= self.max_iter or abs(a - b) <= self.eps or abs(fx) <= self.delta:
            return True
        return False

default_stop = stop_condition()

def bissection(f, a, b, if_list = False, stop = default_stop):
    """
    L'algorithme de bissection pour
    trouver une racine d'une fonction donnée dans un
    certain intervalle où la fonction change de signe

    @param f: fonction dont on calcule une racine
    @param a: borne inférieure
    @param b: borne supérieure
    @param if_list : boolean gérant l'envoie d'une liste ou non
    @param stop: critère d'arrêt
    @return: racine de la fonction ou suite des approx de la racine
    @author: Roland Christophe, Nicolas Klein"""
    
    if f(a) < 0:
        a, b = b, a
    elif f(a)*f(b) > 0:
        raise Exception("La fonction doit changer de signe")
    
    n = 0
    if if_list:
        racines = []
    fx = f((a + b)*0.5)
    
    while (not stop(n, a, b, fx)):
        x = (a + b)*0.5
        
        fx = f(x)
        if fx > 0:
            a = x
        elif fx < 0:
            b = x
        if if_list:
            racines.append(x)
        n += 1
    
    if if_list:
        return racines
    else:
        return x

def fausse_position(f, a, b, if_list = False, stop = default_stop):
    """
    L'algorithme de la fausse position pour
    trouver une racine d'une fonction donnée dans un
    certain intervalle où la fonction change de signe

    @param f: fonction dont on calcule une racine
    @param a: borne inférieure
    @param b: borne supérieure
    @param if_list : boolean gérant l'envoie d'une liste ou non
    @param stop: critère d'arrêt
    @return: racine de la fonction ou suite des approx de la racine
    @author: Roland Christophe, Nicolas Klein"""
    
    if f(a) < 0:
        a, b = b, a
    elif f(a)*f(b) > 0:
        raise Exception("La fonction doit changer de signe")

    fa = f(a)
    fb = f(b)
    fx = f(a - (fa*(b - a))/(fb - fa))
    n = 0
    
    if if_list:
        racines = []
    
    while (not stop(n, a, b, fx)):
        x = a - (f(a)*(b - a))/(f(b) - f(a))

        fx = f(x)
        if fx > 0:
            a = x
        elif fx < 0:
            b = x
        if if_list:
            racines.append(x)
            
        n += 1
        
    if if_list:
        return racines
    else:
        return x

def secante(f, a, b, if_list = False, stop = default_stop):
    """
    L'algorithme de sécante pour
    trouver une racine d'une fonction donnée dans un
    certain intervalle où la fonction change de signe

    @param f: fonction dont on calcule une racine
    @param a: borne inférieure
    @param b: borne supérieure
    @param if_list : boolean gérant l'envoie d'une liste ou non
    @param stop: critère d'arrêt
    @return: racine de la fonction ou suite des approx de la racine
    @author: Roland Christophe, Nicolas Klein"""
    
    if f(a) < 0:
        a, b = b, a
    elif f(a)*f(b) > 0:
        raise Exception("La fonction doit changer de signe")
    fa = f(a)
    fb = f(b)
    fx = f(b - fb * (b - a)/(fb - fa))

    n = 0
    if if_list:
        racines = []
        
    while (not stop(n, a, b, fx)):
        try:
            x = b - fb * (b - a)/(fb - fa)
            a = b
            b = x
            fb = f(b)
            fa = f(a)
        except ZeroDivisionError:
            raise Exception
        
        if if_list:
            racines.append(x)
        n += 1
        
    if if_list:
        return racines
    else:
        return x
    
def newton(x, f, df, if_list = False, stop = default_stop):
    """
    L'algorithme de Newton calculant la racine d'une fonction convexe
    en utilisant sa dérivée
    
    @param x: point d'où démarre l'algorithme, supposé proche de la racine
    @param f: fonction dont on calcule une racine
    @param df: dérivée de la fonction considérée
    @param if_list : boolean gérant l'envoie d'une liste ou non
    @param stop: critère d'arrêt
    @return: racine de la fonction ou suite des approx de la racine
    @author: Roland Christophe, Nicolas Klein"""
    
    fx = f(x)
    dfx = df(x)
    
    y = 0.
    n = 0
    
    if if_list:
        racines = []
    
    while (not stop(n, x, y, fx)):
        y = x
        try:
	    if fx == None: fx = 0.
            x -= fx/dfx
        except ZeroDivisionError:
            raise Exception
        fx = f(x)
        dfx = df(x)
        
        if if_list:
            racines.append(x)
        
        n += 1
    if if_list:
        return racines
    else:
        return x
    
def point_fixe(x, phi, if_list = False, stop = default_stop):
    """

    @param x: point d'où démarre l'algorithme, supposé proche du point fixe
    @param phi: fonction dont on cherche le point fixe
    @param if_list : boolean gérant l'envoie d'une liste ou non
    @param stop: critère d'arrêt
    @return: racine de la fonction ou suite des approx de la racine
    @author: Roland Christophe, Nicolas Klein"""
    
    phix = phi(x)
    y = 0.
    n = 0
    
    if if_list:
        racines = []
        
    while (not stop(n, x, y, phix)):
        y = x
        try:
            x = phi(x)
        except:
            raise Exception
        if if_list:
            racines.append(x)
        n+= 1
        
    if if_list:
        return racines
    else:
        return x
