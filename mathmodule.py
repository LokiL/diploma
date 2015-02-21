__author__ = 'Арслан'

import math


def matrix_mult(matrix1, matrix2):
    """
    Функция для перемножения матриц (a*b)x(b*c)
    На входе две матрицы в формате A = [[a,b,c,..], [d,e,f,..],..]
    На выходе - результат перемножения.

    :param matrix1:
    :param matrix2:
    :return r:
    """
    s = 0  #сумма
    t = []  #временная матрица
    a = len(matrix1)
    b = len(matrix1[0])
    c = len(matrix2[0])
    r = []  # результирующая матрица
    for i in range(0, a):
        for j in range(0, c):
            for k in range(0, b):
                s = s + matrix1[i][k] * matrix2[k][j]
            t.append(s)
            s = 0
        r.append(t)
        t = []
    return r


def rgb_2_lab(rgb):
    """
    Преобразование цвета из RGB в Lab через промежуточное пространство XYZ
    :param RGB = [R,G,B]:
    :return [L,a,b]:
    """
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    r, g, b = r / 255, g / 255, b / 255  #нормализуем до десятичной дроби

    #Inverse sRGB Companding
    corr = lambda x: (((x + 0.055) / 1.055) ** 2.4)  #лямбда-функция для повторяющегося вычисления
    if r > 0.04045:
        r = corr(r)
    else:
        r = r / 12.92

    if g > 0.04045:
        g = corr(g)
    else:
        g = g / 12.92

    if b > 0.04045:
        b = corr(b)
    else:
        b = b / 12.92

    r, g, b = r * 100, g * 100, b * 100

    #Преобразование RGB в XYZ
    rgb = [[r], [g], [b]]
    M = [[0.4124564, 0.3575761, 0.1804375],
         [0.2126729, 0.7151522, 0.0721750],
         [0.0193339, 0.1191920, 0.9503041]]  #стандартная матрица преобразования для sRGB
    XYZ = matrix_mult(M, rgb)

    x = XYZ[0][0]
    y = XYZ[1][0]
    z = XYZ[2][0]

    white_x, white_y, white_z = 95.047, 100.000, 108.883  #Корректировка стандартной освещенности
    x, y, z = x / white_x, y / white_y, z / white_z

    #XYZ в Lab
    epsilon = 0.008856
    k = 903.3
    corrfunc2 = lambda t: (k * t + 16) / 116

    if x > epsilon:
        fx = x ** (1 / 3)
    else:
        fx = corrfunc2(x)

    if y > epsilon:
        fy = y ** (1 / 3)
    else:
        fy = corrfunc2(y)

    if z > epsilon:
        fz = z ** (1 / 3)
    else:
        fz = corrfunc2(z)

    L = round(((116 * fy) - 16), 4)
    a = round((500 * (fx - fy)), 4)
    b = round((200 * (fy - fz)), 4)

    return [L, a, b]


def lab_2_lch(lab):
    """
    Преобразование lab в LCH

    :param lab = [L,a,b]:
    :return [L,C,H]:
    """
    L = round((lab[0]), 4)
    C = round((math.sqrt(lab[1] ** 2 + lab[2] ** 2)), 4)
    H = round((math.atan2(lab[2], lab[1])), 4)
    if H > 0:
        H = (H / math.pi) * 180
    else:
        H = 360 - (abs(H) / math.pi) * 180
    return [L, C, H]


def colordifference(color1, color2):
    #colorX - [r,g,b]
    """
    Формула для подсчета цветового различия (CMC)

    :param color1 = [r,g,b]:
    :param color2 = [r,g,b]:
    :return float:
    """
    color1 = rgb_2_lab(color1)  #Берем Lab значение цвета
    color2 = rgb_2_lab(color2)  #Аналогично

    l = 2  #яркостный компонент
    c = 1  #хроматический компонент
    #Соотношение [l:c]=[2:1] используется для порога приемлемого различия

    #вычисление по формулам CMC
    L1, a1, b1 = color1[0], color1[1], color1[2]
    L2, a2, b2 = color2[0], color2[1], color2[2]
    #Создаем различные переменные
    C1 = round((math.sqrt(a1 ** 2 + b1 ** 2)), 4)
    C2 = round((math.sqrt(a2 ** 2 + b2 ** 2)), 4)
    dC = C1 - C2
    dL = L1 - L2
    da = a1 - a2
    db = b1 - b2
    dH = math.sqrt(abs(da ** 2 + db ** 2 - dC ** 2))
    SC = ((0.0638 * C1) / (1 + (0.0131 * C1))) + 0.638
    F = math.sqrt(C1 ** 4 / (C1 ** 4 + 1900))

    if L1 < 16:
        SL = 0.511
    else:
        SL = (0.040975 * L1) / (1 + (0.01765 * L1))

    H1 = math.atan2(b1, a1)
    if H1 > 0:
        H1 = (H1 / math.pi) * 180
    else:
        H1 = 360 - (abs(H1) / math.pi) * 180

    if (164 <= H1) or (H1 <= 345):
        T = 0.56 + abs(0.2 * math.cos(H1 + 168))
    else:
        T = 0.36 + abs(0.4 * math.cos(H1 + 35))

    SH = SC * ((F * T) + 1 - F)

    colordiff = math.sqrt(
        (dL / (l * SL)) ** 2 + (dC / (c * SC)) ** 2 + (dH / SH) ** 2)  #Считаем, собственно, разницу цветов

    return round(colordiff, 4)  #Значение абсолютно


def calc_color_matrix(M, n):  #NB! Возможно некорректно нелинейное преобразование, проверить
    """
    Cреднее арифметическое матрицы, используется для получения среднего цвета в матрице n*n.
    Подсчет идет через суммирование каждой компоненты и деление на общее число.
    M - матрица
    n - размер

    :param M:
    :param n:
    :return [R,G,B]:
    """
    avR = 0
    avG = 0
    avB = 0
    for i in range(n):
        for j in range(n):
            avR += M[i][j][0]
            avG += M[i][j][1]
            avB += M[i][j][2]
    avcalc = lambda t: t / (n * n)
    avR = int(avcalc(avR))
    avG = int(avcalc(avG))
    avB = int(avcalc(avB))
    return [avR, avG, avB]
