"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""



def display_symbol_row(start_code, end_code, length=10, pos=0, flag=False):
    """

    :param start_code: start symbol code for the table
    :param end_code: end symbol code for the table
    :param length: row length
    :param pos: current position of symbol in the row
    :param flag: symbol has a last position in the row
    :return: table of the ASCII symbol in the range
    """
    if start_code > end_code:
        return False
    if pos == length:
        pos = 0
        flag = True
    if start_code == end_code:
        if flag:
            flag = False
            return "\n" + str(start_code) + " - '" + str(chr(start_code)) + "'"
        else:
            return str(start_code) + " - '" + str(chr(start_code)) + "'"
    else:
        if flag:
            flag = False
            return "\n" + str(start_code) + " - '" + str(chr(start_code)) + "'\t" + display_symbol_row(start_code + 1,
                                                                                                       end_code,
                                                                                                       length,
                                                                                                       pos + 1,
                                                                                                       flag)
        else:
            return str(start_code) + " - '" + str(chr(start_code)) + "'\t" + display_symbol_row(start_code + 1,
                                                                                                end_code,
                                                                                                length,
                                                                                                pos + 1,
                                                                                                flag)


print(display_symbol_row(32, 127, 10))
