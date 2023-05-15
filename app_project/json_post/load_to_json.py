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
    
    f1.close()

    templates["A_var"] = templatesIN["A_var"]
    templates["precision"] = templatesIN["precision"]
    templates["stud_id"] = templatesIN["stud_id"]

    A = templates["A_var"]
    prec = templates["precision"]

    A_dvoich, A_dvoich_whole, A_dvoich_frac = from10to2(A, prec)
    templates["A_dvoich"] = A_dvoich
    templatesIN["A_dvoich"] = True if templatesIN["A_dvoich"] == templates["A_dvoich"] else False

    A_oct = from10to8(A, A_dvoich_whole, A_dvoich_frac)
    templates["A_oct"] = A_oct
    templatesIN["A_oct"] = True if templatesIN["A_oct"] == templates["A_oct"] else False

    A_hex = from10to16(A, A_dvoich_whole, A_dvoich_frac)
    templates["A_hex"] = A_hex
    templatesIN["A_hex"] = True if templatesIN["A_hex"] == templates["A_hex"] else False

    numb = templatesIN["numb_with_system1"][0]['numb']
    system_from = templatesIN["numb_with_system1"][0]['system_from']
    system_to = templatesIN["numb_with_system1"][0]['system_to']

    templates["numb_with_system1"][0]['numb'] = templatesIN["numb_with_system1"][0]['numb']
    templates["numb_with_system1"][0]['system_from'] = templatesIN["numb_with_system1"][0]['system_from']
    templates["numb_with_system1"][0]['system_to'] = templatesIN["numb_with_system1"][0]['system_to']

    if system_from == 10:
        templates["numb_with_system1"][0]['result'] = from10(numb, system_to)
    elif system_from == 2:
        templates["numb_with_system1"][0]['result'] = from2(numb, system_to)
    else:
        templates["numb_with_system1"][0]['result'] = fromP(numb, system_from, system_to)
    templatesIN["numb_with_system1"][0]['result'] = True if templatesIN["numb_with_system1"][0]['result'] == \
                                                            templates["numb_with_system1"][0]['result'] else False

    numb = templatesIN["numb_with_system2"][0]['numb']
    system_from = templatesIN["numb_with_system2"][0]['system_from']
    system_to = templatesIN["numb_with_system2"][0]['system_to']

    templates["numb_with_system2"][0]['numb'] = templatesIN["numb_with_system2"][0]['numb']
    templates["numb_with_system2"][0]['system_from'] = templatesIN["numb_with_system2"][0]['system_from']
    templates["numb_with_system2"][0]['system_to'] = templatesIN["numb_with_system2"][0]['system_to']

    if system_from == 10:
        templates["numb_with_system2"][0]['result'] = from10(numb, system_to)
    elif system_from == 2:
        templates["numb_with_system2"][0]['result'] = from2(numb, system_to)
    else:
        templates["numb_with_system2"][0]['result'] = fromP(numb, system_from, system_to)
    templatesIN["numb_with_system2"][0]['result'] = True if templatesIN["numb_with_system2"][0]['result'] == \
                                                            templates["numb_with_system2"][0]['result'] else False

    numb = templatesIN["numb_with_system3"][0]['numb']
    system_from = templatesIN["numb_with_system3"][0]['system_from']
    system_to = templatesIN["numb_with_system3"][0]['system_to']

    templates["numb_with_system3"][0]['numb'] = templatesIN["numb_with_system3"][0]['numb']
    templates["numb_with_system3"][0]['system_from'] = templatesIN["numb_with_system3"][0]['system_from']
    templates["numb_with_system3"][0]['system_to'] = templatesIN["numb_with_system3"][0]['system_to']

    if system_from == 10:
        templates["numb_with_system3"][0]['result'] = from10(numb, system_to)
    elif system_from == 2:
        templates["numb_with_system3"][0]['result'] = from2(numb, system_to)
    else:
        templates["numb_with_system3"][0]['result'] = fromP(numb, system_from, system_to)
    templatesIN["numb_with_system3"][0]['result'] = True if templatesIN["numb_with_system3"][0]['result'] == \
                                                            templates["numb_with_system3"][0]['result'] else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)
    f1.close()
    return [templates, templatesIN]


def form_json3(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_3_json.json")

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    f1.close()

    templates["A_var"] = templatesIN["A_var"]
    templates["B_var"] = templatesIN["B_var"]
    templates["stud_id"] = templatesIN["stud_id"]

    q = templates["A_var"]
    w = templates["B_var"]

    templates["A"][0]["str"] = convert(q)
    templatesIN['A'][0]['str'] = True if templatesIN['A'][0]['str'] == templates["A"][0]["str"] else False
    templates["A"][0]["rev"] = rev(q)
    templatesIN['A'][0]['rev'] = True if templatesIN['A'][0]['rev'] == templates["A"][0]["rev"] else False
    templates["A"][0]["dop"] = dop(q)
    templatesIN['A'][0]['dop'] = True if templatesIN['A'][0]['dop'] == templates["A"][0]["dop"] else False
    templates["A"][0]["int"] = convert(convert(q))

    templates["B"][0]["str"] = convert(w)
    templatesIN['B'][0]['str'] = True if templatesIN['B'][0]['str'] == templates["B"][0]["str"] else False
    templates["B"][0]["rev"] = rev(w)
    templatesIN['B'][0]['rev'] = True if templatesIN['B'][0]['rev'] == templates["B"][0]["rev"] else False
    templates["B"][0]["dop"] = dop(w)
    templatesIN['B'][0]['dop'] = True if templatesIN['B'][0]['dop'] == templates["B"][0]["dop"] else False
    templates["B"][0]["int"] = convert(convert(w))

    templates["-A"][0]["str"] = convert(-q)
    templatesIN['-A'][0]['str'] = True if templatesIN['-A'][0]['str'] == templates["-A"][0]["str"] else False
    templates["-A"][0]["rev"] = rev(-q)
    templatesIN['-A'][0]['rev'] = True if templatesIN['-A'][0]['rev'] == templates["-A"][0]["rev"] else False
    templates["-A"][0]["dop"] = dop(-q)
    templatesIN['-A'][0]['dop'] = True if templatesIN['-A'][0]['dop'] == templates["-A"][0]["dop"] else False
    templates["-A"][0]["int"] = convert(convert(-q))

    templates["-B"][0]["str"] = convert(-w)
    templatesIN['-B'][0]['str'] = True if templatesIN['-B'][0]['str'] == templates["-B"][0]["str"] else False
    templates["-B"][0]["rev"] = rev(-w)
    templatesIN['-B'][0]['rev'] = True if templatesIN['-B'][0]['rev'] == templates["-B"][0]["rev"] else False
    templates["-B"][0]["dop"] = dop(-w)
    templatesIN['-B'][0]['dop'] = True if templatesIN['-B'][0]['dop'] == templates["-B"][0]["dop"] else False
    templates["-B"][0]["int"] = convert(convert(-w))

    templates["A*2^-2"][0]["str"] = shift(convert(q), "str", -2)
    templatesIN['A*2^-2'][0]['str'] = True if check_overflow(templatesIN['A*2^-2'][0]['str'],
                                                             templates["A*2^-2"][0]["str"]) else False
    templates["A*2^-2"][0]["rev"] = shift(rev(q), "str", -2)
    templatesIN['A*2^-2'][0]['rev'] = True if check_overflow(templatesIN['A*2^-2'][0]['rev'],
                                                             templates["A*2^-2"][0]["rev"]) else False
    templates["A*2^-2"][0]["dop"] = shift(dop(q), "str", -2)
    templatesIN['A*2^-2'][0]['dop'] = True if check_overflow(templatesIN['A*2^-2'][0]['dop'],
                                                             templates["A*2^-2"][0]["dop"]) else False
    templates["A*2^-2"][0]["int"] = convert(shift(convert(q), "str", -2))

    templates["A*2^-3"][0]["str"] = shift(convert(q), "str", -3)
    templatesIN['A*2^-3'][0]['str'] = True if check_overflow(templatesIN['A*2^-3'][0]['str'],
                                                             templates["A*2^-3"][0]["str"]) else False
    templates["A*2^-3"][0]["rev"] = shift(rev(q), "str", -3)
    templatesIN['A*2^-3'][0]['rev'] = True if check_overflow(templatesIN['A*2^-3'][0]['rev'],
                                                             templates["A*2^-3"][0]["rev"]) else False
    templates["A*2^-3"][0]["dop"] = shift(dop(q), "str", -3)
    templatesIN['A*2^-3'][0]['dop'] = True if check_overflow(templatesIN['A*2^-3'][0]['dop'],
                                                             templates["A*2^-3"][0]["dop"]) else False
    templates["A*2^-3"][0]["int"] = convert(shift(convert(q), "str", -3))

    templates["A*2^+3"][0]["str"] = shift(convert(q), "str", 3)
    templatesIN['A*2^+3'][0]['str'] = True if check_overflow(templatesIN['A*2^+3'][0]['str'],
                                                             templates["A*2^+3"][0]["str"]) else False
    templates["A*2^+3"][0]["rev"] = shift(rev(q), "str", 3)
    templatesIN['A*2^+3'][0]['rev'] = True if check_overflow(templatesIN['A*2^+3'][0]['rev'],
                                                             templates["A*2^+3"][0]["rev"]) else False
    templates["A*2^+3"][0]["dop"] = shift(dop(q), "str", 3)
    templatesIN['A*2^+3'][0]['dop'] = True if check_overflow(templatesIN['A*2^+3'][0]['dop'],
                                                             templates["A*2^+3"][0]["dop"]) else False
    templates["A*2^+3"][0]["int"] = convert(shift(convert(q), "str", 3))

    templates["A*2^+4"][0]["str"] = shift(convert(q), "str", 4)
    templatesIN['A*2^+4'][0]['str'] = True if check_overflow(templatesIN['A*2^+4'][0]['str'],
                                                             templates["A*2^+4"][0]["str"]) else False
    templates["A*2^+4"][0]["rev"] = shift(rev(q), "str", 4)
    templatesIN['A*2^+4'][0]['rev'] = True if check_overflow(templatesIN['A*2^+4'][0]['rev'],
                                                             templates["A*2^+4"][0]["rev"]) else False
    templates["A*2^+4"][0]["dop"] = shift(dop(q), "str", 4)
    templatesIN['A*2^+4'][0]['dop'] = True if check_overflow(templatesIN['A*2^+4'][0]['dop'],
                                                             templates["A*2^+4"][0]["dop"]) else False
    templates["A*2^+4"][0]["int"] = convert(shift(convert(q), "str", 4))

    templates["B*2^-2"][0]["str"] = shift(convert(w), "str", -2)
    templatesIN['B*2^-2'][0]['str'] = True if check_overflow(templatesIN['B*2^-2'][0]['str'],
                                                             templates["B*2^-2"][0]["str"]) else False
    templates["B*2^-2"][0]["rev"] = shift(rev(w), "str", -2)
    templatesIN['B*2^-2'][0]['rev'] = True if check_overflow(templatesIN['B*2^-2'][0]['rev'],
                                                             templates["B*2^-2"][0]["rev"]) else False
    templates["B*2^-2"][0]["dop"] = shift(dop(w), "str", -2)
    templatesIN['B*2^-2'][0]['dop'] = True if check_overflow(templatesIN['B*2^-2'][0]['dop'],
                                                             templates["B*2^-2"][0]["dop"]) else False
    templates["B*2^-2"][0]["int"] = convert(shift(convert(w), "str", -2))

    templates["B*2^-3"][0]["str"] = shift(convert(w), "str", -3)
    templatesIN['B*2^-3'][0]['str'] = True if check_overflow(templatesIN['B*2^-3'][0]['str'],
                                                             templates["B*2^-3"][0]["str"]) else False
    templates["B*2^-3"][0]["rev"] = shift(rev(w), "str", -3)
    templatesIN['B*2^-3'][0]['rev'] = True if check_overflow(templatesIN['B*2^-3'][0]['rev'],
                                                             templates["B*2^-3"][0]["rev"]) else False
    templates["B*2^-3"][0]["dop"] = shift(dop(w), "str", -3)
    templatesIN['B*2^-3'][0]['dop'] = True if check_overflow(templatesIN['B*2^-3'][0]['dop'],
                                                             templates["B*2^-3"][0]["dop"]) else False
    templates["B*2^-3"][0]["int"] = convert(shift(convert(w), "str", -3))

    templates["B*2^+3"][0]["str"] = shift(convert(w), "str", 3)
    templatesIN['B*2^+3'][0]['str'] = True if check_overflow(templatesIN['B*2^+3'][0]['str'],
                                                             templates["B*2^+3"][0]["str"]) else False
    templates["B*2^+3"][0]["rev"] = shift(rev(w), "str", 3)
    templatesIN['B*2^+3'][0]['rev'] = True if check_overflow(templatesIN['B*2^+3'][0]['rev'],
                                                             templates["B*2^+3"][0]["rev"]) else False
    templates["B*2^+3"][0]["dop"] = shift(dop(w), "str", 3)
    templatesIN['B*2^+3'][0]['dop'] = True if check_overflow(templatesIN['B*2^+3'][0]['dop'],
                                                             templates["B*2^+3"][0]["dop"]) else False
    templates["B*2^+3"][0]["int"] = convert(shift(convert(w), "str", 3))

    templates["B*2^+4"][0]["str"] = shift(convert(w), "str", 4)
    templatesIN['B*2^+4'][0]['str'] = True if check_overflow(templatesIN['B*2^+4'][0]['str'],
                                                             templates["B*2^+4"][0]["str"]) else False
    templates["B*2^+4"][0]["rev"] = shift(rev(w), "str", 4)
    templatesIN['B*2^+4'][0]['rev'] = True if check_overflow(templatesIN['B*2^+4'][0]['rev'],
                                                             templates["B*2^+4"][0]["rev"]) else False
    templates["B*2^+4"][0]["dop"] = shift(dop(w), "str", 4)
    templatesIN['B*2^+4'][0]['dop'] = True if check_overflow(templatesIN['B*2^+4'][0]['dop'],
                                                             templates["B*2^+4"][0]["dop"]) else False
    templates["B*2^+4"][0]["int"] = convert(shift(convert(w), "str", 4))

    with open(ret_json, 'w') as output:
        json.dump(templates, output)
    f1.close()
    return [templates, templatesIN]


def form_json4(ret_json, in_json):
    ret_json = clear_json(ret_json, "app_project/json_post/format_4_json.json")

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    f1.close()

    templates["A_var"] = templatesIN["A_var"]
    templates["B_var"] = templatesIN["B_var"]
    templates["stud_id"] = templatesIN["stud_id"]

    q = templates["A_var"]
    w = templates["B_var"]

    A_B = summator(q, w)
    templates["A+B"][0]["str"] = convert(A_B)
    templatesIN['A+B'][0]['str'] = True if templatesIN['A+B'][0]['str'] == templates["A+B"][0]["str"] else False
    templates["A+B"][0]["rev"] = rev(A_B)
    templatesIN['A+B'][0]['rev'] = True if templatesIN['A+B'][0]['rev'] == templates["A+B"][0]["rev"] else False
    templates["A+B"][0]["dop"] = dop(A_B)
    templatesIN['A+B'][0]['dop'] = True if templatesIN['A+B'][0]['dop'] == templates["A+B"][0]["dop"] else False
    templates["A+B"][0]["int"] = A_B

    minA_B = summator(-q, w)
    templates["-A+B"][0]["str"] = convert(minA_B)
    templatesIN['-A+B'][0]['str'] = True if templatesIN['-A+B'][0]['str'] == templates["-A+B"][0]["str"] else False
    templates["-A+B"][0]["rev"] = rev(minA_B)
    templatesIN['-A+B'][0]['rev'] = True if templatesIN['-A+B'][0]['rev'] == templates["-A+B"][0]["rev"] else False
    templates["-A+B"][0]["dop"] = dop(minA_B)
    templatesIN['-A+B'][0]['dop'] = True if templatesIN['-A+B'][0]['dop'] == templates["-A+B"][0]["dop"] else False
    templates["-A+B"][0]["int"] = minA_B

    A_minB = summator(q, -w)
    templates["A-B"][0]["str"] = convert(A_minB)
    templatesIN['A-B'][0]['str'] = True if templatesIN['A-B'][0]['str'] == templates["A-B"][0]["str"] else False
    templates["A-B"][0]["rev"] = rev(A_minB)
    templatesIN['A-B'][0]['rev'] = True if templatesIN['A-B'][0]['rev'] == templates["A-B"][0]["rev"] else False
    templates["A-B"][0]["dop"] = dop(A_minB)
    templatesIN['A-B'][0]['dop'] = True if templatesIN['A-B'][0]['dop'] == templates["A-B"][0]["dop"] else False
    templates["A-B"][0]["int"] = A_minB

    minA_minB = summator(-q, -w)
    templates["-A-B"][0]["str"] = convert(minA_minB)
    templatesIN['-A-B'][0]['str'] = True if templatesIN['-A-B'][0]['str'] == templates["-A-B"][0]["str"] else False
    templates["-A-B"][0]["rev"] = rev(minA_minB)
    templatesIN['-A-B'][0]['rev'] = True if templatesIN['-A-B'][0]['rev'] == templates["-A-B"][0]["rev"] else False
    templates["-A-B"][0]["dop"] = dop(minA_minB)
    templatesIN['-A-B'][0]['dop'] = True if templatesIN['-A-B'][0]['dop'] == templates["-A-B"][0]["dop"] else False
    templates["-A-B"][0]["int"] = minA_minB

    with open(ret_json, 'w') as output:
        json.dump(templates, output)
    output.close()
    return [templates, templatesIN]


def clear_json(json_to_format, format):
    shutil.copy2(format,
                 json_to_format)  # copy empty json (proto) to our json with results (file)
    return json_to_format
