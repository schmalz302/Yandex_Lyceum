from zipfile import ZipFile
import zipfile
import os


def human_read_format(size):
    if size < 1024:
        return f'{round(size)}Б'
    elif size / 1024 < 1024:
        a = size / 1024
        return f'{round(a)}КБ'
    elif size / (1024 ** 2) < 1024:
        a = size / (1024 ** 2)
        return f'{round(a)}МБ'
    elif size / (1024 ** 3) < 1024:
        a = size / (1024 ** 3)
        return f'{round(a)}ГБ'


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
    bc = list(myzip.namelist())
    cc = []
    cd = []
    for i in range(len(a)):
        cd = os.path.isfile(myzip.extract(a[i]))
        cc = human_read_format(myzip.getinfo(a[i]).file_size)
        if a[i][-1] == '/':
            a[i] = a[i][:-1]
        if cd:
            a[i] += f'__{cc}'
    a = [i.split('/') for i in a]
    for i in range(len(a)):
        if a[i][-1] == '':
            a[i] = a[i][:-1]
    for i in a:
        bb(i)


def aa(a, b):
    for key in a:
        c = ' '.join(key.split('__')).rstrip()
        print(b * ' ' + c)
        aa(a[key], b + 2)


aa(b, 0)



