__author__ = 'Арслан'

from tkinter import *
from tkinter.ttk import *

from mainfile import *
from statmodule import get_number_of_colors


def load(event):
    """
    Обработчик события загрузки файла

    :param event:
    :return None:
    """
    fn = load_file()
    if fn is None:
        return
    else:
        file_name_label.configure(text=fn.name)  #выводим имя открытого файла на форме
        root.update_idletasks()  #Обновляем форму
        t = start_color_analysis(fn)  #Запускаем анализ
        #print(get_number_of_colors(t))
        results_message.configure(text=get_number_of_colors(t))
        return


def change_parameters(event):
    """
    Обработчик события нажатия кнопки загрузки параметров.
    Изменяет параметры анализа изображения: значения цвета и матрицы сжатия

    :param event:
    :return None:
    """
    #Меняем цвета
    current_blue = string_into_nums(blue_entry.get())
    current_blue_label.configure(text=current_blue)

    current_green = string_into_nums(green_entry.get())
    current_green_label.configure(text=current_green)

    current_red = string_into_nums(red_entry.get())
    current_red_label.configure(text=current_red)

    current_yellow = string_into_nums(yellow_entry.get())
    current_yellow_label.configure(text=current_yellow)

    current_violet = string_into_nums(violet_entry.get())
    current_violet_label.configure(text=current_violet)

    current_brown = string_into_nums(brown_entry.get())
    current_brown_label.configure(text=current_brown)

    current_black = string_into_nums(black_entry.get())
    current_black_label.configure(text=current_black)

    current_color = [['blue', current_blue],  #blue
                     ['green', current_green],  #green
                     ['red', current_red],  #red
                     ['yellow', current_yellow],  #yellow
                     ['violet', current_violet],  #violet
                     ['brown', current_brown],  #brown
                     ['black', current_black]]

    #Меняем матрицу
    current_matrix = string_into_nums(matrix_scale_correction_entry.get())
    current_matrix_label.configure(text=current_matrix)

    return


def get_dalt(event):
    """
    Обработчик события изменения параметра дальтонизма

    :param event:
    :return None:
    """
    current_daltonism = daltonism_combobox.get()
    return


if __name__ == '__main__':
    root = Tk()
    root.title('Color analysis')
    root.resizable(0, 0)

    '''Блок создания виджетов'''
    #создание фреймов для организации
    btn_frame = Frame(root)
    color_select_frame = Frame(root)
    matrix_scale_correction_frame = Frame(root)
    daltonism_frame = Frame(root)
    results_frame = Frame(root)

    #Фрейм управления
    open_file_button = Button(btn_frame, text='Load File')  #Кнопка для запуска основного цикла
    open_file_button.bind('<Button-1>', load)  #1 параметр - по лкм активация, второй - вызываемая функция
    info_label = Label(btn_frame, text='Открытый файл:')
    file_name_label = Label(btn_frame)
    change_parameters_button = Button(btn_frame, text='Изменить параметры цвета')  #Кнопка чтения параметров
    change_parameters_button.bind('<Button-1>', change_parameters)

    #Фрейм ввода цветов
    #Подписи к полям ввода цвета
    color_parameters = Label(color_select_frame, text='Параметры цвета(R G B:')
    custom_color_parameters_label = Label(color_select_frame, text='Свои')
    current_color_parameters_label = Label(color_select_frame, text='Текущие')
    current_blue_label = Label(color_select_frame, text=current_color[0][1])
    current_green_label = Label(color_select_frame, text=current_color[1][1])
    current_red_label = Label(color_select_frame, text=current_color[2][1])
    current_yellow_label = Label(color_select_frame, text=current_color[3][1])
    current_violet_label = Label(color_select_frame, text=current_color[4][1])
    current_brown_label = Label(color_select_frame, text=current_color[5][1])
    current_black_label = Label(color_select_frame, text=current_color[6][1])

    blue_label = Label(color_select_frame, text='Синий:')
    green_label = Label(color_select_frame, text='Зеленый:')
    red_label = Label(color_select_frame, text='Красный:')
    yellow_label = Label(color_select_frame, text='Желтый:')
    violet_label = Label(color_select_frame, text='Фиолетовый:')
    brown_label = Label(color_select_frame, text='Коричневый:')
    black_label = Label(color_select_frame, text='Черный:')

    #Поля для ввода своих значений цвета
    blue_entry = Entry(color_select_frame, width=10)  #width - x-размер виджета
    green_entry = Entry(color_select_frame, width=10)
    red_entry = Entry(color_select_frame, width=10)
    yellow_entry = Entry(color_select_frame, width=10)
    violet_entry = Entry(color_select_frame, width=10)
    brown_entry = Entry(color_select_frame, width=10)
    black_entry = Entry(color_select_frame, width=10)

    #Фрейм корректировки матрицы
    #Ввод матрицы сжатия
    matrix_scale_correction_label = Label(matrix_scale_correction_frame, text='Матрица \nсжатия:')
    custom_matrix_parameters_label = Label(matrix_scale_correction_frame, text='Своя')
    current_matrix_parameters_label = Label(matrix_scale_correction_frame, text='Текущая')
    matrix_scale_correction_entry = Entry(matrix_scale_correction_frame, width=3)
    current_matrix_label = Label(matrix_scale_correction_frame, text=current_matrix)


    #Фрейм дальтонизма
    #Корректировка для дальтоников, надписи
    daltonism_label = Label(daltonism_frame, text='Цветовая слепота')
    daltonism_combobox = Combobox(daltonism_frame, values=['Норма', 'Протанопия', 'Дейтеранопия', 'Тританопия'])
    daltonism_combobox.set('Норма')
    daltonism_combobox.bind('<Button-1>', get_dalt)


    #Фрейм вывода результатов
    results_label = Label(results_frame, text='Результат анализа')
    results_message = Message(results_frame, text='Проверка\nПроверка\nПроверка')

    '''Настройка расположения элементов'''
    #Фреймы
    btn_frame.grid(row=0, column=0, sticky='w', pady=3, padx=3, columnspan=4)
    color_select_frame.grid(row=1, column=0, columnspan=2, sticky='w', pady=3, padx=3)
    matrix_scale_correction_frame.grid(row=2, column=0, columnspan=2, sticky='w', pady=3, padx=3)
    daltonism_frame.grid(row=3, column=0, columnspan=2, sticky='w', pady=3, padx=3)
    results_frame.grid(row=1, column=3, sticky='n', pady=3, padx=3)

    #Блок файла
    open_file_button.grid(row=0, column=0, sticky='w', pady=1,
                          padx=1)  #размещение в сетке, row - номер строки, column - номер столбца
    info_label.grid(row=1, column=0, sticky='w', pady=1, padx=1)
    file_name_label.grid(row=1, column=2, sticky='w', pady=1, padx=1)
    change_parameters_button.grid(row=0, column=1, sticky='w', pady=1, padx=1)
    #Блок ввода цветов
    color_parameters.grid(row=0, column=0, columnspan=2, sticky='w', pady=1,
                          padx=1)  #сolumnspan - количество столбцов, занимаемых виджетом
    custom_color_parameters_label.grid(row=1, column=1, sticky='w', pady=1, padx=1)
    current_color_parameters_label.grid(row=1, column=2, sticky='w', pady=1, padx=1)
    blue_label.grid(row=2, column=0, sticky='w', pady=1, padx=1)  #sticky - приклеивание к стороне света
    blue_entry.grid(row=2, column=1, sticky='e', pady=1, padx=1)
    green_label.grid(row=3, column=0, sticky='w', pady=1, padx=1)
    green_entry.grid(row=3, column=1, sticky='e', pady=1, padx=1)
    red_label.grid(row=4, column=0, sticky='w', pady=1, padx=1)
    red_entry.grid(row=4, column=1, sticky='e', pady=1, padx=1)
    yellow_label.grid(row=5, column=0, sticky='w', pady=1, padx=1)
    yellow_entry.grid(row=5, column=1, sticky='e', pady=1, padx=1)
    violet_label.grid(row=6, column=0, sticky='w', pady=1, padx=1)
    violet_entry.grid(row=6, column=1, sticky='e', pady=1, padx=1)
    brown_label.grid(row=7, column=0, sticky='w', pady=1, padx=1)
    brown_entry.grid(row=7, column=1, sticky='e', pady=1, padx=1)
    black_label.grid(row=8, column=0, sticky='w', pady=1, padx=1)
    black_entry.grid(row=8, column=1, sticky='e', pady=1, padx=1)
    current_blue_label.grid(row=2, column=2, sticky='e', pady=1, padx=1)
    current_green_label.grid(row=3, column=2, sticky='e', pady=1, padx=1)
    current_red_label.grid(row=4, column=2, sticky='e', pady=1, padx=1)
    current_yellow_label.grid(row=5, column=2, sticky='e', pady=1, padx=1)
    current_violet_label.grid(row=6, column=2, sticky='e', pady=1, padx=1)
    current_brown_label.grid(row=7, column=2, sticky='e', pady=1, padx=1)
    current_black_label.grid(row=8, column=2, sticky='e', pady=1, padx=1)

    #блок корректировки матрицы
    matrix_scale_correction_label.grid(row=0, column=0, sticky='w', pady=1, padx=1)
    custom_matrix_parameters_label.grid(row=1, column=0, sticky='w', pady=1, padx=1)
    current_matrix_parameters_label.grid(row=1, column=1, sticky='w', pady=1, padx=1)
    matrix_scale_correction_entry.grid(row=2, column=0, sticky='w', pady=1, padx=1)
    current_matrix_label.grid(row=2, column=1, sticky='w', pady=1, padx=1)

    #блок дальтонизма
    daltonism_label.grid(row=0, column=0, sticky='w', pady=1, padx=1)
    daltonism_combobox.grid(row=5, column=0)

    #блок вывода результатов
    results_label.grid(row=0, column=0, columnspan=2, sticky='w', pady=1, padx=1)
    results_message.grid(row=1, column=0, columnspan=2, sticky='w', pady=1, padx=1)

    root.mainloop()