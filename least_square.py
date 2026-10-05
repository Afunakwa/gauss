#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gauss as gs

def least_square_lin(xn, yn, w):
    if len(xn) != len(yn):
        raise Exception("Les listes sont de tailles différentes")
    
    n = len(xn)
    
    sum_x, sum_y, sum_x2, sum_xy, sum_w = 0, 0, 0, 0, 0
    
    for i in xrange(n):
        w_x = w(xn[i])
        sum_x += xn[i] * w_x
        sum_y += yn[i] * w_x
        sum_x2 += xn[i]**2 * w_x
        sum_xy += xn[i]*yn[i] * w_x
        sum_w += w_x
        
    det = sum_x2 * sum_w - sum_x**2

    if det == 0:
        if n == 1:
            raise Exception("On a une infinité de solutions")
        else:
            raise Exception("La solution est une droite verticale")
        
    a = (sum_xy * sum_w - sum_x * sum_y)/det
    b = (sum_x2 * sum_y - sum_xy * sum_x)/det
    
    return (a, b)

def least_square_alt(xn, yn, w):
    if len(xn) != len(yn):
        raise Exception("Les listes sont de tailles différentes")
    
    n = len(xn)
    
    sum_x, sum_d_yx, sum_x2, sum_xy, sum_, sum_w = 0, 0, 0, 0, 0, 0
    
    for i in xrange(n):
        w_x = w(xn[i])
        sum_x += xn[i] * w_x
        sum_d_yx += yn[i]/xn[i] * w_x
        sum_x2 += xn[i]**2. * w_x
        sum_xy += xn[i]*yn[i] * w_x
        sum_ += 1/xn[i]**2. * w_x
        sum_w += w_x
        
    det = sum_x2 * sum_ - sum_x*sum_w

    if det == 0:
        if n == 1:
            raise Exception("On a une infinité de solutions")
        else:
            raise Exception("La solution est une droite verticale")
        
    a = (sum_xy * sum_ - sum_x * sum_d_yx)/det
    b = (sum_x2 * sum_d_yx - sum_xy * sum_w)/det
    
    return (a, b)
    
def leat_square_quad(xn, yn, w):
    if len(xn) != len(yn):
        raise Exception("Les listes sont de tailles différentes")
    
    n = len(xn)
    
    sum_x, sum_x_2, sum_x_3, sum_x_4, sum_y, sum_y_x, sum_y_x_2, sum_w = 0, 0, 0, 0, 0, 0, 0, 0
    
    for i in xrange(n):
        w_x = w(xn[i])
        sum_x += xn[i] * w_x
        sum_x_2 += xn[i]**2. * w_x
        sum_x_3 += xn[i]**3. * w_x
        sum_x_4 += xn[i]**4. * w_x
        sum_y += yn[i] * w_x
        sum_y_x += yn[i] * xn[i] * w_x
        sum_y_x_2 += yn[i] * xn[i]**2. * w_x
        sum_w += w_x

    f = [sum_x_4, sum_x_3, sum_x_2]
    g = [sum_x_3, sum_x_2, sum_x]
    h = [sum_x_2, sum_x, sum_w]
    matrice = [f, g, h]
    vecteur = [sum_y_x_2, sum_y_x, sum_y]
    
    return gs.gauss_partiel(matrice, vecteur)
