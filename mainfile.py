__author__ = 'Мусин А.А. МГППУ ИТ 5.2'
__copyright__ = 'Copyright 2015'
__license__ = 'GNU GPL'
__version__ = '2.1'
__maintainer__ = 'Musin A.A.'
__email__ = 'lernar@gmail.com'
__status__ = 'Release'

from tkinter.filedialog import askopenfile
from processingmodule import bypass_picture, readfile, string_into_nums


def load_file():
    """
    Функция для вызова диалога открытия


    :return string:
    """
    fn = askopenfile()
    if fn == '':
        return
    else:
        return fn


def start_color_analysis(fn):  #основной цикл
    """
    Старт основного цикла программы

    :param fn: string путь к файлу
    :return None:
    """
    t = bypass_picture(readfile(fn), current_matrix)

    return t



#стартовые значения
current_blue = [0, 77, 255]
current_green = [0, 255, 0]
current_red = [255, 0, 0]
current_yellow = [255, 237, 0]
current_violet = [90, 0, 157]
current_brown = [150, 75, 0]
current_black = [0, 0, 0]

current_matrix = 3  #значение матрицы

current_color = [['blue', current_blue],  #blue
                 ['green', current_green],  #green
                 ['red', current_red],  #red
                 ['yellow', current_yellow],  #yellow
                 ['violet', current_violet],  #violet
                 ['brown', current_brown],  #brown
                 ['black', current_black]]  #black
                #['grey', [133, 133, 133]]]  #grey
