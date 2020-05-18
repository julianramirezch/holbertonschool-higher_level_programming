#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        for i in range(x):
            print('{:d}'.format(my_list[i]), end='')
            cont += 1
        print('')
    except IndexError:
        print('')
    finally:
        return cont
