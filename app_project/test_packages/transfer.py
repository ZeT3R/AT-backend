# -*- coding: windows-1251 -*-

import math
import random


def from10to2(a, precision):
    frac, whole = math.modf(a)  # Раскладываем на целую и дробную часть
    frac, whole = round(frac, 3), round(int(whole), 3)  # Делаем только 3 знака после запятой (параметр можно менять)
    frac_save, whole_save = frac, whole  # Сохраняем значения, так как будем их менять потом

    dvoich_whole = []  # Список для целой части в двоичном виде
    dvoich_frac = []  # Список для дробной части в двоичном виде

    while whole > 1:  # Пока не дойдём до конца (пока целая частьн е равна 0 или 1)
        dvoich_whole.append(math.trunc(whole % 2))  # Добавляем остаток от деления на 2
        whole = whole / 2  # Делим на 2 наше число
    dvoich_whole.reverse()  # После всего этого переворачиваем список

    for i in range(precision):  # В цикле до этой точности
        if frac == 0:  # Если мы дошли до 0, то
            break  # Выходим из цикла
        frac = frac * 2  # Умножаем дробную часть на 2
        dvoich_frac.append(math.trunc(frac))  # Добавляем целую часть
        if frac > 1:  # Если в результате умножения, дробная часть стала больше 1., то
            frac -= 1  # Вычитаем единицу
    # Складываем два наших списка, преобразовываем в строку и ставим запятую между целой и дробной частью
    dvoich_enterp = "".join(map(str, dvoich_whole)) + "," + "".join(map(str, dvoich_frac))
    return dvoich_enterp, dvoich_whole, dvoich_frac


def from10to8(a, a_dvoich_whole, a_dvoich_frac):
    oct_frac = []  # Список для дробной части, переведённой в восьмеричную систему
    while len(a_dvoich_frac) % 3 != 0:
        a_dvoich_frac.append(0)
    for i in range(len(a_dvoich_frac) // 3):  # Идём по циклу до тех пор, пока у нас триплеты не выходят за границы
        triplet = a_dvoich_frac[:3]  # Берём первые три числа от запятой
        triplet = "".join(map(str, triplet))  # Переводим в строку
        a_dvoich_frac = a_dvoich_frac[3:]  # Уменьшаем наш изначальный список
        triplet = int(triplet, base=2)  # Переводим из двоичной в десятичную
        oct_frac.append(triplet)  # Прибавляем к итоговому списку

    oct_frac = "".join(map(str, oct_frac))  # Переделываем итоговый массив в строку
    oct_whole = int("".join(map(str, a_dvoich_whole)), 2)  # Переделываем итоговый массив в строку
    oct_enterp = (oct(oct_whole)[2:] + "," + oct_frac)
    return oct_enterp


def from10to16(a, a_dvoich_whole, a_dvoich_frac):
    hex_frac = []  # Массив для шестандцатеричного представления числа
    while len(a_dvoich_frac) % 4 != 0:
        a_dvoich_frac.append(0)
    for i in range(len(a_dvoich_frac) // 4):  # Идём пока есть квадралеты
        quadro = a_dvoich_frac[:4]  # Берём первые 4 числа
        quadro = "".join(map(str, quadro))  # Преобразовываем в строку
        a_dvoich_frac = a_dvoich_frac[4:]  # Уменьшаем массивчик
        quadro = hex(int(quadro, 2))  # Переводим в 16-ричную систему из 2-чной
        hex_frac.append(quadro[2:])  # Прибавляем к итоговому списку

    hex_frac = "".join(map(str, hex_frac))  # Преобразовываем список в строку
    hex_whole = int("".join(map(str, a_dvoich_whole)), 2)  # Переделываем итоговый массив в строку
    hex_enterp = (hex(hex_whole)[2:] + "," + hex_frac)
    return hex_enterp


def from10(number, p):  # Функци преобразования числа number из 10-чной в p-тую систему счисления
    number_list = []  # Массивчик для циферок
    while number > 1:  # Пока не равно 0 или 1
        number_list.append(math.trunc(number % p))  # Добавляем остаток от деления на p - систему счисления
        number = number / p  # Делим на систему счисления
    number_list.reverse()  # Переворачиваем
    return "".join(map(str, number_list))  # Преобразовываем в красивую строку


def from2(number, p):  # Функйция преобразования числа number из 2-чной в p-тую систему счисления
    if type(number) is not str:  # Если пришла не строка, то
        number = str(number)  # Преобразовываем в строку
    for i in number:
        if int(i) >= 2:
            return 0
    if p == 10:  # Если нужно перевести в десятичную степень
        return int(number, 2)  # То просто возвращаем, преобразовывая с помощью встроенной функции
    else:  # Иначе
        number = int(number, 2)  # Преобразовываем в десятичную
        return from10(number, p)  # И отправляем в функцию выше


def fromP(number, p_in, p_out):  # Функйция преобразования числа number из p-той в любую систему счисления
    if type(number) is not str:  # Если не строка
        number = str(number)  # Преобразовываем в неё
    for i in number:
        if int(i) >= p_in:
            return 0
    number = int(number, p_in)  # Преобразовываем из заданной в десятичную систему счисления
    return from10(number, p_out)  # И снова пихаем в функцию from10 :)
