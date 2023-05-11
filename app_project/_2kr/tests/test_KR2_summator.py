# -*- coding: windows-1251 -*-

import sys

sys.path.append("..")
import unittest
import algorithms as kr


class test_KR2_summator(unittest.TestCase):

    def test_summator(self):
        for i in range(128):
            for j in range(128):
                A = i
                B = j
                if (i + j >= 127):
                    continue
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
                    A[0] = '1'
                if not B_is_minus:
                    B = list(B[2:])
                else:
                    B = list(B[3:])
                bit_depth = 8
                while len(A) != bit_depth:
                    A.insert(0, "0")
                while len(B) != bit_depth:
                    B.insert(0, "0")
                if A_is_minus:
                    A[0] = '1'
                if B_is_minus:
                    B[0] = '1'

                C = kr.addition(A, B)

                with self.subTest(i=i, j=j):
                    self.assertEqual(i + j, int('0b' + ''.join(C), base=2))

    def test_summator_minusA(self):
        for i in range(128):
            for j in range(128):
                A = -i
                B = j
                if (i + j >= 127):
                    continue
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
                bit_depth = 8
                while len(A) != bit_depth:
                    A.insert(0, "0")
                while len(B) != bit_depth:
                    B.insert(0, "0")
                if A_is_minus:
                    A[0] = '1'
                if B_is_minus:
                    B[0] = '1'

                C = kr.addition(A, B)

                with self.subTest(i=i, j=j):
                    if -i + j >= 0:
                        if -i + j == 0 and -i < 0:
                            self.assertEqual(-i + j, int('0b' + ''.join(kr.Fullreverse(C)), base=2))
                        else:
                            self.assertEqual(-i + j, int('0b' + ''.join(C), base=2))
                    else:
                        self.assertEqual(-i + j, int('-0b' + ''.join(kr.Fullreverse(C)), base=2))

    def test_summator_minusB(self):
        for i in range(128):
            for j in range(128):
                A = i
                B = -j
                if (i + j >= 127):
                    continue
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
                    A[0] = '1'
                if not B_is_minus:
                    B = list(B[2:])
                else:
                    B = list(B[3:])
                bit_depth = 8
                while len(A) != bit_depth:
                    A.insert(0, "0")
                while len(B) != bit_depth:
                    B.insert(0, "0")
                if A_is_minus:
                    A[0] = '1'
                if B_is_minus:
                    B[0] = '1'

                C = kr.addition(A, B)

                with self.subTest(i=i, j=j):
                    if i - j >= 0:
                        if i - j == 0 and -j < 0:
                            self.assertEqual(i - j, int('0b' + ''.join(kr.Fullreverse(C)), base=2))
                        else:
                            self.assertEqual(i - j, int('0b' + ''.join(C), base=2))
                    else:
                        self.assertEqual(i - j, int('-0b' + ''.join(kr.Fullreverse(C)), base=2))

    #
    def test_summator_minusAB(self):
        for i in range(128):
            for j in range(128):
                A = -i
                B = -j
                if (i + j >= 127):
                    continue
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
                    A[0] = '1'
                if not B_is_minus:
                    B = list(B[2:])
                else:
                    B = list(B[3:])
                bit_depth = 8
                while len(A) != bit_depth:
                    A.insert(0, "0")
                while len(B) != bit_depth:
                    B.insert(0, "0")
                if A_is_minus:
                    A[0] = '1'
                if B_is_minus:
                    B[0] = '1'

                C = kr.addition(A, B)

                with self.subTest(i=i, j=j):
                    if -i - j >= 0:
                        if -i - j == 0 and -j < 0:
                            self.assertEqual(-i - j, int('0b' + ''.join(kr.Fullreverse(C)), base=2))
                        else:
                            self.assertEqual(-i - j, int('0b' + ''.join(C), base=2))
                    else:
                        self.assertEqual(-i - j, int('-0b' + ''.join(kr.Fullreverse(C)), base=2))
