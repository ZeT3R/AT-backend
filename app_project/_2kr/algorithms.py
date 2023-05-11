# -*- coding: windows-1251 -*-
import random

bit_depth = 8


def rev(A, bits=bit_depth):
    A = convert(A)
    if A[0] == '1':
        for i in range(len(A) - 1, 0, -1):
            if A[i] == '0':
                A[i] = '1'
            else:
                A[i] = '0'
    return A


def dop(A, bits=bit_depth):
    A = rev(A)
    if A[0] == '1':
        A = addition(A, ['1'], 'dop')

    return A


def addition(A, B, code='str'):
    while len(B) != bit_depth:
        B.insert(0, "0")

    if A[0] == '1' and code == 'str':
        A = reverse(A)
    if B[0] == '1' and code == 'str':
        B = reverse(B)

    C = ["0" for _ in range(len(A))]
    flag = False
    for i in range(len(A) - 1, -1, -1):
        if i == 0 and ((flag == True) and ((A[i] == '1' and B[i] == '0') or
                                           (A[i] == '0' and B[i] == '1'))
                       or (A[i] == '1' and B[i] == '1')):
            C = addition(C, ['1'])

        if (A[i] == '1' and B[i] == '0') or (A[i] == '0' and B[i] == '1'):
            if not flag:
                C[i] = '1'
            else:
                C[i] = '0'
        elif (A[i] == '0' and B[i] == '0'):
            if not flag:
                C[i] = '0'
            else:
                C[i] = '1'
                flag = False
        else:
            if not flag:
                C[i] = '0'
                flag = True
            else:
                C[i] = '1'

    return C


def Fullreverse(A):
    for i in range(len(A) - 1, -1, -1):
        if A[i] == '1':
            A[i] = '0'
        else:
            A[i] = '1'
    return A


def reverse(A):
    for i in range(len(A) - 1, 0, -1):
        if A[i] == '1':
            A[i] = '0'
        else:
            A[i] = '1'
    return A


def convert(A):
    if isinstance(A, int):
        A_is_minus = True if A < 0 else False

        A = bin(A)

        if not A_is_minus:
            A = list(A[2:])
        else:
            A = list(A[3:])
            A[0] = '1'

        while len(A) != bit_depth:
            A.insert(0, "0")

        if A_is_minus:
            A[0] = '1'


    else:
        if A[0] == '1':
            A = int('-0b' + ''.join(Fullreverse(reverse(A))), base=2)
        else:
            if isinstance(A, list):
                A = int('0b' + ''.join(A), base=2)

    return A


def summator(num1, num2, bits=bit_depth-1):
    A = num1
    B = num2
    if (num1 + num2 >= (2**bits)-1) or (num1 + num2 < -(2**bits)+1):
        return ("OVERFLOW")
    A_is_minus = False
    B_is_minus = False
    if A < 0:
        A_is_minus = True
    if B < 0:
        B_is_minus = True
    A = bin(A)
    B = bin(B)
    if not A_is_minus:
        A = list(A[2:])
    else:
        A = list(A[3:])

    if not B_is_minus:
        B = list(B[2:])
    else:
        B = list(B[3:])
    while len(A) != bit_depth:
        A.insert(0, "0")
    while len(B) != bit_depth:
        B.insert(0, "0")
    if A_is_minus:
        A[0] = '1'
    if B_is_minus:
        B[0] = '1'

    C = addition(A, B)
    if num1 + num2 >= 0:
        if num1 + num2 == 0 and (num1 < 0 or num2 < 0):
            return int('0b' + ''.join(Fullreverse(C)), base=2)
        else:
            return int('0b' + ''.join(C), base=2)
    else:
        return int('-0b' + ''.join(Fullreverse(C)), base=2)


def shift(A, code, shft):
    flag = True if A[0] == '1' else False

    if shft < 0:
        if flag:
            if code == 'str':
                for i in range(-shft):
                    A[2:] = A[1:-1]
                    A[1] = "0"
            else:
                for i in range(-shft):
                    A[2:] = A[1:-1]
                    A[1] = "1"

        else:
            for i in range(-shft):
                A[2:] = A[1:-1]
                A[1] = "0"

    else:
        if flag:
            if code == 'str':
                for i in range(shft):
                    if A[1] == '1':
                        A = "OVERFLOW"
                        return A
                    A[1:-1] = A[2:]
                    A[-1] = '0'
            else:
                for i in range(shft):
                    if A[1] == '0':
                        A = 'OVERFLOW'
                        return A
                    A[1:-1] = A[2:]
                    A[-1] = '1'

        else:
            for i in range(shft):
                if A[1] == '1':
                    A = "OVERFLOW"
                    return A
                A[1:-1] = A[2:]
                A[-1] = "0"

    return A
