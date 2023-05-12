# -*- coding: windows-1251 -*-

from app_project._2kr.algorithms import convert, dop, rev, summator
import json
import shutil


def check_overflow(str1, str2):
    if ((str1 == 'OVERFLOW' or str1 == '������������') and (str2 == 'OVERFLOW' or str2 == '������������')) or \
            str1 == str2:
        return True
    else:
        return False


def _3KR_load_to_json(ret_json, in_json):
    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    f1.close()

    # While there is no variant generation, I write the values for A and B in the JSON file myself.
    # Then we'll just fill them in and that's it.

    # var_numbers = generate_var()  ######## returns dict {"A": value, "B": value} (for example) ########
    # templates["A_var"] = var_numbers["A"]
    # templates["B_var"] = var_numbers["B"]

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

def clear_json(file):
    shutil.copy2("app_project/_3kr/KR3_json_proto.json", file)  # copy empty json (proto) to our json with results (file)
    return file