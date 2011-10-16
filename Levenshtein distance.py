# -*- coding: utf-8 -*-

from sys import argv
import codecs



def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    lines = []
    for line in f:
        line = line.replace('\n','')
        line = line.lower()
        lines.append(line)
    print lines[0],lines[1]


if __name__ == "__main__":
    main(argv)