from zipfile import ZipFile
b = {}


def bb(a):
    c = b
    for i in range(len(a)):
        if a[i] in c:
            c = c[a[i]]
        else:
            c[a[i]] = {}


with ZipFile('input.zip') as myzip:
    a = list(myzip.namelist())
    for i in range(len(a)):
        if a[i][-1] == '/':
            a[i] = a[i][:-1]
    a = [i.split('/') for i in myzip.namelist()]
    for i in range(len(a)):
        if a[i][-1] == '':
            a[i] = a[i][:-1]
    for i in a:
        bb(i)


def aa(a, b):
    for key in a:
        print(b * ' ' + key)
        aa(a[key], b + 2)


aa(b, 0)
