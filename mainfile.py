__author__ = 'Арслан'

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
    bypass_picture(readfile(fn), current_matrix)

    return



#стартовые значения
current_blue = [0, 77, 255]
current_green = [0, 255, 0]
current_red = [255, 0, 0]
current_yellow = [255, 237, 0]
current_violet = [90, 0, 157]
current_brown = [150, 75, 0]
current_black = [0, 0, 0]

current_matrix = 3  #значение матрицы
current_daltonism = 'Норма'  #0,1,2,3 - "Норма","Протанопия", "Дейтеранопия", "Тританопия"

current_color = [['blue', current_blue],  #blue
                 ['green', current_green],  #green
                 ['red', current_red],  #red
                 ['yellow', current_yellow],  #yellow
                 ['violet', current_violet],  #violet
                 ['brown', current_brown],  #brown
                 ['black', current_black]]  #black
                #['grey', [133, 133, 133]]]  #grey
