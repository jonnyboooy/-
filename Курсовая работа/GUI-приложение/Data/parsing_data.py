import pandas as pd
import os
import keyboard


def parsing():
    '''Функция, в которой парсятся исходные данные из файла "input_data.xlsx".'''

    if os.path.exists('input_data.xlsx'):
        print('\033[92m' + 'Файл \'input_data.xlsx\' был успешно открыт на чтение!\n' + '\033[30m')

        aircraft_data = pd.read_excel('input_data.xlsx', sheet_name='aircraft')
        air_defense_data = pd.read_excel('input_data.xlsx', sheet_name='air_defense')

        return aircraft_data, air_defense_data
    else:
        print('\033[91m' + 'Ошибка при открытии файла \'input_data.xlsx\' на чтение!\n'
              '\t - Нажмите клавишу < Enter >, чтобы повторить попытку\n'
              '\t - Нажмите клавишу < Escape >, чтобы завершить работу' + '\033[30m')

        while True:
            if keyboard.read_key() == 'esc':
                exit(0)
            elif keyboard.read_key() == 'enter':
                break

        return parsing()
