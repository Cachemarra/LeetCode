#%% Half pyramid.

def pyramid(num: int, justify: str='left') -> None:
    '''
    Print a half pyramid with the indicated justification.
    :param: num: int. The number of rows to print.
    :param: justify: str. The align of the pyramid. Values: [left, right]
    :return: None.
    '''
    # Inicialización de variables
    row = 0
    row_symbol = ''
    # Ciclo for para imprimir los renglones
    for i in range(num):
        row = i + 1
        
        # asignamos el valor al renglon
        if row != 1:
            row_symbol += '*'
            
        else:
            row_symbol = '*'
        
        # Imprimimos el renglon
        if justify == 'right':
            print(row_symbol.rjust(num))
        else:
            print(row_symbol)


#%% Funcion principal
if __name__ == '__main__':
    # Test cases
    for i in range(8):
        print(f'Test case {i+1}:')
        pyramid(i+1, 'right')
        print('')
