#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv)

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        # script name
        name = argv[0]
        # 1 argument
        a = int(argv[1])
        # operator +,-,*,/
        opr = argv[2]
        # 2argument
        b = int(argv[3])

        if opr != '+' and opr != '-' and opr != '*' and opr != '/':
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
        elif opr == '+':
            res = add(a, b)
        elif opr == '-':
            res = sub(a, b)
        elif opr == '*':
            res = mul(a, b)
        else:
            res = div(a, b)
        print('{} {} {} = {}'.format(a, opr, b, res))
