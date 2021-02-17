import os
import string


def Gamma():
    A = 7
    B = 3
    M = 4096
    y = 2020
    gamma_list = []
    for i in range(8):
        y = (A * y) % M
        gamma_list.append(y)
    return gamma_list


def Coded(text):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    # находим индексы всех пробелов и записываем их
    index = []
    for i in range(len(text)):
        if text[i] == ' ':
            index.append(i)
    # текст переводим в верхний регистр и удаляем пробелы
    text = text.upper().replace(' ', '')
    coded_text = ''
    gamma_list = Gamma()
    cnt = 0
    for i in range(len(text)):
        coded_text += chr((ord(text[i]) + gamma_list[cnt] % 32))
        cnt += 1
        if cnt == 7:
            cnt = 0
    # возвращаем пробелы на места
    for i in index:
        coded_text = coded_text[0:i] + ' ' + coded_text[i:]
    return coded_text


def DeCoded(text):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    # находим индексы всех пробелов и записываем их
    index = []
    for i in range(len(text)):
        if text[i] == ' ':
            index.append(i)
    # текст переводим в верхний регистр и удаляем пробелы
    text = text.replace(' ', '')
    decoded_text = ''
    gamma_list = Gamma()
    cnt = 0
    for i in range(len(text)):
        decoded_text += chr((ord(text[i]) - gamma_list[cnt] % 32))
        cnt += 1
        if cnt == 7:
            cnt = 0
    # возвращаем пробелы на места
    for i in index:
        decoded_text = decoded_text[0:i] + ' ' + decoded_text[i:]
    return decoded_text.lower()


print("1 - Шифрование")
print("2 - Расшифровка")
answer = int(input('Ваш выбор: '))
os.system('CLS')
if answer == 1:
    f = open('Source.txt', 'r', encoding='utf-8')
    text = f.read()
    Coded_message = Coded(text)
    f.close()
    f = open('Coded.txt', 'w', encoding='utf-8')
    f.write(Coded_message)
    f.close()
    print('Файл зашифрован')
    a = input('Нажмите Enter для выхода')

if answer == 2:
    f = open('Coded.txt', 'r', encoding='utf-8')
    text = f.read()
    DeCoded_message = DeCoded(text)
    f.close()
    f = open('DeCoded.txt', 'w', encoding='utf-8')
    f.write(DeCoded_message)
    f.close()
    print('Файл расшифрован')
    a = input('Нажмите Enter для выхода')
