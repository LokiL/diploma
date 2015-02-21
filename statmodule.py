__author__ = 'Арслан'

from mathmodule import colordifference, lab_2_lch, rgb_2_lab
import mainfile


def classify(color):
    """
    Функция классификации цвета.

    :param color:
    :return string(id):
    """
    diff = 100
    id = ''
    tmpcolor = lab_2_lch(rgb_2_lab(color))
    if tmpcolor[1] <= 22:  #отдельная проверка на серый цвет
        return 'grey'
    else:
        for i in range(len(mainfile.current_color)):
            t = colordifference(color, mainfile.current_color[i][1])
            if t < diff:
                diff = t
                id = mainfile.current_color[i][0]
        return id


''' Непонятно откуда, потом подчистить.
def count_colors(list):
    """

    :param list:
    :return:
    """
    d = {i[0]: list.count(i[0]) for i in current_color}
    return d
'''
