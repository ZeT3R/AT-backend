import pandas as pd

trues = {
    'a': ['1', '0', '0', '0', '1', '1', '0', '0', '1', '1'],  # Истинные значения для a
    'b': ['1', '0', '1', '1', '0', '1', '0', '1', '1', '1'],  # Истинные значения для b
    'c': ['1', '1', '1', '0', '1', '0', '0', '0', '1', '1'],  # Истинные значения для c
    'd': ['1', '1', '0', '0', '1', '1', '1', '0', '1', '0'],  # Истинные значения для d
    'e': ['1', '0', '1', '0', '0', '1', '1', '0', '1', '0'],  # Истинные значения для e
    'f': ['1', '0', '0', '0', '0', '0', '1', '1', '1', '0'],  # Истинные значения для f
    'g': ['0', '0', '0', '1', '1', '1', '1', '0', '1', '1'],  # Истинные значения для g
    'l': ['0', '1', '0', '1', '0', '0', '1', '1', '0', '0'],  # Истинные значения для l
    'm': ['0', '0', '1', '1', '0', '0', '0', '0', '0', '1']  # Истинные значения для m
}

carno_minimization = {
    "a_0": {"TDNF": "x1 v (x2 & nx3) v (nx3 & nx4)", "TKNF": "nx3 & (x1 v x2 v nx4)"},
    "a_1": {"TDNF": "(x1 & x3) v (nx3 & x4) v (x2 & x3 & nx4)", "TKNF": "(nx3 v nx4) & (x3 v x4) & (x1 v x2 v nx3)"},
    "a_2": {"TDNF": "(x2 & x3) v (x1 & x3) v (x3 & nx4)", "TKNF": "x3 & (x1 v x2 v nx4)"},
    "a_3": {"TDNF": "(x3 & x4) v (x1 & nx3 & nx4)", "TKNF": "(nx3 v x4) & (x1 v x3) & (x3 v nx4)"},
    "a_4": {"TDNF": "(x1 & nx3) v (nx3 & nx4)", "TKNF": "nx3 & (x1 v nx4)"},
    "a_5": {"TDNF": "(nx3 & x4) v (x1 & x3 & nx4)", "TKNF": "(x3 v x4) & (nx3 v nx4) & (x1 v x4)"},
    "a_6": {"TDNF": "(x1 & x3) v (x3 & nx4)", "TKNF": "x3 & (x1 v nx4)"},
    "a_7": {"TDNF": "nx1 v (x3 & x4) v (x2 & nx3 & nx4)", "TKNF": "(nx3 v x4) & (x3 v nx4) & (nx1 v x2 v x4)"},
    "b_0": {"TDNF": "x1 v (x2 & x4) v (nx2 & nx3) v (x3 & x4)", "TKNF": "(x1 v x2 v x3 v nx4) & (nx2 v x4)"},
    "b_1": {"TDNF": "x1 v (x2 & nx4) v (nx2 & x4)", "TKNF": "(nx2 v nx4) & (x1 v x2 v x4)"},
    "b_2": {"TDNF": "(x2 & x4) v (x1 & x4) v (nx1 & nx3) v (nx2 & x3 & nx4)", "TKNF": "(nx2 v nx3 v x4) & (x1 v x2 v nx4) & (x2 v x3 v x4)"},
    "b_3": {"TDNF": "(x1 & nx4) v (nx2 & x3) v (x3 & nx4) v (nx1 & nx3 & x4)", "TKNF": "(nx2 v nx3 v nx4) & (x1 v x3 v x4) & (x2 v x3 v nx4)"},
    "b_4": {"TDNF": "(x1 & x2) v (x2 & x3) v (nx2 & x4) v (x2 & nx3 & nx4)", "TKNF": "(x2 v x4) & (x1 v x3 v nx4)"},
    "b_5": {"TDNF": "(x1 & nx4) v (x2 & x4)", "TKNF": "(x2 v nx4) & (x1 v x4)"},
    "b_6": {"TDNF": "(x1 & x4) v (x2 & x3 & nx4) v (nx2 & nx3)", "TKNF": "(x1 v nx4) & (x2 v nx3 v x4) & (nx2 v x3 v x4)"},
    "b_7": {"TDNF": "nx1 v (x2 & x3) v (x3 & nx4) V (x2 & nx4) v (nx2 & nx3 & x4)", "TKNF": "(nx2 v x3 v nx4) & (nx1 v x2 v x3 v x4) & (x2 v nx3 v nx4)"},
    "c_0": {"TDNF": "(nx2 & nx3) v (nx3 & nx4) v (nx2 & nx4)", "TKNF": "(nx2 v nx4) & (nx2 v nx3) & (nx3 v nx4)"},
    "c_1": {"TDNF": "(nx2 & x4) v (nx2 & x3) v (nx3 & x4)", "TKNF": "(x3 v x4) & (nx2 v nx3)"},
    "c_2": {"TDNF": "(nx2 & x3) v (x2 & nx4)", "TKNF": "(nx2 v nx4) & (nx1 v x3)"},
    "c_3": {"TDNF": "(x3 & x4) v (x2 & nx3)", "TKNF": "(x2 v x3) & (nx3 v x4)"},
    "c_4": {"TDNF": "(x2 & nx4) v (nx3 & nx4) v (x2 & nx3)", "TKNF": "(x2 v nx4) & (nx3 v nx4) & (x2 v nx3)"},
    "c_5": {"TDNF": "(x2 & x3) v (nx3 & x4)", "TKNF": "(x2 v nx3) & (x3 v x4)"},
    "c_6": {"TDNF": "(x2 & x3) v (nx2 & nx4)", "TKNF": "(nx2 v x3) & (x2 v nx4)"},
    "c_7": {"TDNF": "(x3 & x4) v (nx2 & nx3)", "TKNF": "(nx2 v x3) & (nx3 v x4)"},
    "d_0": {"TDNF": "(nx1 & nx3) v (x2 & nx4) v (x1 & nx4)", "TKNF": "(nx3 v nx4) & (nx1 v nx4) & (x2 v nx3)"},
    "d_1": {"TDNF": "(x2 & x3) v (nx3 & x4) v (nx1 & x3 & nx4)", "TKNF": "(x3 v x4) & (nx1 v nx4) & (x2 v nx3 v nx4)"},
    "d_2": {"TDNF": "(nx1 & x3) v (nx2 & nx4)", "TKNF": "(nx1 v nx4) & (x1 v x3)"},
    "d_3": {"TDNF": "(x3 & x4) v (nx2 & nx3) v (nx1 & nx3 & nx4)", "TKNF": "(nx3 v x4) & (nx1 v nx2) & (x1 v x3 v nx4)"},
    "d_4": {"TDNF": "(x1 & nx4) v (nx2 & nx3) v (nx1 & nx3)", "TKNF": "(nx3 v nx4) & (nx2 v nx3) & (nx1 v nx2 v nx4)"},
    "d_5": {"TDNF": "(nx3 & x4) v (nx2 & x3) v (nx1 & nx4)", "TKNF": "(x3 v x4) & (nx1 v nx2 v x4) & (nx2 v nx3 v nx4)"},
    "d_6": {"TDNF": "(x2 & nx4) v (nx2 & x3) v nx1", "TKNF": "(x2 v x3) & (nx1 v nx2 v nx4)"},
    "d_7": {"TDNF": "(x3 & x4) v (x2 & nx3) v (x1 & nx3 & nx4)", "TKNF": "(nx3 v x4) & (x1 v x3) & (x2 v x3 v nx4)"},
    "e_0": {"TDNF": "(nx2 & nx4) v (x3 & nx4) v (x2 & nx3 & x4)", "TKNF": "(nx3 v nx4) & (x2 v nx4) v (nx2 v x3 v x4)"},
    "e_1": {"TDNF": "(x2 & x3) v (nx2 & x4)", "TKNF": "(x2 v x4) & (nx2 v x3)"},
    "e_2": {"TDNF": "(nx2 & nx4) v (nx3 & nx4) v (x2 & x3 & x4)", "TKNF": "(x3 v nx4) & (x2 v nx4) & (nx2 v nx3 v x4)"},
    "e_3": {"TDNF": "(nx2 & x4) v (nx3 & x4) v (nx2 & nx3)", "TKNF": "(nx3 v x4) & (nx2 v x4) & (nx2 v nx3)"},
    "e_4": {"TDNF": "(x2 & nx4) v (x3 & nx4) & (nx2 & nx3 & x4)", "TKNF": "(nx2 v nx4) & (nx3 v nx4) & (x2 v x3 v x4)"},
    "e_5": {"TDNF": "(x2 & x4) v (nx2 & x3)", "TKNF": "(nx2 v x4) & (x2 v x3)"},
    "e_6": {"TDNF": "(x2 & nx4) v (nx3 & nx4) v (nx2 & x3 & x4)", "TKNF": "(nx2 v nx4) & (x3 v nx4) & (x2 v nx3 v x4)"},
    "e_7": {"TDNF": "(x2 & x4) v (x2 & nx3) v (nx3 & x4)", "TKNF": "(nx3 v x4) & (x2 v x4) & (x2 v nx3)"},
    "f_0": {"TDNF": "(x2 & x3) v (nx2 & nx3 & nx4)", "TKNF": "(nx2 v x3) & (x2 v nx3) & (x2 v nx4)"},
    "f_1": {"TDNF": "(nx2 & nx3) v (x2 & x3 & x4)", "TKNF": "(nx2 v x3) & (nx3 v x4) & (x2 v nx3)"},
    "f_2": {"TDNF": "(nx2 & nx4) v (nx2 & nx3)", "TKNF": "(nx2 & (nx3 v nx4)"},
    "f_3": {"TDNF": "(nx2 & x4) v (nx2 & x3)", "TKNF": "nx2 & (x3 v x4)"},
    "f_4": {"TDNF": "(nx2 & x3) v (x2 & nx3 & nx4)", "TKNF": "(nx2 v nx4) & (x2 v x3) & (x1 v nx3)"},
    "f_5": {"TDNF": "(x2 & nx3) v (x1 & x3 & x4)", "TKNF": "(nx2 v nx3) & (x2 v x3) & (x2 v x4)"},
    "f_6": {"TDNF": "(x2 & nx3) v (x2 & nx4)", "TKNF": "x2 & (nx3 v nx4)"},
    "f_7": {"TDNF": "(x2 & x3) v (x2 & x4)", "TKNF": "x2 & (x3 v x4)"},
    "g_0": {"TDNF": "x1 v (x2 & nx3) v (x2 & nx4) v (nx2 & x3 & x4)", "TKNF": "(x1 v x2 v x4) & (nx2 v nx3 v nx4) & (x1 v x2 v x3)"},
    "g_1": {"TDNF": "x2 v (x1 & x4) v (x1 & x3)", "TKNF": "(x1 v x2) & (x2 v x3 v x4)"},
    "g_2": {"TDNF": "(x2 & x3) v (x1 & x3) v (x2 & x4) v (x1 & nx4)", "TKNF": "(x1 v x2) & (x2 v x3 v nx4) & (x1 v x3 v x4)"},
    "g_3": {"TDNF": "(x1 & x4) v (x1 & nx3) v (x2 & x3)", "TKNF": "(x1 v x3) & (x1 v x2) & (x2 v nx3 v x4)"},
    "g_4": {"TDNF": "(x1 & nx3) v (nx2 & nx4) v (x2 & x3 & x4)", "TKNF": "(x1 v x4) & (x1 v x3) & (x2 v nx3 v nx4)"},
    "g_5": {"TDNF": "nx2 v (x1 & x3) v (x1 & x4)", "TKNF": "x1 & (nx2 v x3 v x4)"},
    "g_6": {"TDNF": "(x1 & x3) v (nx2 & x4) v (x1 & x2 & nx4)", "TKNF": "x1 & (x2 v x3 v x4) & (nx2 v x3 v nx4)"},
    "g_7": {"TDNF": "(x2 & nx3) v (nx2 & x3) v (nx1 & nx3) v (x1 & x2 & x4)", "TKNF": "(nx1 v x2 v x3) & (nx2 v nx3 v x4) & (x1 v nx3)"},
    "l_0": {"TDNF": "(x2 & x3) v (nx1 & nx2 & x4)", "TKNF": "nx1 & (nx2 v x3) & (x2 v x4)"},
    "l_1": {"TDNF": "(nx3 & nx4) v (nx1 & nx2 & nx4) v (x2 & x3 & x4)", "TKNF": "(x3 v nx4) & (x2 v nx4) & (nx1 v nx3) & (nx2 v nx3 v x4)"},
    "l_2": {"TDNF": "(x1 & nx3) v (nx3 & x4) v (nx1 & nx2 & x4)", "TKNF": "(x1 v x4) & (nx1 v nx3) & (nx2 v nx3)"},
    "l_3": {"TDNF": "(nx1 & nx4) v (x3 & nx4) v (x1 & nx3 & x4)", "TKNF": "(x1 v nx4) & (nx3 v nx4) v (nx1 v x3 v x4)"},
    "l_4": {"TDNF": "(nx1 & x4) v (x1 & x3)", "TKNF": "(nx1 v x3) & (x1 v x4)"},
    "l_5": {"TDNF": "(nx3 & nx4) v (nx1 & nx4) v (x1 & x3 & x4)", "TKNF": "(x3 v nx4) & (x1 v nx4) & (nx1 v nx3 v x4)"},
    "l_6": {"TDNF": "(x2 & nx3) v (nx3 & x4) v (nx1 & x4)", "TKNF": "(nx1 v nx3) & (nx3 v x4) & (x2 v x4)"},
    "l_7": {"TDNF": "(x3 & nx4) v (x1 & nx2 & nx4) v (x2 & nx3 & x4)", "TKNF": "x1 & (nx3 v nx4) & (x2 v nx4) & (nx2 v x3 v x4)"},
    "m_0": {"TDNF": "(x1 & x4) v (nx2 & x3)", "TKNF": "nx2 & (x1 v x3) & (x3 v x4)"},
    "m_1": {"TDNF": "(x1 & x3) v (nx2 & x3 & x4) v (x2 & nx3 & nx4)", "TKNF": "(nx2 v nx3) & (x3 v nx4) & (x2 v x3) & (x1 v x2 v x4)"},
    "m_2": {"TDNF": "(x2 & nx3) v (x1 & x3 & x4)", "TKNF": "(x1 v nx3) & (x2 v x4) & (x2 v x3)"},
    "m_3": {"TDNF": "(x1 & x2) v (x2 & x3 & nx4) v (x2 & nx3 & x4)", "TKNF": "x2 & (nx3 v nx4) & (x1 v x3 v x4)"},
    "m_4": {"TDNF": "(x2 & x3) v (x1 & x2 & x4)", "TKNF": "x2 & (x1 v x3) & (x3 v x4)"},
    "m_5": {"TDNF": "(x1 & x2 & x3) v (x2 & x3 & x4) v (nx2 & nx3 & nx4)", "TKNF": "(x2 v nx3) & (x3 v nx4) & (nx2 v x3) & (x1 v x4)"},
    "m_6": {"TDNF": "(nx2 & nx3) v (x1 & x2 & x3 & x4)", "TKNF": "x1 & (x2 v nx3) & (nx2 v x3) & (nx3 v x4)"},
    "m_7": {"TDNF": "(nx2 & x3 & nx4) v (nx1 & nx4) v (nx2 & nx3 & x4)", "TKNF": "nx2 & (nx3 v nx4) & (nx1 v x3 v x4)"}
}

import copy  # Для хард копирования значений таблицы
import numpy as np  # Для поворота матрицы
from thefuzz import fuzz as f


def Pirs(Tknf):
    Tknf = list(Tknf)  # Превартили в список
    Tknf = [">" if x == "&" or x == "v" else x for x in Tknf]  # Заменили все знаки на стрелочку
    for i, val in enumerate(Tknf):  # Пробегаемся по символам
        if val == "n":  # Если встретили н
            x_save = ''.join(Tknf[i + 1]) + Tknf[i + 2]  # Берём икс и цифру, без н
            del Tknf[i:i + 2]  # удаляем nxX
            Tknf[i] = '(' + x_save + " > " + x_save + ')'  # собираем строчку
    Tknf = ''.join(Tknf)  # переводим в строку
    return Tknf  # возвращаем



def Kvaina_DNF(Fsdnf):
    for i in range(len(Fsdnf)):
        Fsdnf[i] = Fsdnf[i].replace(' ', '')
        Fsdnf[i] = Fsdnf[i].replace('(', '')
        Fsdnf[i] = Fsdnf[i].replace(')', '')
    term_list = [[""] * 0 for i in range(len(Fsdnf))]
    for i in range(len(Fsdnf)):
        term = Fsdnf[i]  # Берём первый терм
        for k in range(term.count('&') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('&')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list[i].append(term[:split])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list[i].append(term)  # Берём всё кроме скобок

    final_list = []
    nnn = term_list.copy()
    for i in range(len(nnn)):
        terms = nnn[i]
        for j in range(len(nnn)):
            if terms == nnn[j]:
                continue
            else:
                temp = terms.copy()
                if f.ratio(terms, nnn[j]) >= 97:
                    # print(terms, 'Минимизируется с ', term_list[j], '\n')
                    for k in range(len(terms)):
                        if (terms[k] != nnn[j][k]):
                            temp.pop(k)
                            term_list.append(temp)
                            final_list.append(terms)
                            break

    import itertools

    final_list.sort()

    final_list = list(final_list for final_list, _ in itertools.groupby(final_list))
    term_list.sort()
    term_list[:] = [x for x in term_list if x not in final_list]
    term_list = list(term_list for term_list, _ in itertools.groupby(term_list))

    ret = []
    for i in range(len(term_list)):
        ret.append('&'.join(term_list[i]))
    return (ret)


def Kvaina_KNF(Fsknf):
    for i in range(len(Fsknf)):
        Fsknf[i] = Fsknf[i].replace(' ', '')
        Fsknf[i] = Fsknf[i].replace('(', '')
        Fsknf[i] = Fsknf[i].replace(')', '')
    term_list = [[""] * 0 for i in range(len(Fsknf))]
    for i in range(len(Fsknf)):
        term = Fsknf[i]  # Берём первый терм
        for k in range(term.count('v') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('v')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list[i].append(term[:split])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list[i].append(term)  # Берём всё кроме скобок

    final_list = []
    nnn = term_list.copy()
    for i in range(len(nnn)):
        terms = nnn[i]
        for j in range(len(nnn)):
            if terms == nnn[j]:
                continue
            else:
                temp = terms.copy()
                if f.ratio(terms, nnn[j]) >= 97:
                    # print(terms, 'Минимизируется с ', term_list[j], '\n')
                    for k in range(len(terms)):
                        if (terms[k] != nnn[j][k]):
                            temp.pop(k)
                            term_list.append(temp)
                            final_list.append(terms)
                            break

    import itertools

    final_list.sort()

    final_list = list(final_list for final_list, _ in itertools.groupby(final_list))
    term_list.sort()
    term_list[:] = [x for x in term_list if x not in final_list]
    term_list = list(term_list for term_list, _ in itertools.groupby(term_list))

    ret = []
    for i in range(len(term_list)):
        ret.append('v'.join(term_list[i]))
    return (ret)


def Quine_McCluskey(function, ftype, my_var):
    zero_count = 0
    K00 = []
    K01 = []
    K02 = []
    K03 = []
    K04 = []
    for i in range(len(function)):
        if function[i].count('0') > zero_count:
            zero_count = function[i].count('0')
    if zero_count == 4:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K00.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K01.append(function[i])
            elif function[i].count('0') == zero_count - 2:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 3:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 3:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K01.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 2:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 2:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K02.append(function[i])
            elif function[i].count('0') == zero_count - 1:
                K03.append(function[i])
            else:
                K04.append(function[i])
    elif zero_count == 1:
        for i in range(len(function)):
            if function[i].count('0') == zero_count:
                K03.append(function[i])
            else:
                K04.append(function[i])
    else:
        for i in range(len(function)):
            K04.append(function[i])

    K0 = K00.copy()
    K1 = K01.copy()
    K2 = K02.copy()
    K3 = K03.copy()
    cube1 = []
    counter = 0
    equal = 0

    if len(K00) > 0:
        for i in range(len(K00)):
            for j in range(len(K01)):
                for k in range(len(K00[i])):
                    if K00[i][k] != K01[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K00[i])):
                        if K00[i][k] != K01[j][k]:
                            cube1.append(''.join(K00[i][:k] + 'x' + K00[i][k + 1:]))
                            if K00[i] in K0:
                                K0.remove(K00[i])
                            if K01[j] in K1:
                                K1.remove(K01[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K01)):
            for j in range(len(K02)):
                for k in range(len(K01[i])):
                    if K01[i][k] != K02[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            cube1.append(''.join(K01[i][:k] + 'x' + K01[i][k + 1:]))
                            if K01[i] in K1:
                                K1.remove(K01[i])
                            if K02[j] in K2:
                                K2.remove(K02[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0


    elif len(K01) > 0:
        for i in range(len(K01)):
            for j in range(len(K02)):
                for k in range(len(K01[i])):
                    if K01[i][k] != K02[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K01[i])):
                        if K01[i][k] != K02[j][k]:
                            cube1.append(''.join(K01[i][:k] + 'x' + K01[i][k + 1:]))
                            if K01[i] in K1:
                                K1.remove(K01[i])
                            if K02[j] in K2:
                                K2.remove(K02[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    elif len(K02) > 0:
        for i in range(len(K02)):
            for j in range(len(K03)):
                for k in range(len(K02[i])):
                    if K02[i][k] != K03[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K02[i])):
                        if K02[i][k] != K03[j][k]:
                            cube1.append(''.join(K02[i][:k] + 'x' + K02[i][k + 1:]))
                            if K02[i] in K2:
                                K2.remove(K02[i])
                            if K03[j] in K3:
                                K3.remove(K03[j])
                else:
                    counter = 0

        equal = 0
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    elif len(K03) > 0:
        for i in range(len(K03)):
            for j in range(len(K04)):
                for k in range(len(K03[i])):
                    if K03[i][k] != K04[j][k]:
                        counter += 1
                if counter == 1:
                    for k in range(len(K03[i])):
                        if K03[i][k] != K04[j][k]:
                            cube1.append(''.join(K03[i][:k] + 'x' + K03[i][k + 1:]))
                            if K03[i] in K3:
                                K3.remove(K03[i])
                else:
                    counter = 0

    else:
        cube1 = K04

    K11, K12, K13, K14 = [], [], [], []

    cube1 += K0 + K1 + K2 + K3

    for i in range(len(cube1)):
        if cube1[i][0] == 'x':
            K11.append(cube1[i])
        elif cube1[i][1] == 'x':
            K12.append(cube1[i])
        elif cube1[i][2] == 'x':
            K13.append(cube1[i])
        else:
            K14.append(cube1[i])

    final = []
    test = []

    counter = 0
    for i in range(len(K11)):
        if len(K11) == 1:
            final.append(K11[0])
            break
        for j in range(len(K11)):
            if i == j:
                continue
            for k in range(len(K11[i])):
                if K11[i][k] != K11[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K11[i])):
                    if K11[i][k] != K11[j][k]:
                        final.append(''.join(K11[i][:k] + 'x' + K11[i][k + 1:]))
            else:
                counter = 0
                test.append(K11[i])

    counter = 0
    for i in range(len(K12)):
        if len(K12) == 1:
            final.append(K12[0])
            break
        for j in range(len(K12)):
            if i == j:
                continue
            for k in range(len(K12[i])):
                if K12[i][k] != K12[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K12[i])):
                    if K12[i][k] != K12[j][k]:
                        final.append(''.join(K12[i][:k] + 'x' + K12[i][k + 1:]))
            else:
                counter = 0
                test.append(K12[i])

    counter = 0
    for i in range(len(K13)):
        if len(K13) == 1:
            final.append(K13[0])
            break
        for j in range(len(K13)):
            if i == j:
                continue
            for k in range(len(K13[i])):
                if K13[i][k] != K13[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K13[i])):
                    if K13[i][k] != K13[j][k]:
                        final.append(''.join(K13[i][:k] + 'x' + K13[i][k + 1:]))
            else:
                counter = 0
                test.append(K13[i])

    counter = 0
    for i in range(len(K14)):
        if len(K14) == 1:
            final.append(K14[0])
            break
        for j in range(len(K14)):
            if i == j:
                continue
            for k in range(len(K14[i])):
                if K14[i][k] != K14[j][k]:
                    counter += 1
            if counter == 1:
                for k in range(len(K14[i])):
                    if K14[i][k] != K14[j][k]:
                        final.append(''.join(K14[i][:k] + 'x' + K14[i][k + 1:]))
            else:
                counter = 0
                test.append(K14[i])

    final += test

    import itertools
    final.sort()
    final = list(final for final, _ in itertools.groupby(final))

    ret_final = []
    term = ''
    for i in range(len(final)):
        for j in range(len(final[i])):
            if final[i][j] == '0' and ftype == 'DNF':
                term = term + 'n' + my_var.columns[j]
            elif final[i][j] == '0' and ftype == 'KNF':
                term = term + my_var.columns[j]
            elif final[i][j] == '1' and ftype == 'DNF':
                term = term + my_var.columns[j]
            elif final[i][j] == '1' and ftype == 'KNF':
                term = term + 'n' + my_var.columns[j]
            else:
                continue
            if ftype == 'DNF':
                term = term + ' & '
            else:
                term = term + ' v '
        term = term[:-3]
        ret_final.append(term)
        term = ''
    for i in range(len(ret_final)):
        ret_final[i] = ret_final[i].replace(" ", "")
    return ret_final


def check_Table_tdnf(table, splitTdnf):
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(splitTdnf)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = splitTdnf[i]  # Берём первый терм
        for k in range(term.count('&') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('&')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                if len(term) == 2 or (len(term) == 3 and term.find("n")):
                    term_list.append(term)
                else:
                    term_list.append(term[1:-1])  # Берём всё кроме скобок
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '&'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                if (keys[j].find('n') != -1):  # Если ключ называется nx что-то
                    col = keys[j].replace("n", '')  # Убираем букву n у col
                    if table[col][count] == '1':  # Если в таблице 1
                        term_list[keys[j]].append('0')  # То меняем на 0 (Инверсия)
                    else:  # Если же 0
                        term_list[keys[j]].append('1')  # То ставим 1
                else:  # Если не нашли n,
                    term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборка
        for l in range(16):  # 16 значений
            fin.append(int(term_list[keys[0]][l]))  # запоминаем значения по первому ключу
        for h in range(1, len(keys)):  # От 1 (0 мы уже запомнили) до количества ключей
            for l in range(16):  # 16 значений там
                fin[l] = fin[l] & int(term_list[keys[h]][l])  # ПОбитовое умножение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = list(table.columns)[4] + "="
    name = name + 'v'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя
    fin = []  # Обнуляем
    for l in range(16):  # 16 значений
        fin.append(int(table_changed[names[0]][l]))  # Берём значения первого столбца
    for h in range(1, len(names) - 1):  # Идём по всем столбцам крое первого
        for l in range(16):  # 16 значений
            fin[l] = fin[l] | table_changed[names[h]][l]  # И делаем побитовое сложение между ними
    table_changed[names[len(names) - 1]] = fin  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


# То же самое и для СКНФ. Комментарии прошлой фунции актуальны и для этой:

def check_Table_tknf(table, splitTknf):
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Массив для буковок
    for i in range(len(splitTknf)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = splitTknf[i]  # Берём первый терм
        for k in range(term.count('v') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('v')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                if len(term) == 2 or (len(term) == 3 and term.find("n")):
                    term_list.append(term)
                else:
                    term_list.append(term[1:-1])  # Берём всё кроме скобок
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи

        order = "KLMNOPRST"  # Список с названиями столбцов
        name = 'v'.join(keys)  # ФОрмируем строку
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Добавляем букву
        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                if (keys[j].find('n') != -1):  # Если ключ называется nx что-то
                    col = keys[j].replace("n", '')  # Убираем букву n у col
                    if table[col][count] == '1':  # Если в таблице 1
                        term_list[keys[j]].append('0')  # То меняем на 0 (Инверсия)
                    else:  # Если же 0
                        term_list[keys[j]].append('1')  # То ставим 1
                else:  # Если не нашли n,
                    term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборка
        for l in range(16):  # 16 значений
            fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
        for h in range(1, len(keys)):  # По всем ключам кроме первого
            for l in range(16):  # 16 значений
                fin[l] = fin[l] | int(term_list[keys[h]][l])  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = list(table.columns)[4] + "="
    name = name + '&'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя
    fin = []  # Обнуляем
    for l in range(16):  # 16 значений
        fin.append(int(table_changed[names[0]][l]))  # Берём значения первого столбика
    for h in range(1, len(names) - 1):  # Все значения из столбцов, кроме первого
        for l in range(16):  # 16 значений
            fin[l] = fin[l] & table_changed[names[h]][l]  # Побитовое умножение между ними
    table_changed[names[len(names) - 1]] = fin  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


def Split_Pirs(Tknf_pirs):
    tknf_check = []  # создали список
    for i in range(Tknf_pirs.count(") > (") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if (Tknf_pirs.find(') > (') != -1):  # если нашли знак
            tknf_check.append(Tknf_pirs[:Tknf_pirs.find(") > (") + 1])  # добавляем всё до знака
            Tknf_pirs = ''.join(Tknf_pirs[Tknf_pirs.find(") > (") + 4:])  # Срезаем строку
    else:  # Если нет знака
        tknf_check.append(Tknf_pirs)  # Значит срезали всё до последнего терма. ПРосто прибавляем
    return tknf_check  # Возвраащем


def Split_Sheffer(Tdnf_sheffer):
    tdnf_check = []  # создали список
    for i in range(Tdnf_sheffer.count(") / (") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if Tdnf_sheffer.find(') / (') != -1:
            tdnf_check.append(Tdnf_sheffer[:Tdnf_sheffer.find(") / (") + 1])  # добавляем всё до знака
            Tdnf_sheffer = ''.join(Tdnf_sheffer[Tdnf_sheffer.find(") / (") + 4:])  # Срезаем строку
    else:  # Если нет знака
        tdnf_check.append(Tdnf_sheffer)  # Значит срезали всё до последнего терма. ПРосто прибавляем
        # print(tdnf_check)
    return tdnf_check  # Возвраащем


def check_Table_Pirs(table, Tknf_pirs):
    # print(pirs)
    pirs = Split_Pirs(Tknf_pirs)
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(pirs)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = pirs[i]  # Берём первый терм
        for k in range(term.count('>') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('>')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list.append(term[1:-1])  # Берём всё кроме скобок
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '>'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборкf
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[-1]][l]))  # Первый ключ - все значения
            # for h in range(len(keys)-1, -4, -1): # По всем ключам кроме первого
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # Побитовое сложение
        else:
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
            for h in range(1, len(keys)):  # По всем ключам кроме первого
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] | int(term_list[keys[h]][l])))  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = list(table.columns)[4] + "="
    name = name + '>'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя

    final_col = []
    final_col = (table.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


def check_Table_Sheffer(table, Tdnf_sheffer):
    # print(pirs)
    sheffer = Split_Sheffer(Tdnf_sheffer)
    table_changed = table.copy()  # Сохраняеи таблицу, чтобы не изменить её
    names = []  # Имена для столбцов новой таблицы
    orders = []  # Имена для последоватлньости буковок в столбцах
    for i in range(len(sheffer)):  # Сколько термов расспличенных
        term_list = []  # Создаём список
        term = sheffer[i]  # Берём первый терм
        for k in range(term.count('/') + 1):  # Бежим по количеству знаков определённом терме
            split = term.find('/')  # Ищем позицию знака
            if (split != -1):  # Если знаки есть
                term_list.append(term[1:split - 1])  # Берём всё до знака (Кроме скобки в начале и пробела)
                term = term[split + 1:]  # Срезаем всё до знака и берём то, что осталось
            else:  # Если же больше нет знака
                term_list.append(term[1:-1])  # Берём всё кроме скобок
        check = term_list[0]
        for j in range(1, len(term_list)):
            if check == term_list[j]:
                term_list[j] = term_list[j] + ')'
            check = term_list[j]
        term_list = dict.fromkeys(term_list, [])  # Переводим в слвоарь
        keys = list(term_list)  # Запоминаем ключи
        order = "KLMNOPRST"  # Список с названиями столбцов
        name = '/'.join(keys)  # Соединяем ключи (иксы) и между ними ставим знак
        if name[0] == '(':
            name = name + ')'
        elif name[-1] == ')' and name.find('(') == -1:
            name = '(' + name
        names.append(order[i] + '=' + name)  # Собираем название
        orders.append(order[i])  # Берём итую букву из строки
        for j in range(len(keys)):
            keys[j] = keys[j].replace('(', '')
            keys[j] = keys[j].replace(')', '')

        for j in range(len(term_list)):  # Идёт по каждому иксу
            col = keys[j]  # Запоминаем значение ключа
            term_list[col] = []  # зануляем значение списка значений
            for count in range(16):  # 16 значений всего
                term_list[col].append(table[col][count])  # То заполняем так как есть
        fin = []  # Финальная сборкf
        if names[i].count('(') > 0 and names[i].count(')') > 0 and names[i][2] != '(':
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[-1]][l]))  # Первый ключ - все значения
            # for h in range(len(keys)-1, -4, -1): # По всем ключам кроме первого
            for h in range(len(keys) - 2, -1, -1):
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # Побитовое сложение
        else:
            for l in range(16):  # 16 значений
                fin.append(int(term_list[keys[0]][l]))  # Первый ключ - все значения
            for h in range(1, len(keys)):  # По всем ключам кроме первого
                for l in range(16):  # 16 значений
                    fin[l] = int(not (fin[l] & int(term_list[keys[h]][l])))  # Побитовое сложение
        table_changed[names[i]] = fin  # Создаём столбец со значениями в таблице
    name = list(table.columns)[4] + "="
    name = name + '/'.join(orders)  # Формируем название последнего столбца
    names.append(name)  # Добавляем новое имя

    final_col = []
    final_col = (table.iloc[:, -1])

    table_changed[names[len(names) - 1]] = final_col  # Создаём последний столбец в таблице
    # table_changed.pop("СДНФ") # Удаляем из таблицы колонки СДНФ
    # table_changed.pop("СКНФ") # И СКНФ
    return table_changed  # Возвращаем


def Split_Tdnf(Tdnf):
    tdnf_check = []  # создали список
    for i in range(Tdnf.count("v") + 1):  # Смотрим, сколько знаков и прибавляем 1 к значению
        if (Tdnf.find('v') != -1):  # если нашли знак
            tdnf_check.append(Tdnf[:Tdnf.find("v") - 1])  # добавляем всё до знака
            Tdnf = ''.join(Tdnf[Tdnf.find("v") + 2:])  # Срезаем строку
    else:  # Если нет знака
        tdnf_check.append(Tdnf)  # Значит срезали всё до последнего терма. ПРосто прибавляем
    return tdnf_check  # Возвраащем


def Split_Tknf(Tknf):  # То же самое для КНФ
    tknf_check = []  # Список
    for i in range(Tknf.count("&") + 1):  # До количества знаков + 1
        if (Tknf.find('&') != -1):  # Если нашли
            tknf_check.append(Tknf[:Tknf.find("&") - 1])  # Берём всё до него
            Tknf = ''.join(Tknf[Tknf.find("&") + 2:])  # Берём всё после него и взятых термов
    else:  # Если больше нет
        tknf_check.append(Tknf)  # Просто прибавяем

    return tknf_check  # Возвращаем


def Sheffer(Tdnf):
    Tdnf = list(Tdnf)  # переводим в список
    Tdnf = ["/" if x == "&" or x == "v" else x for x in Tdnf]  # меняем на чёрточку все знаки
    for i, val in enumerate(Tdnf):  # пробегаемся по значениям
        if val == "n":  # встретили н
            x_save = ''.join(Tdnf[i + 1]) + Tdnf[i + 2]  # записали икс с цифрой
            del Tdnf[i:i + 2]  # удалили н и икс с цифрой
            Tdnf[i] = '(' + x_save + " / " + x_save + ')'  # Собрали строчку
    Tdnf = ''.join(Tdnf)  # преобразовали в строку
    return Tdnf  # вернули


def format_DNF(NF):
    for i in range(len(NF)):
        NF[i] = '(' + NF[i] + ')'
    NF = ' v '.join(NF)
    return NF


def format_KNF(NF):
    for i in range(len(NF)):
        NF[i] = '(' + NF[i] + ')'
    NF = ' & '.join(NF)
    return NF


def create_carno(var_seg):  # Функция создания карты Карно
    Carno = [['', '', '', ''],  # Будем делать её в двумерном списке
             ['', '', '', ''],  # Получится, как двумерный массив
             ['', '', '', ''],
             ['', '', '', '']]

    counter = 0  # Счётчик
    for i in range(4):  # 4 строки
        for j in range(4):  # 4 столбца
            if (var_seg[counter]) == 'x':  # Если у нас х в столбце b
                Carno[i][j] = 'x'  # то и ставим в таблицу х
            elif (var_seg[counter]) == '1':  # Если единица
                Carno[i][j] = '1'  # То и ставим единицу
            else:  # Ну и остаётся ноль
                Carno[i][j] = '0'  # Его и записываем
            counter += 1  # Каждый раз увеличиваем счётчик

    Carno_save = copy.deepcopy(Carno)  # Копируем таблицу, сохраняем её, ибо начинается веселье

    #                                        1 ШАГ
    ##############################################################################################
    # Здесь мы меняем значения крест-накрест
    Carno[0][2] = Carno_save[1][0]
    Carno[0][3] = Carno_save[1][1]
    Carno[1][0] = Carno_save[0][2]
    Carno[1][1] = Carno_save[0][3]

    Carno[2][2] = Carno_save[3][0]
    Carno[2][3] = Carno_save[3][1]
    Carno[3][0] = Carno_save[2][2]
    Carno[3][1] = Carno_save[2][3]
    ###############################################################################################

    #                                       2 ШАГ
    ###############################################################################################
    # Здесь мы меняем столбцы местами
    Carno_save = copy.deepcopy(Carno)  # Снова сохраняем уже новую карту Карно

    for i in range(4):
        for j in range(4):
            if i < 2:
                Carno[j][i] = Carno_save[j][i + 2]
            elif i == 2:
                Carno[j][i] = Carno_save[j][i - 1]
            else:
                Carno[j][i] = Carno_save[j][i - 3]
    ###############################################################################################

    #                                      3 и 4 ШАГИ
    ###############################################################################################
    # # Переворачиваем карту Карно на 90 градусов ПРОТИВ часовой стрелки (axes(0, 1) - по часовой)
    # Мы ставим axes(1, 0), что позволит нам перевернуть её ПРОТИВ часовой стрелки.
    Carno = np.rot90(Carno, axes=(1, 0))
    Carno_save = copy.deepcopy(Carno)  # Снова сохраняем уже перевёрнутую карту

    # Меняем первый и второй столбец местами
    for i in range(2):
        for j in range(4):
            if i == 0:
                Carno[j][i] = Carno_save[j][i + 1]
            else:
                Carno[j][i] = Carno_save[j][i - 1]
    ###############################################################################################

    return Carno  # Получаем результат


def create_var(b, offset, seg):  # Функция создания таблицы под определённый вариант
    dataframe = pd.DataFrame(trues)
    # Словарь со значениями x1-x4. Он всегда будет одинаковым.
    ix = {'x1': ['0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
          'x2': ['0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1'],
          'x3': ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1'],
          'x4': ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']}
    target = {seg: []}  # Создаём словарик, в нём ключ b и не записываем туда значения
    for i in range(offset):  # От 0 до значения смещения
        target[seg].append('x')  # Запихиваем иксы (это как раз смещение от начала, зависит от варианта)
    for i in range(len(b)):  # После этого мы
        target[seg].append(b[i])  # Запихиваем в словарик все значения по варианту. В данном случае b_true
    while len(target[seg]) != 16:  # Если после всех махинаций, у нас есть пустые значения, то
        target[seg].append('x')  # Дозаполняем их иксами
    final = pd.DataFrame.from_dict(ix)  # Создаём датафрейм из словаря с иксами
    final[seg] = target[seg]  # Создаём новый столбец из нашего словаря по варианту
    return final  # И возвращаем


def modify_str(func, t_func):  # Функция изменения строки. Меняет нули и единицы на буквенные обозначения
    func = list(func)  # Переводим функцию в список
    if t_func == 'SDNF':  # Если СДНФ
        for i in range(4):  # 4 терма
            if func[i] == '0':  # Если у нас нолик, то
                func[i] = ' nx' + str(i + 1) + ' &'  # Пишем не икс i+1. У нас же с нуля, а там с x1.
            else:  # Иначе, если у нас 1
                func[i] = ' x' + str(i + 1) + ' &'  # Просто икс. В конце добавляем знак умножения
    else:  # Если же СКНФ
        for i in range(4):  # 4 терма
            if func[i] == '0':  # Если ноль
                func[i] = ' nx' + str(i + 1) + ' v'  # Делаем то же самое, ибо мы развернули заранее
            else:  # Если 1
                func[i] = ' x' + str(i + 1) + ' v'  # То же самое, что и СДНФ, только в конце знак сложения

    func = ''.join(func)  # Переводим в строку
    return func  # Возвращаем


def modify_var(var_table, offset, seg):  # Функция модификации таблицы (добавления столбцов и их заполнение)
    SDKNF = {'SDNF': [], 'SKNF': []}  # Создаём словари для функций
    Fsdnf, Fsknf = [], []  # Создаём списки для возврата значения, как по методичке
    for i in range(16):  # 16 строк у нас всего. ИЗначально их надо заполнить прочерками (-)
        SDKNF['SDNF'].append('-')  # Заполняем
        SDKNF['SKNF'].append('-')  # Заполняем
    var_table['SDNF'] = SDKNF['SDNF']  # Впихиваем в таблицу
    var_table['SKNF'] = SDKNF['SKNF']  # Впихиваем в таблицу
    func = ''  # Наша функция СДНФ/СКНФ
    func_list_DNF = []
    func_list_KNF = []
    for i in range(offset, offset + 10):  # Идём от конца смещения до смещения + 10 (Ибо 10 значений)
        if var_table[seg][i] == '1':  # Если в столбце seg у нас стоит 1, значит
            # Значит, что у нас СДНФ столбец заполнять надо. Мы присваиваем функции значения
            # столбцов x1, x2, x3, x4 так, как они есть, те же цифры
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_DNF.append(func)
            func = modify_str(func, 'SDNF')  # Запихиваем в функцию изменения строки
            func = list(func)  # Снова преобразовываем в список
            func.pop()  # Вытаскиваем последний элемент, то есть v
            func.append(")")  # Добавляем в конец закрывающую скобку
            func.insert(0, '(')  # И в начало добавляем открывающую скобку
            func = ''.join(func)  # Снова переводим в строку
            var_table.at[i, 'SDNF'] = func  # Ставим строку значением в нашем столбце
            Fsdnf.append(func)  # И добавляем в массив полной функции СДНФ
        else:  # Если же у нас нолик в столбце b, то
            # То значит, что у нас СКНФ вступает в бой. Здесь нужно предварителньо инвертировать
            # значения, чтобы получить правильный результат. Изначально пихаем обычные значения
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_KNF.append(func)
            func = list(func)  # Переводим в список
            for j in range(4):  # 4 терма
                if (func[j] == '0'):  # Если был 0
                    func[j] = '1'  # Станет 1
                else:  # Если была 1
                    func[j] = '0'  # Станет 0
            func = modify_str(func, 'SKNF')  # Преобразовываем строку
            func = list(func)  # Снова в список
            func.pop()  # Вытаскиваем лишний символ
            func.append(")")  # Добавляем в конец закрывающую скобку
            func.insert(0, '(')  # И в начало добавляем открывающую скобку
            func = ''.join(func)  # Снова в строку
            var_table.at[i, 'SKNF'] = func  # Добавляем значение в таблицу
            Fsknf.append(func)  # И прибавляем в финальный список функции СКНФ
    return var_table, Fsdnf, Fsknf, func_list_DNF, func_list_KNF