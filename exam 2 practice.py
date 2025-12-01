def countEs(st):
    count = 0
    if st == 0:
        return 0
    else:
        if 'e' in st:
            count += 1
    return count

def countEs(x,st):
    x = 0
    if st == '':
        return x
    elif 'e' not in st[0]:
        return st[:1]
    else:
        return (x,st[:1])
##def minEs(st):
##    ls = ''
##    es = countEs(st)
##    if st == '':
##        return ''
##    elif es[0] < es[1]:
##        return countEs[0]
##    else:
##        return -1
def countChars(string):
    d = {}
    for ch in string:
        a = string.count(ch)
        d[ch] = a
    return d

def makeDict(lst):
    d = {}
    for i in range(len(lst)):
        if i % 2 == 0:
            d[lst[i]] = [lst[i+1]]
    return d

##def extractVal(d, key):
##    if key in d:
##        return d[key]
def extractVal(d,keys):
    vals = []
    for key in keys:
        if key in d:
            vals.append(d[key])
        else:
            vals.append(None)
    return vals

