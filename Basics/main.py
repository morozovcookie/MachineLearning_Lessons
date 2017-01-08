import pandas
import numpy
import os


def categorical_to_numeric(data_frame):
    headers = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason',
               'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet',
               'romantic']
    for header in headers:
        data_frame[header] = data_frame[header].astype('category')
        data_frame[header] = data_frame[header].cat.codes
    return data_frame

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    student_dir = os.path.join(base_dir, 'student')
    output_dir = os.path.join(base_dir,  'output')

    # Создаем директорию для выходных файлов
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Читаем датасеты
    df_mat = pandas.read_csv(os.path.join(student_dir, 'student-mat.csv'), sep=';')
    df_por = pandas.read_csv(os.path.join(student_dir, 'student-por.csv'), sep=';')

    # Всем нечисленным параметрам ставим в соответствие некоторое число
    df_mat = categorical_to_numeric(data_frame=df_mat)
    df_por = categorical_to_numeric(data_frame=df_por)

    # "Математика" и "Португальский" также являются параметрами для датасета
    # К каждому датасету добавил столбец cources, где math=0, а por=1
    df_mat = df_mat.assign(course=pandas.Series(numpy.array([0] * df_mat.shape[0])))
    df_por = df_por.assign(course=pandas.Series(numpy.array([1] * df_por.shape[0])))

    # Объединим два датасета в один
    merged = pandas.concat([df_mat, df_por])

    # Сохраним каждый датасет в новый csv-файл
    df_mat.to_csv(os.path.join(output_dir, 'student-mat.csv'),    sep=';', index=False)
    df_por.to_csv(os.path.join(output_dir, 'student-por.csv'),    sep=';', index=False)
    merged.to_csv(os.path.join(output_dir, 'student-merged.csv'), sep=';', index=False)
