'''
There is a series, S, where the next term is the sum of pervious three terms. Given the first three terms of the series, a, b, and c
respectively, you have to output the nth term of the series using recursion.

Recursive method for calculating nth term is given below.

    S(n) = { a  if n=1
             b  if n=2
             c  if n=3
             S(n-1) + S(n-2) + S(n-3) Otro caso 
    }

'''

#%% Método función sobre recursión
def solucion(n, a, b, c):

    result = 0

    # Creamos un switch case falso en python
    case = {1: a,
            2: b,
            3: c
    }

    # Si n es menor a 4 regresamos inmediatamente el resultado
    if n < 4:
        return case[n]
    
    else:
        for i in range(1, 4):
            result += solucion(n-i, a, b, c)
        
    return result


#%% Probamos el método
if __name__ == '__main__':
    ''' Pruebas
    
    n = 5; a, b, c = (1, 2, 3); result = 11

    n = 4; a, b, c = (1, 1, 1); result = 3

    n = 3; a, b, c = (4, 6, 8); result = 8

    n = 5; a, b, c = (46, 68, 100); result = 382
    '''

    # Probamos el método
    n = 5
    a, b, c = (46, 68, 100)

    resultado = solucion(n, a, b, c)

    print(resultado)


