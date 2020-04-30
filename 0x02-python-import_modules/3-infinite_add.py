#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)
    adds = 0

    for i in range(1, len):
        adds += int(argv[i])
    print('{}'.format(adds))
