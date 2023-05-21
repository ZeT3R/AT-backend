# -*- coding: windows-1251 -*-

import math
import random


def from10to2(a, precision):
    frac, whole = math.modf(a)  # ������������ �� ����� � ������� �����
    frac, whole = round(frac, 3), round(int(whole), 3)  # ������ ������ 3 ����� ����� ������� (�������� ����� ������)
    frac_save, whole_save = frac, whole  # ��������� ��������, ��� ��� ����� �� ������ �����

    dvoich_whole = []  # ������ ��� ����� ����� � �������� ����
    dvoich_frac = []  # ������ ��� ������� ����� � �������� ����

    while whole > 1:  # ���� �� ����� �� ����� (���� ����� ������ � ����� 0 ��� 1)
        dvoich_whole.append(math.trunc(whole % 2))  # ��������� ������� �� ������� �� 2
        whole = whole / 2  # ����� �� 2 ���� �����
    dvoich_whole.reverse()  # ����� ����� ����� �������������� ������

    for i in range(precision):  # � ����� �� ���� ��������
        if frac == 0:  # ���� �� ����� �� 0, ��
            break  # ������� �� �����
        frac = frac * 2  # �������� ������� ����� �� 2
        dvoich_frac.append(math.trunc(frac))  # ��������� ����� �����
        if frac > 1:  # ���� � ���������� ���������, ������� ����� ����� ������ 1., ��
            frac -= 1  # �������� �������
    # ���������� ��� ����� ������, ��������������� � ������ � ������ ������� ����� ����� � ������� ������
    dvoich_enterp = "".join(map(str, dvoich_whole)) + "," + "".join(map(str, dvoich_frac))
    return dvoich_enterp, dvoich_whole, dvoich_frac


def from10to8(a, a_dvoich_whole, a_dvoich_frac):
    oct_frac = []  # ������ ��� ������� �����, ����������� � ������������ �������
    while len(a_dvoich_frac) % 3 != 0:
        a_dvoich_frac.append(0)
    for i in range(len(a_dvoich_frac) // 3):  # ��� �� ����� �� ��� ���, ���� � ��� �������� �� ������� �� �������
        triplet = a_dvoich_frac[:3]  # ���� ������ ��� ����� �� �������
        triplet = "".join(map(str, triplet))  # ��������� � ������
        a_dvoich_frac = a_dvoich_frac[3:]  # ��������� ��� ����������� ������
        triplet = int(triplet, base=2)  # ��������� �� �������� � ����������
        oct_frac.append(triplet)  # ���������� � ��������� ������

    oct_frac = "".join(map(str, oct_frac))  # ������������ �������� ������ � ������
    oct_whole = int("".join(map(str, a_dvoich_whole)), 2)  # ������������ �������� ������ � ������
    oct_enterp = (oct(oct_whole)[2:] + "," + oct_frac)
    return oct_enterp


def from10to16(a, a_dvoich_whole, a_dvoich_frac):
    hex_frac = []  # ������ ��� ������������������ ������������� �����
    while len(a_dvoich_frac) % 4 != 0:
        a_dvoich_frac.append(0)
    for i in range(len(a_dvoich_frac) // 4):  # ��� ���� ���� ����������
        quadro = a_dvoich_frac[:4]  # ���� ������ 4 �����
        quadro = "".join(map(str, quadro))  # ��������������� � ������
        a_dvoich_frac = a_dvoich_frac[4:]  # ��������� ���������
        quadro = hex(int(quadro, 2))  # ��������� � 16-������ ������� �� 2-����
        hex_frac.append(quadro[2:])  # ���������� � ��������� ������

    hex_frac = "".join(map(str, hex_frac))  # ��������������� ������ � ������
    hex_whole = int("".join(map(str, a_dvoich_whole)), 2)  # ������������ �������� ������ � ������
    hex_enterp = (hex(hex_whole)[2:] + "," + hex_frac)
    return hex_enterp


def from10(number, p):  # ������ �������������� ����� number �� 10-���� � p-��� ������� ���������
    number_list = []  # ��������� ��� �������
    while number > 1:  # ���� �� ����� 0 ��� 1
        number_list.append(math.trunc(number % p))  # ��������� ������� �� ������� �� p - ������� ���������
        number = number / p  # ����� �� ������� ���������
    number_list.reverse()  # ��������������
    return "".join(map(str, number_list))  # ��������������� � �������� ������


def from2(number, p):  # �������� �������������� ����� number �� 2-���� � p-��� ������� ���������
    if type(number) is not str:  # ���� ������ �� ������, ��
        number = str(number)  # ��������������� � ������
    for i in number:
        if int(i) >= 2:
            return 0
    if p == 10:  # ���� ����� ��������� � ���������� �������
        return int(number, 2)  # �� ������ ����������, �������������� � ������� ���������� �������
    else:  # �����
        number = int(number, 2)  # ��������������� � ����������
        return from10(number, p)  # � ���������� � ������� ����


def fromP(number, p_in, p_out):  # �������� �������������� ����� number �� p-��� � ����� ������� ���������
    if type(number) is not str:  # ���� �� ������
        number = str(number)  # ��������������� � ��
    for i in number:
        if int(i) >= p_in:
            return 0
    number = int(number, p_in)  # ��������������� �� �������� � ���������� ������� ���������
    return from10(number, p_out)  # � ����� ������ � ������� from10 :)
