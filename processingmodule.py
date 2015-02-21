from PIL import Image
from statmodule import classify
from mathmodule import calc_color_matrix
import re


def readfile(filename): #
    """
    Читаем файл и создаем список цветов в нем

    :param filename:
    :return PIL.Image:
    """
    im = Image.open(str(filename.name))
    return im


def getmatrix(im, x, y, size):
    """
`   Генерируем двумерный список с первым элементом в х,у размера size. Создается он по следующему правилу:
    берем цвет пикселя x+i, y+j, где i,j - итератор в диапазоне от начальной точки на картинке
    и до конечной точки матрицы. Возвращаемое значение - матрица.

    :param im:
    :param x:
    :param y:
    :param size:
    :return list(M):
    """
    M = [[list(im.getpixel(tuple((x+i, y+j))))
          for j in range(len(range(x, x+size)))]
         for i in range(len(range(y, y+size)))] #аналог нижеследующего цикла
    '''
    M = []
    for i in range(len(range(y, y + size))):
        M.append([list(im.getpixel(tuple((x + i, y + j)))) for j in range(len(range(x, x + size)))])'''
    return M


def resize(img, n):
    """
    Изменение размера картинки для деления на целое число матриц.
    n - размерность требуемой матрицы
    img - PIL.IMage
    :param img:
    :param n:
    :return PIL.Image:
    """
    x = img.size[0]
    y = img.size[1]

    while x%n != 0:
        x += 1
    while y%n != 0:
        y += 1
    img = img.resize((x,y), resample=1)
    return img



def bypass_picture(image, n): 
    """
    Основная функция обработки картинки. n - размер матрицы сжатия.
    :param image:
    :param n:
    :return list(colors):
    """
    image = resize(image, n)
    x, y = image.size[0], image.size[1]
    colors = []
    for i in range(0, image.size[0], n):
        for j in range(0, image.size[0], n):
            t = classify(calc_color_matrix(getmatrix(image, i, j, n), n))
            colors.append(t)
    return colors

def string_into_nums(in_string):
    """
    Функция парсинга строк, получаемых из вводимых пользователем данных. Отсекается все, что не числа.
    :param in_string:
    :return list(\d+):
    """
    ret = re.compile('\d+')  # выделять только числа
    return list(map(int, ret.findall(in_string))) #вернуть список строк, который преобразовывается в список чисел

