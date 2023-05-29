import json
import shutil
from app_project.test_packages.transfer import *
from app_project.test_packages.algorithms import *
from app_project.test_packages.second_test_helper import *
import app_project.test_packages.multiply_algo as algo
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
    templates["var_seg"] = varik[templatesIN["segment"]].tolist()
    print(templates["var_seg"])
    templatesIN["var_seg"] = True if templatesIN["var_seg"] == templates["var_seg"] else False
    varik, Fsdnf, Fsknf, func_list_DNF, func_list_KNF = modify_var(varik,
                                                                    templatesIN["offset"],
                                                                    templatesIN["segment"])  # Получаем СДНФ и СКНФ и меняем таблицу
    print("Fсднф = ", Fsdnf, '\n\n', "Fскнф = ", Fsknf)  # Проверяем
    print(varik)

    templates["Fsdnf"] = Fsdnf
    templates["Fsknf"] = Fsknf

    in_sdnf = templatesIN["Fsdnf"].copy()
    in_sknf = templatesIN["Fsknf"].copy()

    templatesIN["Fsdnf"] = True if templatesIN["Fsdnf"] == templates["Fsdnf"] else False
    templatesIN["Fsknf"] = True if templatesIN["Fsknf"] == templates["Fsknf"] else False

    Carno = create_carno(varik[templatesIN["segment"]])
    print(Carno)
    templates["Carno"]["carno_0"] = Carno[0][0]
    templates["Carno"]["carno_1"] = Carno[0][1]
    templates["Carno"]["carno_2"] = Carno[0][2]
    templates["Carno"]["carno_3"] = Carno[0][3]
    templates["Carno"]["carno_4"] = Carno[1][0]
    templates["Carno"]["carno_5"] = Carno[1][1]
    templates["Carno"]["carno_6"] = Carno[1][2]
    templates["Carno"]["carno_7"] = Carno[1][3]
    templates["Carno"]["carno_8"] = Carno[2][0]
    templates["Carno"]["carno_9"] = Carno[2][1]
    templates["Carno"]["carno_10"] = Carno[2][2]
    templates["Carno"]["carno_11"] = Carno[2][3]
    templates["Carno"]["carno_12"] = Carno[3][0]
    templates["Carno"]["carno_13"] = Carno[3][1]
    templates["Carno"]["carno_14"] = Carno[3][2]
    templates["Carno"]["carno_15"] = Carno[3][3]

    for i in range(16):
        templatesIN["Carno"]["carno" + "_" + str(i)] = True if templatesIN["Carno"]["carno" + "_" + str(i)] == templates["Carno"]["carno" + "_" + str(i)] else False


    carno_minim = carno_minimization[templatesIN["segment"] + "_" + str(templatesIN["offset"])]
    print(carno_minim)
    Tknf = carno_minim["TKNF"]
    Tdnf = carno_minim["TDNF"]

    templates["carno_tdnf"] = Tdnf
    templates["carno_tknf"] = Tknf

    templatesIN["carno_tdnf"] = True if templatesIN["carno_tdnf"] == templates["carno_tdnf"] else False
    templatesIN["carno_tknf"] = True if templatesIN["carno_tknf"] == templates["carno_tknf"] else False

    Tknf_pirs = Pirs(Tknf)  # запомнили результат
    Tdnf_sheffer = Sheffer(Tdnf)  # запомнили результат

    print(Tknf_pirs)
    print(Tdnf_sheffer)

    templates["Pirs"] = Tknf_pirs
    templates["Sheffer"] = Tdnf_sheffer

    templatesIN["Pirs"] = True if templatesIN["Pirs"] == templates["Pirs"] else False
    templatesIN["Sheffer"] = True if templatesIN["Sheffer"] == templates["Sheffer"] else False

    splitTdnf = Split_Tdnf(Tdnf)  # Присваиваем
    splitTknf = Split_Tknf(Tknf)  # Присваиваем

    print(splitTdnf)
    print(splitTknf)

    Quine = Kvaina_DNF(in_sdnf)
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

    in_Quine_DNF = Quine_Tdnf_check[Quine_Tdnf_check.columns[-1]].tolist()
    templatesIN["Quine_DNF"] = True if in_Quine_DNF == templates["var_seg"] else False



    Quine_KNF = Kvaina_KNF(in_sknf)
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

    in_Quine_KNF = Quine_Tdnf_check[Quine_Tknf_check.columns[-1]].tolist()
    templatesIN["Quine_KNF"] = True if in_Quine_KNF == templates["var_seg"] else False

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



def form_json_two_bits(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_json_two_bits.json")
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["X"]
    y = templatesIN["Y"]

    number_of_bits = algo.calculate_bits(x, y)

    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)

    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)
    S = ['0' for m in range(len(X) * 2 - 1)]
    interval_left = len(Y) - 2
    interval_right = len(Y)
    corr = 0
    algo.bit_depth = len(S)
    for i in range((len(Y) - 1) // 2):
        two_bits = Y[interval_left:interval_right]
        if corr == 1:
            two_bits = algo.change_bits(two_bits)
            if two_bits == ["0", "0"]:
                corr = 1
            else:
                corr = 0
        if two_bits == ['0', '0']:
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
        elif two_bits == ["0", '1']:
            S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
        elif two_bits == ['1', '1']:
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)
            corr = 1
        else:
            new_X = algo.shift(X.copy(), 'str' if X[0] == '0' else 'rev', 1)
            S = algo.addition(S, new_X, len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -2)

        if templatesIN["S"]["S" + str(i + 1)]  != "":

            templates["S"]["S" + str(i + 1)] = S.copy()
            templatesIN["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["S"]["S" + str(i + 1)]) == algo.convert(templates["S"]["S" + str(i + 1)]) else False

        interval_left -= 2
        interval_right -= 2

    if Y[0] == '0' and corr == 1:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
    elif Y[0] == '1' and corr == 1:
        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
    elif Y[0] == "1" and corr == 0:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)

    templates["S"]["correct"] = S.copy()
    templatesIN["S"]["correct"] = True if algo.convert(templatesIN["S"]["correct"]) == algo.convert(templates["S"]["correct"]) else False

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))

    templates["result"] = S.copy()
    templatesIN["result"] = True if algo.convert(templatesIN["result"]) == algo.convert(templates["result"]) else False



    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def form_json_section_multiply(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_json_two_bits.json")
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["X"]
    y = templatesIN["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)
    minX = algo.Fullreverse(X.copy())

    S = ['0' for m in range(len(X) * 2 - 1)]

    while len(minX) != len(S):
        minX.append(minX[0])

    for m in range(1, len(Y)):
        anal_bit = Y[m]
        minX = algo.shift(minX, "rev", -1)
        if anal_bit == '1':
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='rev', kr=3)
        templates["S"]["S" + str(m)] = S.copy()

        if templatesIN["S"]["S" + str(m + 1)] != "":

            templatesIN["S"]["S" + str(m)] = True if algo.convert(templatesIN["S"]["S" + str(m)], len(S)) == algo.convert(
            templates["S"]["S" + str(m)], len(S)) else False

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))

    templates["result"] = S.copy()
    templatesIN["result"] = True if algo.convert(templatesIN["result"], len(S)) == algo.convert(templates["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def form_json_dop_corr_step(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_json_two_bits.json")
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["X"]
    y = templatesIN["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    dopX = algo.dop(x, algo.bit_depth / 2 + 1)
    dopY = algo.dop(y, algo.bit_depth / 2 + 1)

    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)

    S = ['0' for m in range(len(X) * 2 - 1)]

    for i in range(len(Y)):
        anal_bit = dopY[i]
        if anal_bit == '1' and i == 0:
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
        elif anal_bit == '1':
            S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
        dopX.insert(1, X[0])

        templates["S"]["S" + str(i + 1)] = S.copy()
        if templatesIN["S"]["S" + str(i + 1)] != "":
            templatesIN["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["S"]["S" + str(i + 1)], len(S)) == algo.convert(
            templates["S"]["S" + str(i + 1)], len(S)) else False

    if S[0] == '1':
        S = algo.dop(algo.convert(S, len(S)), len(S))

    templates["result"] = S.copy()
    templatesIN["result"] = True if algo.convert(templatesIN["result"], len(S)) == algo.convert(templates["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def form_json_no_tail_rest(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_json_div.json")
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["X"]
    y = templatesIN["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    dopY = algo.dop(y, algo.bit_depth / 2 + 1)

    Z = []
    S = []

    minYdop = algo.Fullreverse(dopY.copy())
    minYdop = algo.addition(minYdop, ['1'], code='dop', bits=len(minYdop))

    for i in range(len(Y) - 1):
        if i == 0:
            S = algo.addition(X.copy(), minYdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
            if S[0] == '0':
                exit("Overflow")
            else:
                Z.append("0")
            S = algo.shift(S, 'dop', 1, ignore=True)
            S[-1] = X[0]
            templates["Z"].append(Z[0])
        if S[0] == '1':
            S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'dop', 1, ignore=True)
            S[-1] = X[0]
            if S[0] == '1':
                Z.append('0')
            else:
                Z.append("1")
        else:
            S = algo.addition(S, minYdop.copy(), len(X) * 2 - 1, code="dop", kr=3)
            S = algo.shift(S, 'dop', 1, ignore=True)
            S[-1] = X[0]
            if S[0] == '0':
                Z.append('1')
            else:
                Z.append('0')

        templates["Z"].append(Z[-1])

        templates["S"]["S" + str(i + 1)] = S.copy()

        if templatesIN["S"]["S" + str(i + 1)] != "":

            templatesIN["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["S"]["S" + str(i + 1)], len(S)) == algo.convert(
            templates["S"]["S" + str(i + 1)], len(S)) else False

        templatesIN["Z"] = True if templatesIN["Z"] == templates["Z"] else False

    templates["result"] = Z.copy()
    templatesIN["result"] = True if algo.convert(templatesIN["result"], len(Z)) == algo.convert(templates["result"], len(Z)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]



def clear_json(json_to_format, format):
    shutil.copy2(format,
                 json_to_format)  # copy empty json (proto) to our json with results (file)
    return json_to_format