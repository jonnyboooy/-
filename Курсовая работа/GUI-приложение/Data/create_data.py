import pandas as pd
from random import randint


def create_data(number_of_air_defenses: int):
    '''Функция, в которой формируются исходные данные и записываются в файл "input_data.xlsx".'''

    aircraft_data = pd.DataFrame(data={'X0': 0,
                                       'Y0': 0,
                                       'X_end': 15,
                                       'Y_end': 15},
                                 index=[0])

    air_defense_data = pd.DataFrame(data={'X_target': 7,
                                          'Y_target': 7,
                                          'R_target': 3},
                                    index=[0])

    with pd.ExcelWriter(path='input_data.xlsx', mode='w') as writer:

        aircraft_data.to_excel(excel_writer=writer,
                               sheet_name='aircraft',
                               index=False)
        air_defense_data.to_excel(excel_writer=writer,
                                  sheet_name='air_defense',
                                  index=False)
