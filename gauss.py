EPSILON = 2**-10

def affiche(m):
    n = len(m)
    for k in xrange(n):
        print m[k]

def gauss_partiel(matrice, vecteur):
    n = len(matrice)
    
    for j in xrange(n):
        maximum = 0
        for i in xrange(j, n):
            if abs(matrice[i][j]) > maximum:
                maximum = abs(matrice[i][j])
                pivot = i

        if maximum < EPSILON:
            raise Exception

        matrice[pivot], matrice[j] = matrice[j], matrice[pivot]
        vecteur[pivot], vecteur[j] = vecteur[j], vecteur[pivot]

        for i in xrange(j+1, n):
            t = matrice[i][j]/matrice[j][j]
            for l in xrange(j, n):
                matrice[i][l] -= matrice[j][l]*t
            vecteur[i] -= vecteur[j]*t
    
    sol = [None]*n
    i = n - 1
    while i >= 0:
        somme = 0
        for j in xrange(i+1, n):
            somme += matrice[i][j]*sol[j]
        sol[i] = (vecteur[i] - somme)/matrice[i][i]
        i -= 1
        
    return sol

def gauss_total(matrice, vecteur):
    
    n = len(matrice)
    b = range(n)
    for j in xrange(n - 1):
        maximum = 0
        for i in xrange(j, n):
            for k in xrange(j, n):
                if abs(matrice[i][k]) > maximum:
                    maximum = abs(matrice[i][k])
                    pvt = (i, k)
        #print pvt, matrice
        
            if maximum < EPSILON:
                raise Exception

        matrice[pvt[0]], matrice[j] = matrice[j], matrice[pvt[0]]
        vecteur[pvt[0]], vecteur[j] = vecteur[j], vecteur[pvt[0]]
        b[pvt[1]], b[k] = b[k], b[pvt[1]]

        for i in xrange(j+1, n):
            t = matrice[i][b[j]]/matrice[j][b[j]]
            for l in xrange(j, n):
                if matrice[j][b[j]]!= 0:
                    matrice[i][b[l]] -= matrice[j][b[l]]*t
            vecteur[i] -= vecteur[j]*t

    sol = [None]*n
    i = n-1
    while i >= 0:
        inte = 0.
        for j in xrange(i+1, n):
            inte += matrice[i][b[j]]*sol[b[j]]
        x = (vecteur[i] - inte)/matrice[i][i]
        sol[i] = x
        i -= 1
    return sol
