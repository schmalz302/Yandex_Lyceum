import shutil
import datetime


def make_reserve_arc(source, dest):
    now = datetime.datetime.now()
    f = f'{now.day}.{now.month}.{now.year}-{now.hour}.{now.minute}.{now.second}'
    shutil.make_archive(f'archive_{f}', 'zip', root_dir=source)
    shutil.move(f'archive_{f}.zip', dest)


make_reserve_arc(input("Введите путь к каталогу, который надо архивировать: "),
                 input("Введите путь к каталогу, в который необходимо поместить результат: "))
