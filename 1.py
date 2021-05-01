import os
aa = input('Введите название каталога: ')
cc = os.listdir(aa)
f = []


# функция для представления размера в нормальном виде
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


for i in os.listdir(aa):
    c = os.path.getsize(f"{aa}\{i}")
    if os.path.isdir(f"{aa}\{i}"):
        f.append([len(os.listdir(f"{aa}\{i}")), human_read_format(c), c, i])
    else:
        f.append([0, human_read_format(c), c, i])
f = sorted(f, key=lambda x: x[0])[-10:]
f = sorted(f, key=lambda x: x[2])[::-1]
for i in range(len(f)):
    print(f"{f[i][3]}{(40 - len(str(f[i][3]))) * ' '}-{f[i][1]}")
