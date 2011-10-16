# -*- coding: utf-8 -*-

from sys import argv
import codecs

def getLDTable(inpFirstString, inpSecondString):
    s = inpFirstString
    t = inpSecondString
    m = len(s)
    n = len(t)
    table = [[i] for i in range(m+1)]
    for line in table:
        for char in t:
            line.append(0)
    d = table
    for j in range(1,n+1):
        d[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1,    # a deletion
                              d[i][j-1] + 1,    # an insertion
                              d[i-1][j-1] + 1)  # a substitution
    return d

def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    lines = []
    for line in f:
        line = line.replace('\n','')
        line = line.lower()
        lines.append(line)
    for line in getLDTable(lines[0],lines[1]):
        print line


if __name__ == "__main__":
    main(argv)