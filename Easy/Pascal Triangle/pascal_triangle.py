#%% Importación de librerias.
from math import factorial

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # If just want the first column return a 1
        if numRows == 1:
            return [[1]]
        
        # For other number of rows
        else:
            if numRows == 2:
                return [[1], [1, 1]]
            else:
                answer = [[1], [1, 1]] # The first two columns
                items = 2
                for i in

            row_ans = [1]

        # I'll use the formula to calculate the value
        pascal_val = lambda r, c: int(factorial(r) / (factorial(c) * factorial(r - c)))



        return 


# ------------------------- Pruebas
# Test
if __name__ == '__main__':
    # Asignamos el número de pruebas a realizar y el valor de renglon máximo permitido.
    num_tests = 10
    renglon_maximo = 10
    imprimir = True # Imprimir en pantalla
    init_0 = False  # Envolver en 0s.

    # Creamos conjuntos de pruebas.
    # Por comodidad solo elegiremos renglones del 0 al 10
    rows = [np.random.randint(0, renglon_maximo) for i in range(num_tests)]
    columns = []
    for i in rows:
        if i == 0:
            columns.append(0)
        else:
            columns.append(np.random.randint(0, i/2 + 1))

    # Creamos una función para obtener el valor de una celda en la posición ROW, COLUMN
    pascal_val = lambda r, c: int(factorial(r) / (factorial(c) * factorial(r - c)))
    # Obtenemos el valor de x celda del triangulo de pascal.
    answers = list(map(pascal_val, rows, columns))

    # Realizamos un test para comprobar el buen funcionamiento.
    passed = 0 # Variable para tener un conteo de los examenes aprobados.

    for i in range(len(rows)):
        print(f'Prueba {i} '.center(40, '-'))
        print(f'Row: {rows[i]}, Colum: {columns[i]}')
        
        # Obtenemos el resultado de nuestra funcion
        valor_celda = pascal(rows[i], columns[i], imprimir=imprimir, init_0=init_0)
        print(f'Respuesta esperada: {answers[i]} <-> Respuesta obtenida: {valor_celda}\n ')

        if answers[i] == valor_celda:
            passed += 1
    
    # Obtenemos la calificación del sistema.
    calificacion = (passed / num_tests) * 100
    print(f'\nLa función paso {passed} pruebas de {num_tests}.')
    print(f'Calificación: {calificacion}')

