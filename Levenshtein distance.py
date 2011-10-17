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

def getListOfChangesFromTable(inpLDTable, inpFirstString, inpSecondString):
    d = inpLDTable
    s = inpFirstString
    t = inpSecondString
    tmpStr = s
    result = [tmpStr]
    i = len(s)
    j = len(t)
    while i != 0 or j != 0:
        if i == 0:
            tmpStr = tmpStr[:i] + t[j-1] + tmpStr[i:] # an insertion
            j -= 1
        elif j == 0:
            tmpStr = tmpStr[:i-1] + '' + tmpStr[i:] # a deletion
            i -= 1
        elif d[i-1][j] < d[i][j]:
            tmpStr = tmpStr[:i-1] + tmpStr[i:] # a deletion
            i -= 1
        elif d[i][j-1] < d[i][j]:
            tmpStr = tmpStr[:i] + t[j-1] + tmpStr[i:] # an insertion
            j -= 1
        elif d[i-1][j-1] < d[i][j]:
            tmpStr = tmpStr[:i-1] + t[j-1] + tmpStr[i:] # a substitution
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
            continue
        result.append(tmpStr)
    return  result


def getListOfChanges(inpFirstString, inpSecondString):
    LDTable = getLDTable(inpFirstString,inpSecondString)
    listOfChanges = getListOfChangesFromTable(LDTable,inpFirstString,inpSecondString)
    return listOfChanges

def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    lines = []
    for line in f:
        line = line.replace('\n','')
        line = line.lower()
        lines.append(line)
    listOfChanges = getListOfChanges(lines[0],lines[1])
    for item in listOfChanges:
        print item



if __name__ == "__main__":
    main(argv)