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

def get_number_of_colors(color):
    list = []
    list.append(['grey', color.count('grey')])
    list.append(['blue', color.count('blue')])
    list.append(['green', color.count('green')])
    list.append(['red', color.count('red')])
    list.append(['yellow', color.count('yellow')])
    list.append(['violet', color.count('violet')])
    list.append(['brown', color.count('brown')])
    list.append(['black', color.count('black')])
    return list

''' Непонятно откуда, потом подчистить.
def count_colors(list):
    """

    :param list:
    :return:
    """
    d = {i[0]: list.count(i[0]) for i in current_color}
    return d
'''
