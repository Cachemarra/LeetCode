#%% Def function of the full pyramid script
def pyramid(n: int) -> None:
    """
    Print a full pyramid based on the n number of rows.
    :param: n: int. Number of rows of the pyramid.
    :return: None.
    """
    # Iterate over the number of rows
    row = 0
    actual_row = ''

    for i in range(n):
        row += 1
        if row != 1:            
            actual_row = '*' * (2 * row-1)
            actual_row = actual_row.center(n*2, ' ')
            print(actual_row)
            
        else:
            print('*'.center(n*2, ' '))


#%% Main func
if __name__ == '__main__':

    for i in range(5):
        print(f'Test case {i}')
        pyramid(i+1)
        print('\n')
