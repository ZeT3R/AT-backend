import json
import shutil
from app_project.test_packages.transfer import *
from app_project.test_packages.algorithms import *
from app_project.test_packages.second_test_helper import *
import pandas

def check_overflow(str1, str2):
    if ((str1 == 'OVERFLOW' or str1 == 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ') and (
            str2 == 'OVERFLOW' or str2 == 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ')) or \
            str1 == str2:
        return True
    else:
        return False


def form_json1(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_1_json.json")
    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    count = 0

    templates["A_var"] = templatesIN["A_var"]
    templates["precision"] = templatesIN["precision"]
    templates["stud_id"] = templatesIN["stud_id"]

    A = templates["A_var"]
    prec = templates["precision"]

    A_dvoich, A_dvoich_whole, A_dvoich_frac = from10to2(A, prec)
    templates["A_dvoich"] = A_dvoich
    templatesIN["A_dvoich"] = True if templatesIN["A_dvoich"] == templates["A_dvoich"] else False
    if templatesIN["A_dvoich"]: count += 10

    A_oct = from10to8(A, A_dvoich_whole, A_dvoich_frac)
    templates["A_oct"] = A_oct
    templatesIN["A_oct"] = True if templatesIN["A_oct"] == templates["A_oct"] else False
    if templatesIN["A_oct"]: count += 15

    A_hex = from10to16(A, A_dvoich_whole, A_dvoich_frac)
    templates["A_hex"] = A_hex
    templatesIN["A_hex"] = True if templatesIN["A_hex"] == templates["A_hex"] else False
    if templatesIN["A_hex"]: count += 15

    for i in range(len(templatesIN["numb_with_system"])):
        if templatesIN["numb_with_system"][i]['numb'] == "":
            templatesIN["numb_with_system"][i]['result'] = False
            continue
        numb = int(templatesIN["numb_with_system"][i]['numb'], 10)
        system_from = int(templatesIN["numb_with_system"][i]['system_from'], 10)
        system_to = int(templatesIN["numb_with_system"][i]['system_to'], 10)

        templates["numb_with_system"][i]['numb'] = int(templatesIN["numb_with_system"][i]['numb'], 10)
        templates["numb_with_system"][i]['system_from'] = int(templatesIN["numb_with_system"][i]['system_from'], 10)
        templates["numb_with_system"][i]['system_to'] = int(templatesIN["numb_with_system"][i]['system_to'], 10)

        if system_from == 10:
            templates["numb_with_system"][i]['result'] = from10(numb, system_to)
        elif system_from == 2:
            templates["numb_with_system"][i]['result'] = from2(numb, system_to)
        else:
            templates["numb_with_system"][i]['result'] = fromP(numb, system_from, system_to)
        templatesIN["numb_with_system"][i]['result'] = True if templatesIN["numb_with_system"][i]['result'] ==\
                                                               templates["numb_with_system"][i]['result'] else False
        if templatesIN["numb_with_system"][i]['result']: count += 10

    templatesIN["score"] = count

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def form_json2(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_2_json.json")

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    count = 0
    var = trues[templatesIN["segment"]]
    varik = create_var(var, templatesIN["offset"], templatesIN["segment"])
    print(varik)

    my_var_save = varik.copy()
    varik, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = modify_var(varik,
                                                                    templatesIN["offset"],
                                                                    templatesIN["segment"])  # Получаем СДНФ и СКНФ и меняем таблицу
    print("Fсднф = ", Fsdnf, '\n\n', "Fскнф = ", Fsknf)  # Проверяем
    print(varik)

    Carno = create_carno(varik[templatesIN["segment"]])
    print(Carno)
    carno_minim = carno_minimization[templatesIN["segment"] + "_" + str(templatesIN["offset"])]
    print(carno_minim)
    Tknf = carno_minim["TKNF"]
    Tdnf = carno_minim["TDNF"]

    Tknf_pirs = Pirs(Tknf)  # запомнили результат
    Tdnf_sheffer = Sheffer(Tdnf)  # запомнили результат

    print(Tknf_pirs)
    print(Tdnf_sheffer)

    splitTdnf = Split_Tdnf(Tdnf)  # Присваиваем
    splitTknf = Split_Tknf(Tknf)  # Присваиваем

    print(splitTdnf)
    print(splitTknf)

    table1 = check_Table_tdnf(my_var_save, splitTdnf)  # Запоминаем первую таблицу СДНФ
    table2 = check_Table_tknf(my_var_save, splitTknf)  # Запоминаем вторую таблицу СКНФ

    for i in range(len(table1[templatesIN["segment"]])):
        if table1[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(table1[templatesIN["segment"]][i]) != int(table1.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")

    for i in range(len(table2[templatesIN["segment"]])):
        if table2[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(table2[templatesIN["segment"]][i]) != int(table2.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")

    chkPirs = check_Table_Pirs(my_var_save, Tknf_pirs)
    chkSheffer = check_Table_Sheffer(my_var_save, Tdnf_sheffer)

    for i in range(len(chkPirs[templatesIN["segment"]])):
        if chkPirs[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(chkPirs[templatesIN["segment"]][i]) != int(chkPirs.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")

    for i in range(len(chkSheffer[templatesIN["segment"]])):
        if chkSheffer[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(chkSheffer[templatesIN["segment"]][i]) != int(chkSheffer.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")

    Quine = Kvaina_DNF(Fsdnf)
    while 1:
        temp = Kvaina_DNF(Quine)
        if temp == Quine:
            break
        else:
            Quine = temp.copy()

    for i in range(len(Quine)):
        Quine[i] = Quine[i].replace('&', ' & ')
    Quine = format_DNF(Quine)
    split_check = Split_Tdnf(Quine)
    Quine_Tdnf_check = check_Table_tdnf(my_var_save, split_check)

    for i in range(len(Quine_Tdnf_check[templatesIN["segment"]])):
        if Quine_Tdnf_check[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(Quine_Tdnf_check[templatesIN["segment"]][i]) != int(Quine_Tdnf_check.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")


    Quine_KNF = Kvaina_KNF(Fsknf)
    while 1:
        temp = Kvaina_KNF(Quine_KNF)
        if temp == Quine_KNF:
            break
        else:
            Quine_KNF = temp.copy()

    for i in range(len(Quine_KNF)):
        Quine_KNF[i] = Quine_KNF[i].replace('v', ' v ')
    Quine_KNF = format_KNF(Quine_KNF)
    split_check_knf = Split_Tknf(Quine_KNF)
    Quine_Tknf_check = check_Table_tknf(my_var_save, split_check_knf)


    for i in range(len(Quine_Tknf_check[templatesIN["segment"]])):
        if Quine_Tknf_check[templatesIN["segment"]][i] == 'x':
            continue
        else:
            if int(Quine_Tknf_check[templatesIN["segment"]][i]) != int(Quine_Tknf_check.iloc[:,-1][i]):
                print("You suck, little boy, go fuck yourself!")

    return [templates, templatesIN]

def form_json3(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_3_json.json")

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    count = 0

    templates["A_var"] = templatesIN["A_var"]
    templates["B_var"] = templatesIN["B_var"]
    templates["stud_id"] = templatesIN["stud_id"]

    q = templates["A_var"]
    w = templates["B_var"]

    templates["A"]["str"] = convert(q)
    templatesIN['A']['str'] = True if templatesIN['A']['str'] == templates["A"]["str"] else False
    if templatesIN['A']['str']: count += 1
    templates["A"]["rev"] = rev(q)
    templatesIN['A']['rev'] = True if templatesIN['A']['rev'] == templates["A"]["rev"] else False
    if templatesIN['A']['rev']: count += 2
    templates["A"]["dop"] = dop(q)
    templatesIN['A']['dop'] = True if templatesIN['A']['dop'] == templates["A"]["dop"] else False
    if templatesIN['A']['dop']: count += 2
    templates["A"]["int"] = convert(convert(q))

    templates["B"]["str"] = convert(w)
    templatesIN['B']['str'] = True if templatesIN['B']['str'] == templates["B"]["str"] else False
    if templatesIN['B']['str']: count += 1
    templates["B"]["rev"] = rev(w)
    templatesIN['B']['rev'] = True if templatesIN['B']['rev'] == templates["B"]["rev"] else False
    if templatesIN['B']['rev']: count += 2
    templates["B"]["dop"] = dop(w)
    templatesIN['B']['dop'] = True if templatesIN['B']['dop'] == templates["B"]["dop"] else False
    if templatesIN['B']['dop']: count += 2
    templates["B"]["int"] = convert(convert(w))

    templates["-A"]["str"] = convert(-q)
    templatesIN['-A']['str'] = True if templatesIN['-A']['str'] == templates["-A"]["str"] else False
    if templatesIN['-A']['str']: count += 1
    templates["-A"]["rev"] = rev(-q)
    templatesIN['-A']['rev'] = True if templatesIN['-A']['rev'] == templates["-A"]["rev"] else False
    if templatesIN['-A']['rev']: count += 2
    templates["-A"]["dop"] = dop(-q)
    templatesIN['-A']['dop'] = True if templatesIN['-A']['dop'] == templates["-A"]["dop"] else False
    if templatesIN['-A']['dop']: count += 2
    templates["-A"]["int"] = convert(convert(-q))

    templates["-B"]["str"] = convert(-w)
    templatesIN['-B']['str'] = True if templatesIN['-B']['str'] == templates["-B"]["str"] else False
    if templatesIN['-B']['str']: count += 1
    templates["-B"]["rev"] = rev(-w)
    templatesIN['-B']['rev'] = True if templatesIN['-B']['rev'] == templates["-B"]["rev"] else False
    if templatesIN['-B']['rev']: count += 2
    templates["-B"]["dop"] = dop(-w)
    templatesIN['-B']['dop'] = True if templatesIN['-B']['dop'] == templates["-B"]["dop"] else False
    if templatesIN['-B']['dop']: count += 2
    templates["-B"]["int"] = convert(convert(-w))

    templates["A*2^-2"]["str"] = shift(convert(q), "str", -2)
    templatesIN['A*2^-2']['str'] = True if check_overflow(templatesIN['A*2^-2']['str'],
                                                             templates["A*2^-2"]["str"]) else False
    if templatesIN['A*2^-2']['str']: count += 2
    templates["A*2^-2"]["rev"] = shift(rev(q), "str", -2)
    templatesIN['A*2^-2']['rev'] = True if check_overflow(templatesIN['A*2^-2']['rev'],
                                                             templates["A*2^-2"]["rev"]) else False
    if templatesIN['A*2^-2']['rev']: count += 4
    templates["A*2^-2"]["dop"] = shift(dop(q), "str", -2)
    templatesIN['A*2^-2']['dop'] = True if check_overflow(templatesIN['A*2^-2']['dop'],
                                                             templates["A*2^-2"]["dop"]) else False
    if templatesIN['A*2^-2']['dop']: count += 4
    templates["A*2^-2"]["int"] = convert(shift(convert(q), "str", -2))

    templates["A*2^-3"]["str"] = shift(convert(q), "str", -3)
    templatesIN['A*2^-3']['str'] = True if check_overflow(templatesIN['A*2^-3']['str'],
                                                             templates["A*2^-3"]["str"]) else False
    if templatesIN['A*2^-3']['str']: count += 2
    templates["A*2^-3"]["rev"] = shift(rev(q), "str", -3)
    templatesIN['A*2^-3']['rev'] = True if check_overflow(templatesIN['A*2^-3']['rev'],
                                                             templates["A*2^-3"]["rev"]) else False
    if templatesIN['A*2^-3']['rev']: count += 4
    templates["A*2^-3"]["dop"] = shift(dop(q), "str", -3)
    templatesIN['A*2^-3']['dop'] = True if check_overflow(templatesIN['A*2^-3']['dop'],
                                                             templates["A*2^-3"]["dop"]) else False
    if templatesIN['A*2^-3']['dop']: count += 4
    templates["A*2^-3"]["int"] = convert(shift(convert(q), "str", -3))

    templates["A*2^+3"]["str"] = shift(convert(q), "str", 3)
    templatesIN['A*2^+3']['str'] = True if check_overflow(templatesIN['A*2^+3']['str'],
                                                             templates["A*2^+3"]["str"]) else False
    if templatesIN['A*2^+3']['str']: count += 2
    templates["A*2^+3"]["rev"] = shift(rev(q), "str", 3)
    templatesIN['A*2^+3']['rev'] = True if check_overflow(templatesIN['A*2^+3']['rev'],
                                                             templates["A*2^+3"]["rev"]) else False
    if templatesIN['A*2^+3']['rev']: count += 4
    templates["A*2^+3"]["dop"] = shift(dop(q), "str", 3)
    templatesIN['A*2^+3']['dop'] = True if check_overflow(templatesIN['A*2^+3']['dop'],
                                                             templates["A*2^+3"]["dop"]) else False
    if templatesIN['A*2^+3']['dop']: count += 4
    templates["A*2^+3"]["int"] = convert(shift(convert(q), "str", 3))

    templates["A*2^+4"]["str"] = shift(convert(q), "str", 4)
    templatesIN['A*2^+4']['str'] = True if check_overflow(templatesIN['A*2^+4']['str'],
                                                             templates["A*2^+4"]["str"]) else False
    if templatesIN['A*2^+4']['str']: count += 2
    templates["A*2^+4"]["rev"] = shift(rev(q), "str", 4)
    templatesIN['A*2^+4']['rev'] = True if check_overflow(templatesIN['A*2^+4']['rev'],
                                                             templates["A*2^+4"]["rev"]) else False
    if templatesIN['A*2^+4']['rev']: count += 4
    templates["A*2^+4"]["dop"] = shift(dop(q), "str", 4)
    templatesIN['A*2^+4']['dop'] = True if check_overflow(templatesIN['A*2^+4']['dop'],
                                                             templates["A*2^+4"]["dop"]) else False
    if templatesIN['A*2^+4']['dop']: count += 4
    templates["A*2^+4"]["int"] = convert(shift(convert(q), "str", 4))

    templates["B*2^-2"]["str"] = shift(convert(w), "str", -2)
    templatesIN['B*2^-2']['str'] = True if check_overflow(templatesIN['B*2^-2']['str'],
                                                             templates["B*2^-2"]["str"]) else False
    if templatesIN['B*2^-2']['str']: count += 2
    templates["B*2^-2"]["rev"] = shift(rev(w), "str", -2)
    templatesIN['B*2^-2']['rev'] = True if check_overflow(templatesIN['B*2^-2']['rev'],
                                                             templates["B*2^-2"]["rev"]) else False
    if templatesIN['B*2^-2']['rev']: count += 4
    templates["B*2^-2"]["dop"] = shift(dop(w), "str", -2)
    templatesIN['B*2^-2']['dop'] = True if check_overflow(templatesIN['B*2^-2']['dop'],
                                                             templates["B*2^-2"]["dop"]) else False
    if templatesIN['B*2^-2']['dop']: count += 4
    templates["B*2^-2"]["int"] = convert(shift(convert(w), "str", -2))

    templates["B*2^-3"]["str"] = shift(convert(w), "str", -3)
    templatesIN['B*2^-3']['str'] = True if check_overflow(templatesIN['B*2^-3']['str'],
                                                             templates["B*2^-3"]["str"]) else False
    if templatesIN['B*2^-3']['str']: count += 2
    templates["B*2^-3"]["rev"] = shift(rev(w), "str", -3)
    templatesIN['B*2^-3']['rev'] = True if check_overflow(templatesIN['B*2^-3']['rev'],
                                                             templates["B*2^-3"]["rev"]) else False
    if templatesIN['B*2^-3']['rev']: count += 4
    templates["B*2^-3"]["dop"] = shift(dop(w), "str", -3)
    templatesIN['B*2^-3']['dop'] = True if check_overflow(templatesIN['B*2^-3']['dop'],
                                                             templates["B*2^-3"]["dop"]) else False
    if templatesIN['B*2^-3']['dop']: count += 4
    templates["B*2^-3"]["int"] = convert(shift(convert(w), "str", -3))

    templates["B*2^+3"]["str"] = shift(convert(w), "str", 3)
    templatesIN['B*2^+3']['str'] = True if check_overflow(templatesIN['B*2^+3']['str'],
                                                             templates["B*2^+3"]["str"]) else False
    if templatesIN['B*2^+3']['str']: count += 2
    templates["B*2^+3"]["rev"] = shift(rev(w), "str", 3)
    templatesIN['B*2^+3']['rev'] = True if check_overflow(templatesIN['B*2^+3']['rev'],
                                                             templates["B*2^+3"]["rev"]) else False
    if templatesIN['B*2^+3']['rev']: count += 4
    templates["B*2^+3"]["dop"] = shift(dop(w), "str", 3)
    templatesIN['B*2^+3']['dop'] = True if check_overflow(templatesIN['B*2^+3']['dop'],
                                                             templates["B*2^+3"]["dop"]) else False
    if templatesIN['B*2^+3']['dop']: count += 4
    templates["B*2^+3"]["int"] = convert(shift(convert(w), "str", 3))

    templates["B*2^+4"]["str"] = shift(convert(w), "str", 4)
    templatesIN['B*2^+4']['str'] = True if check_overflow(templatesIN['B*2^+4']['str'],
                                                             templates["B*2^+4"]["str"]) else False
    if templatesIN['B*2^+4']['str']: count += 2
    templates["B*2^+4"]["rev"] = shift(rev(w), "str", 4)
    templatesIN['B*2^+4']['rev'] = True if check_overflow(templatesIN['B*2^+4']['rev'],
                                                             templates["B*2^+4"]["rev"]) else False
    if templatesIN['B*2^+4']['rev']: count += 4
    templates["B*2^+4"]["dop"] = shift(dop(w), "str", 4)
    templatesIN['B*2^+4']['dop'] = True if check_overflow(templatesIN['B*2^+4']['dop'],
                                                             templates["B*2^+4"]["dop"]) else False
    if templatesIN['B*2^+4']['dop']: count += 4
    templates["B*2^+4"]["int"] = convert(shift(convert(w), "str", 4))

    templatesIN["score"] = count

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def form_json4(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_4_json.json")

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    templates["A_var"] = templatesIN["A_var"]
    templates["B_var"] = templatesIN["B_var"]
    templates["stud_id"] = templatesIN["stud_id"]

    q = templates["A_var"]
    w = templates["B_var"]

    A_B = summator(q, w)
    templates["A+B"]["str"] = convert(A_B)
    templatesIN['A+B']['str'] = True if templatesIN['A+B']['str'] == templates["A+B"]["str"] else False
    if templatesIN['A+B']['str']: count += 5
    templates["A+B"]["rev"] = rev(A_B)
    templatesIN['A+B']['rev'] = True if templatesIN['A+B']['rev'] == templates["A+B"]["rev"] else False
    if templatesIN['A+B']['rev']: count += 10
    templates["A+B"]["dop"] = dop(A_B)
    templatesIN['A+B']['dop'] = True if templatesIN['A+B']['dop'] == templates["A+B"]["dop"] else False
    if templatesIN['A+B']['dop']: count += 10
    templates["A+B"]["int"] = A_B

    minA_B = summator(-q, w)
    templates["-A+B"]["str"] = convert(minA_B)
    templatesIN['-A+B']['str'] = True if templatesIN['-A+B']['str'] == templates["-A+B"]["str"] else False
    if templatesIN['-A+B']['str']: count += 5
    templates["-A+B"]["rev"] = rev(minA_B)
    templatesIN['-A+B']['rev'] = True if templatesIN['-A+B']['rev'] == templates["-A+B"]["rev"] else False
    if templatesIN['-A+B']['rev']: count += 10
    templates["-A+B"]["dop"] = dop(minA_B)
    templatesIN['-A+B']['dop'] = True if templatesIN['-A+B']['dop'] == templates["-A+B"]["dop"] else False
    if templatesIN['-A+B']['dop']: count += 10
    templates["-A+B"]["int"] = minA_B

    A_minB = summator(q, -w)
    templates["A-B"]["str"] = convert(A_minB)
    templatesIN['A-B']['str'] = True if templatesIN['A-B']['str'] == templates["A-B"]["str"] else False
    if templatesIN['A-B']['str']: count += 5
    templates["A-B"]["rev"] = rev(A_minB)
    templatesIN['A-B']['rev'] = True if templatesIN['A-B']['rev'] == templates["A-B"]["rev"] else False
    if templatesIN['A-B']['rev']: count += 10
    templates["A-B"]["dop"] = dop(A_minB)
    templatesIN['A-B']['dop'] = True if templatesIN['A-B']['dop'] == templates["A-B"]["dop"] else False
    if templatesIN['A-B']['dop']: count += 10
    templates["A-B"]["int"] = A_minB

    minA_minB = summator(-q, -w)
    templates["-A-B"]["str"] = convert(minA_minB)
    templatesIN['-A-B']['str'] = True if templatesIN['-A-B']['str'] == templates["-A-B"]["str"] else False
    if templatesIN['-A-B']['str']: count += 5
    templates["-A-B"]["rev"] = rev(minA_minB)
    templatesIN['-A-B']['rev'] = True if templatesIN['-A-B']['rev'] == templates["-A-B"]["rev"] else False
    if templatesIN['-A-B']['rev']: count += 10
    templates["-A-B"]["dop"] = dop(minA_minB)
    templatesIN['-A-B']['dop'] = True if templatesIN['-A-B']['dop'] == templates["-A-B"]["dop"] else False
    if templatesIN['-A-B']['dop']: count += 10
    templates["-A-B"]["int"] = minA_minB

    templatesIN["score"] = count

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def clear_json(json_to_format, format):
    shutil.copy2(format,
                 json_to_format)  # copy empty json (proto) to our json with results (file)
    return json_to_format
