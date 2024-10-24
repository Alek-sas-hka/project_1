class GlobalsVar:
    # Алфавиты для шифра Цезаря
    Eng_Upper: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Eng_Lower: str = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    Ru_Upper: str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    Ru_Lower: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    # Частота
    Freq = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
            'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
            'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
            'q': 0.10, 'z': 0.07}

    # Символы в Коде Бодо для шифра Вернама
    Bodo = dict(zip(['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '],
                    ['01010', '00011', '11001', '01110', '01001', '00001', '01101', '11010', '10100', '00110',
                     '01011', '01111', '10010', '11100', '01100', '11000', '10110', '10111', '00101',
                     '10000', '00111', '11110', '10011', '11101', '10101', '10001', '00100']))

    Size = 54
    Deg_List = [1, 2, 4, 8]
    Bit_Eight = 8
    Text_Freq = 1
    Byte_Start = 0
    Text_mask = 0b11111111
    Img_mask = 0b11111111
    Palette = 256
    SQRT = 0.5
    Size_Condition = 5
    Shift = 96
    Contrast_Size = 100
    Font_Size_25 = 25
    Font_Size_20 = 20
    Row_Size_1 = 1
    Row_Size_2 = 2
    Row_Size_3 = 3
    Row_Size_4 = 4
    Column_Size_1 = 1
    Column_Size_3 = 3
