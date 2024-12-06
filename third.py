import csv
import pickle

def load_table(filepath, delimiterr = ','):
    """
    :param filepath: file from which the table is extracted
    :param delimiterr: a string used to separate fields
    :return: dictionary where key is the column name, values are the column data
    """
    if filepath[-3:] == 'csv':
        try:
            with open(filepath, 'r', newline = '', encoding = 'utf-8') as file:
                reader = csv.reader(file, delimiter = delimiterr)
                headers = next(reader)
                rows = list(reader)
                list1 = [headers] + rows
                header = list1[0][0].split(',')
                row = []
                for ind in range(len(rows)):
                    line = rows[ind][0].split(',')
                    row.append(line)
                row2 = []
                total1 = []
                for ind2 in range(len(row[0])):
                    listt = []
                    for ind3 in range(len(row)):
                        listt.append(row[ind3][ind2])
                    total1.append(listt)
                dic1 = dict(zip(header, total1))
                return dic1

        except FileNotFoundError:
            return 'Файл не найден'
    elif filepath[-3:] == 'pkl':
        try:
            with open(filepath, 'rb') as file:
                dic1 = pickle.load(file)
            return dic1
        except FileNotFoundError:
            return 'Файл не найден'
    elif filepath[-3:] == 'txt':
        try:
            with open(filepath, "r", encoding = 'utf-8') as file:
                lines = file.readlines()
                header = lines[0].strip().split()
                dic1 = {key: [] for key in header}
                for line in lines[1:]:
                    values = line.strip().split()
                    for i, value in enumerate(values):
                        dic1[header[i]].append(value)
            return dic1
        except FileNotFoundError:
            return 'Файл не найден'




def save_table(data):
    """
    :param data: dictionary where key is the column name, values are the column data
    :return: saves the dictionary to a table in a file in the specified format
    """
    formatt = input('Введите формат файла, в который хотите сохранить таблицу: ')
    if formatt == 'csv':
        kkeys = list(data.keys())
        vvalues = list(data.values())
        newlist = []
        newlist.append(kkeys)
        for ind in range(len(vvalues[0])):
            line = []
            for ind2 in range(len(vvalues)):
                part = vvalues[ind2][ind]
                line.append(part)
            newlist.append(line)
        try:
            with open('newflow.csv', 'w+', newline = '') as file:
                writer = csv.writer(file, delimiter = ';')
                writer.writerows(newlist)
                return 'Словарь успешно сохранен в файл'
        except FileNotFoundError:
            return 'Файл не найден'
    elif formatt == 'pkl':
        try:
            with open('newflow.pkl', 'wb') as table:
                pickle.dump(data, table)
            return 'Словарь успешно сохранен в файл'
        except FileNotFoundError:
            return 'Файл не найден'
    elif formatt == 'txt':
        kkeys = list(data.keys())
        vvalues = list(data.values())
        newlist = []
        newlist.append(kkeys)
        for ind in range(len(vvalues[0])):
            line = []
            for ind2 in range(len(vvalues)):
                part = vvalues[ind2][ind]
                line.append(part)
            newlist.append(line)
        try:
            with open('newflow.txt', 'w+', newline = '') as file:
                for ind in range(len(newlist)):
                    line = ''
                    for ind2 in range(len(newlist[ind])):
                        line += newlist[ind][ind2] + ' '
                    file.write(line + "\n")
                return 'Словарь успешно сохранен в файл'
        except FileNotFoundError:
            return 'Файл не найден'


def get_rows_by_number(table, start = 1, stop = 'none', copy_table = False):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param start: line number from which the output will be
    :param stop: line number up to which the output will be
    :param copy_table: is there a need to save the table to a file
    :return: information about successful file saving
    """
    kkeys = list(table.keys())
    vvalues = list(table.values())
    newval = []
    newval.append(kkeys)
    for ind in range(len(vvalues[0])):
        line = []
        for ind2 in range(len(vvalues)):
            part = vvalues[ind2][ind]
            line.append(part)
        newval.append(line)
    result = []
    if not(stop == 'none') and not(stop > len(newval)):
        for lin in range(len(newval)):
            if start <= lin + 1 <= stop:
                result.append(newval[lin])
        if copy_table == False:
            return result
        else:
            try:
                with open('newflow1.csv', 'w+', newline = '') as file:
                    writer = csv.writer(file, delimiter = ';')
                    writer.writerows(result)
                    return 'Словарь успешно сохранен в файл'
            except FileNotFoundError:
                return 'Файл не найден'


def get_rows_by_index(table, figures, copy_table = False):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param figures: number of lines to output
    :param copy_table: is there a need to save the table to a file
    :return: dictionary or information about successful saving of the dictionary to a file
    """
    kkeys = list(table.keys())
    vvalues = list(table.values())
    newval = []
    newval.append(kkeys)
    for ind in range(len(vvalues[0])):
        line = []
        for ind2 in range(len(vvalues)):
            part = vvalues[ind2][ind]
            line.append(part)
        newval.append(line)
    result = []
    for ind3 in range(len(figures)):
        result.append(newval[figures[ind3]])
    if copy_table == False:
        return result
    else:
        try:
            with open('newflow2.csv', 'w+', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(result)
                return 'Словарь успешно сохранен в файл'
        except FileNotFoundError:
            return 'Файл не найден'

def get_column_types(table):
    """
    :param table: dictionary where key is the column name, values are the column data
    :return: dictionary with information about the type of values in the column
    """
    try:
        vvalues = list(table.values())
        kkeys = []
        for ind in range(len(vvalues)):
            kkeys.append((ind + 1, type(vvalues[ind][0])))
        return dict(kkeys)
    except:
        return 'Не удалось создать словарь'

def set_column_types(dictt):
    """
    :param dictt: dictionary where key is the column name, values are the column data
    :return: writing a dictionary with information about the type of values in columns to a file
    """
    kkeys = [list(dictt.keys())]
    vvalues = [list(dictt.values())]
    total = kkeys + vvalues
    try:
        with open('newflow3.csv', 'w+', newline = '') as file:
            writer = csv.writer(file, delimiter = ';')
            writer.writerows(total)
            return 'Словарь успешно сохранен в файл'
    except FileNotFoundError:
        return 'Файл не найден'

def get_values(table, column = 0):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param column: table column number
    :return: list of table values from a column or by column number
    """
    try:
        if type(column) == int:
            vvalues = list(table.values())
            return vvalues[column - 1]
        else:
            return table[column]
    except:
        return 'Не удалось вывести значения'

def get_value(table, column = 0):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param column: element number in a single-row table
    :return: element of a table
    """

    try:
        kkeys = list(table.keys())
        if type(column) == int:
            return kkeys[column]
        else:
            return column
    except:
        return 'Не удалось вывести элемент'

def set_values(table, column = 0):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param column: column name or number
    :return: list of values for table column
    """
    try:
        if type(column) == int:
            vvalues = list(table.values())
            vvalues[column - 1] = input('Введите новое значение: ').split()
            return vvalues
        else:
            kkeys = list(table.keys())
            ind = kkeys.index(column)
            vvalues = list(table.values())
            vvalues[ind] = input('Введите новое значение: ').split()
            return vvalues
    except:
        return 'Не удалось создать список'


def set_value(table, column):
    """
    :param table: dictionary where key is the column name, values are the column data
    :param column: element name or number
    :return: element
    """
    try:
        kkeys = list(table.keys())
        if type(column) == int:
            kkeys[column - 1] = input('Введите новое значение: ')
            return kkeys
        else:
            ind = kkeys.index(column)
            kkeys[ind] = input('Введите новое значение: ')
            return kkeys
    except:
        return 'Не удалось вывести элемент'

def print_table(data):
    """
    :param data: dictionary where key is the column name, values are the column data
    :return: table
    """
    try:
        kkeys = list(data.keys())
        vvalues = list(data.values())
        newlist = []
        newlist.append(kkeys)
        for ind in range(len(vvalues[0])):
            line = []
            for ind2 in range(len(vvalues)):
                part = vvalues[ind2][ind]
                line.append(part)
            newlist.append(line)
        result = ''
        for ind in range(len(newlist)):
            line = ''
            for ind2 in range(len(newlist[ind])):
                line += newlist[ind][ind2] + ' '
            result += line + '\n'
        return result
    except:
        return 'Ошибка вывода таблицы'
filepath = 'gogl.csv'
delimiterr = ';'
table_data = load_table(filepath, delimiterr)
print(load_table(filepath, delimiterr))
print(save_table(table_data))
print(get_rows_by_number(table_data, 1, 3))
print(get_rows_by_index(table_data, [0, 2]))
print(get_column_types(table_data))
print(set_column_types(get_column_types(table_data)))
print(get_values(table_data, 'Страна'))
print(get_value(table_data, 2))
print(set_values(table_data, 'Имя'))
print(set_value(table_data, 3))
print(print_table(table_data))
