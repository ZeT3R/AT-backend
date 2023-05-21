import json
import shutil
from app_project.test_packages.transfer import *
from app_project.test_packages.algorithms import *


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
