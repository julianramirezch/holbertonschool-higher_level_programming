#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)

    for i in range(len):
        cont = i

    if cont == 0:
        print('{} arguments.'.format(cont))
    elif cont == 1:
        print('{} argument:'.format(cont))
        print('{}: {}'.format(cont, argv[cont]))
    else:
        print('{} arguments:'.format(cont))
        for j in range(cont + 1):
            if j != 0:
                print('{}: {}'.format(j, argv[j]))
