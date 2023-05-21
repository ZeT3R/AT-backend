import pandas as pd

trues = {
    'a': ['1', '0', '0', '0', '1', '1', '0', '0', '1', '1'],  # �������� �������� ��� a
    'b': ['1', '0', '1', '1', '0', '1', '0', '1', '1', '1'],  # �������� �������� ��� b
    'c': ['1', '1', '1', '0', '1', '0', '0', '0', '1', '1'],  # �������� �������� ��� c
    'd': ['1', '1', '0', '0', '1', '1', '1', '0', '1', '0'],  # �������� �������� ��� d
    'e': ['1', '0', '1', '0', '0', '1', '1', '0', '1', '0'],  # �������� �������� ��� e
    'f': ['1', '0', '0', '0', '0', '0', '1', '1', '1', '0'],  # �������� �������� ��� f
    'g': ['0', '0', '0', '1', '1', '1', '1', '0', '1', '1'],  # �������� �������� ��� g
    'l': ['0', '1', '0', '1', '0', '0', '1', '1', '0', '0'],  # �������� �������� ��� l
    'm': ['0', '0', '1', '1', '0', '0', '0', '0', '0', '1']  # �������� �������� ��� m
}


def create_var(b, offset, seg):  # ������� �������� ������� ��� ����������� �������
    dataframe = pd.DataFrame(trues)
    # ������� �� ���������� x1-x4. �� ������ ����� ����������.
    ix = {'x1': ['0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
          'x2': ['0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1'],
          'x3': ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1'],
          'x4': ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']}
    target = {seg: []}  # ������ ��������, � ��� ���� b � �� ���������� ���� ��������
    for i in range(offset):  # �� 0 �� �������� ��������
        target[seg].append('x')  # ���������� ���� (��� ��� ��� �������� �� ������, ������� �� ��������)
    for i in range(len(b)):  # ����� ����� ��
        target[seg].append(b[i])  # ���������� � �������� ��� �������� �� ��������. � ������ ������ b_true
    while len(target[seg]) != 16:  # ���� ����� ���� ���������, � ��� ���� ������ ��������, ��
        target[seg].append('x')  # ����������� �� ������
    final = pd.DataFrame.from_dict(ix)  # ������ ��������� �� ������� � ������
    final[seg] = target[seg]  # ������ ����� ������� �� ������ ������� �� ��������
    return final  # � ����������


def modify_str(func, t_func):  # ������� ��������� ������. ������ ���� � ������� �� ��������� �����������
    func = list(func)  # ��������� ������� � ������
    if t_func == 'SDNF':  # ���� ����
        for i in range(4):  # 4 �����
            if func[i] == '0':  # ���� � ��� �����, ��
                func[i] = ' nx' + str(i + 1) + ' ^'  # ����� �� ��� i+1. � ��� �� � ����, � ��� � x1.
            else:  # �����, ���� � ��� 1
                func[i] = ' x' + str(i + 1) + ' ^'  # ������ ���. � ����� ��������� ���� ���������
    else:  # ���� �� ����
        for i in range(4):  # 4 �����
            if func[i] == '0':  # ���� ����
                func[i] = ' nx' + str(i + 1) + ' v'  # ������ �� �� �����, ��� �� ���������� �������
            else:  # ���� 1
                func[i] = ' x' + str(i + 1) + ' v'  # �� �� �����, ��� � ����, ������ � ����� ���� ��������

    func = ''.join(func)  # ��������� � ������
    return func  # ����������


def modify_var(var_table, offset, seg):  # ������� ����������� ������� (���������� �������� � �� ����������)
    SDKNF = {'SDNF': [], 'SKNF': []}  # ������ ������� ��� �������
    Fsdnf, Fsknf = [], []  # ������ ������ ��� �������� ��������, ��� �� ���������
    for i in range(16):  # 16 ����� � ��� �����. ���������� �� ���� ��������� ���������� (-)
        SDKNF['SDNF'].append('-')  # ���������
        SDKNF['SKNF'].append('-')  # ���������
    var_table['SDNF'] = SDKNF['SDNF']  # ��������� � �������
    var_table['SKNF'] = SDKNF['SKNF']  # ��������� � �������
    func = ''  # ���� ������� ����/����
    func_list_DNF = []
    func_list_KNF = []
    for i in range(offset, offset + 10):  # ��� �� ����� �������� �� �������� + 10 (��� 10 ��������)
        if var_table[seg][i] == '1':  # ���� � ������� seg � ��� ����� 1, ������
            # ������, ��� � ��� ���� ������� ��������� ����. �� ����������� ������� ��������
            # �������� x1, x2, x3, x4 ���, ��� ��� ����, �� �� �����
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_DNF.append(func)
            func = modify_str(func, 'SDNF')  # ���������� � ������� ��������� ������
            func = list(func)  # ����� ��������������� � ������
            func.pop()  # ����������� ��������� �������, �� ���� v
            func.append(")")  # ��������� � ����� ����������� ������
            func.insert(0, '(')  # � � ������ ��������� ����������� ������
            func = ''.join(func)  # ����� ��������� � ������
            var_table.at[i, 'SDNF'] = func  # ������ ������ ��������� � ����� �������
            Fsdnf.append(func)  # � ��������� � ������ ������ ������� ����
        else:  # ���� �� � ��� ����� � ������� b, ��
            # �� ������, ��� � ��� ���� �������� � ���. ����� ����� �������������� �������������
            # ��������, ����� �������� ���������� ���������. ���������� ������ ������� ��������
            func = str(var_table['x1'][i]) + str(var_table['x2'][i]) + str(var_table['x3'][i]) \
                   + str(var_table['x4'][i])
            func_list_KNF.append(func)
            func = list(func)  # ��������� � ������
            for j in range(4):  # 4 �����
                if (func[j] == '0'):  # ���� ��� 0
                    func[j] = '1'  # ������ 1
                else:  # ���� ���� 1
                    func[j] = '0'  # ������ 0
            func = modify_str(func, 'SKNF')  # ��������������� ������
            func = list(func)  # ����� � ������
            func.pop()  # ����������� ������ ������
            func.append(")")  # ��������� � ����� ����������� ������
            func.insert(0, '(')  # � � ������ ��������� ����������� ������
            func = ''.join(func)  # ����� � ������
            var_table.at[i, 'SKNF'] = func  # ��������� �������� � �������
            Fsknf.append(func)  # � ���������� � ��������� ������ ������� ����
    return var_table, Fsdnf, Fsknf, func_list_DNF, func_list_KNF