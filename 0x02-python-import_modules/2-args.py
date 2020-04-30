#!/usr/bin/python3
import sys
len = len(sys.argv)

for i in range(len):
    cont = i

if cont == 0:
    print('{} arguments.'.format(cont))
elif cont == 1:
    print('{} argument:'.format(cont))
    print('{}: {}'.format(cont, sys.argv[cont]))
else:
    print('{} arguments:'.format(cont))
    for j in range(cont):
        if j != 0:
            print('{}: {}'.format(j, sys.argv[j]))
