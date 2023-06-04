import json
import app_project.test_packages.multiply_algo as algo

def form_json_Boota(ret_json, in_json):
    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["first"]["X"]
    y = templatesIN["first"]["Y"]

    number_of_bits = algo.calculate_bits_Boota(x, y)
    X = algo.convert(x, number_of_bits)
    Y = algo.convert(y, number_of_bits)

    minX = algo.addition(algo.Fullreverse(X.copy()), ['1'], bits=len(X), code='dop', kr=2)


    S = ['0' for m in range(len(X) * 2 - 1)]

    Y.append('0')

    interval_left = len(Y) - 2
    interval_right = len(Y)

    algo.bit_depth = len(S)

    for i in range(len(Y) - 2):
        two_bits = Y[interval_left:interval_right]

        if two_bits == ['1', '0']:
            S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
        elif two_bits == ['0', '1']:
            S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)
        else:
            S = algo.shift(S, 'str' if S[0] == '0' else 'rev', -1)


        templates["first"]["S"]["S" + str(i + 1)] = S.copy()
        if templatesIN["first"]["S"]["S" + str(i + 1)] != "":
            templatesIN["first"]["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["first"]["S"]["S" + str(i + 1)]) == algo.convert(templates["first"]["S"]["S" + str(i + 1)]) else False


        interval_left -= 1
        interval_right -= 1

    Y.pop()

    if S[0] == '1':
        S = algo.dop(algo.convert(S, len(S)), len(S))

    templates["first"]["result"] = S.copy()
    if templatesIN["first"]["result"] != []:
        templatesIN["first"]["result"] = True if algo.convert(templatesIN["first"]["result"]) == algo.convert(templates["first"]["result"]) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]

def form_json_two_bits(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["second"]["X"]
    y = templatesIN["second"]["Y"]

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


        templates["second"]["S"]["S" + str(i + 1)] = S.copy()
        if templatesIN["second"]["S"]["S" + str(i + 1)] != "":
            templatesIN["second"]["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["second"]["S"]["S" + str(i + 1)]) == algo.convert(templates["second"]["S"]["S" + str(i + 1)]) else False

        interval_left -= 2
        interval_right -= 2

    if Y[0] == '0' and corr == 1:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)
    elif Y[0] == '1' and corr == 1:
        S = algo.addition(S, minX.copy(), len(X) * 2 - 1, code='dop', kr=3)
    elif Y[0] == "1" and corr == 0:
        S = algo.addition(S, X.copy(), len(X) * 2 - 1, code='str' if S[0] == '0' else 'rev', kr=3)

    templates["second"]["S"]["correct"] = S.copy()
    if templatesIN["second"]["S"]["correct"] != "":
        templatesIN["second"]["S"]["correct"] = True if algo.convert(templatesIN["second"]["S"]["correct"]) == algo.convert(templates["second"]["S"]["correct"]) else False

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))

    templates["second"]["result"] = S.copy()
    if templatesIN["second"]["result"] != []:
        templatesIN["second"]["result"] = True if algo.convert(templatesIN["second"]["result"]) == algo.convert(templates["second"]["result"]) else False



    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]













def form_json_section_multiply(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["first"]["X"]
    y = templatesIN["first"]["Y"]

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
        templates["first"]["S"]["S" + str(m)] = S.copy()

        if templatesIN["first"]["S"]["S" + str(m + 1)] != "":

            templatesIN["first"]["S"]["S" + str(m)] = True if algo.convert(templatesIN["first"]["S"]["S" + str(m)], len(S)) == algo.convert(
            templates["first"]["S"]["S" + str(m)], len(S)) else False

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))

    templates["first"]["result"] = S.copy()
    if templatesIN["first"]["result"] != []:
        templatesIN["first"]["result"] = True if algo.convert(templatesIN["first"]["result"], len(S)) == algo.convert(templates["first"]["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def corr_steps_rev(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["second"]["X"]
    y = templatesIN["second"]["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    revX = algo.rev(x, algo.bit_depth / 2 + 1)
    revY = algo.rev(y, algo.bit_depth / 2 + 1)
    minX = algo.Fullreverse(X.copy())

    S = ['0' for i in range(len(X) * 2 - 1)]

    corr_flag = False if revY[0] == '0' else True

    for i in range(len(Y)):
        anal_bit = revY[i]
        if anal_bit == '1' and i != 0:
            S = algo.addition(S, revX.copy(), len(X) * 2 - 1, code='rev', kr=3)

        if i != len(Y) - 1:
            revX.insert(1, X[0])
            if corr_flag:
                minX.append(minX[0])
        templates["second"]["S"]["S" + str(i)] = S.copy()

        if templatesIN["second"]["S"]["S" + str(i + 1)] != "":
            templatesIN["second"]["S"]["S" + str(i)] = True if algo.convert(templatesIN["second"]["S"]["S" + str(i)],
                                                                           len(S)) == algo.convert(
                templates["second"]["S"]["S" + str(i)], len(S)) else False

    if corr_flag:
        S = algo.addition(S, minX, len(X) * 2 - 1, code='rev', kr=3)
        S = algo.addition(S, revX, len(X) * 2 - 1, code='rev', kr=3)

    templates["second"]["S"]["correct"] = S.copy()
    if templatesIN["second"]["S"]["correct"] != "":
        templatesIN["second"]["S"]["correct"] = True if algo.convert(
            templatesIN["second"]["S"]["correct"]) == algo.convert(templates["second"]["S"]["correct"]) else False

    if S[0] == '1':
        S = algo.rev(algo.convert(S, len(S)), len(S))

    templates["second"]["result"] = S.copy()
    if templatesIN["second"]["result"] != []:
        templatesIN["second"]["result"] = True if algo.convert(templatesIN["second"]["result"], len(S)) == algo.convert(
            templates["second"]["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]














def form_json_dop_corr_step(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["first"]["X"]
    y = templatesIN["first"]["Y"]

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

        templates["first"]["S"]["S" + str(i + 1)] = S.copy()
        if templatesIN["first"]["S"]["S" + str(i + 1)] != "":
            templatesIN["first"]["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["first"]["S"]["S" + str(i + 1)], len(S)) == algo.convert(
            templates["first"]["S"]["S" + str(i + 1)], len(S)) else False

    if S[0] == '1':
        S = algo.dop(algo.convert(S, len(S)), len(S))

    templates["first"]["result"] = S.copy()
    if templatesIN["first"]["result"] != []:
        templatesIN["first"]["result"] = True if algo.convert(templatesIN["first"]["result"], len(S)) == algo.convert(templates["first"]["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def adjacent_digits(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["second"]["X"]
    y = templatesIN["second"]["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    dopX = algo.dop(x, algo.bit_depth / 2 + 1)
    dopY = algo.dop(y, algo.bit_depth / 2 + 1)

    if len(dopY) % 2 != 0:
        dopY.append("0")

    S = ['0' for i in range(len(X) * 2 - 1)]

    minXdop = algo.Fullreverse(dopX.copy())
    minXdop = algo.addition(minXdop, ['1'], code='dop', bits=len(minXdop))

    interval_left = 0
    interval_right = 2

    for i in range(len(dopY) - 1):
        two_bits = dopY[interval_left:interval_right]

        if two_bits == ['1', '0']:
            S = algo.addition(S, minXdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
        elif two_bits == ["0", "1"]:
            S = algo.addition(S, dopX.copy(), len(X) * 2 - 1, code='dop', kr=3)
        dopX.insert(1, dopX[0])
        minXdop.insert(1, minXdop[0])

        templates["second"]["S"]["S" + str(i + 1)] = S.copy()
        if templatesIN["second"]["S"]["S" + str(i + 1)] != "":
            templatesIN["second"]["S"]["S" + str(i + 1)] = True if algo.convert(
                templatesIN["second"]["S"]["S" + str(i + 1)], len(S)) == algo.convert(
                templates["second"]["S"]["S" + str(i + 1)], len(S)) else False

        interval_left += 1
        interval_right += 1

    if S[0] == '1':
        S = algo.dop(algo.convert(S, len(S)), len(S))

    templates["second"]["result"] = S.copy()
    if templatesIN["second"]["result"] != []:
        templatesIN["second"]["result"] = True if algo.convert(templatesIN["second"]["result"], len(S)) == algo.convert(templates["second"]["result"], len(S)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]















def form_json_no_tail_rest_Remain(ret_json, in_json):
    algo.bit_depth = 8
    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["first"]["X"]
    y = templatesIN["first"]["Y"]

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
            templates["first"]["Z"].append(Z[0])
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
        templates["first"]["Z"].append(Z[-1])

        templates["first"]["S"]["S" + str(i + 1)] = S.copy()

        if templatesIN["first"]["S"]["S" + str(i + 1)] != "":

            templatesIN["first"]["S"]["S" + str(i + 1)] = True if algo.convert(templatesIN["first"]["S"]["S" + str(i + 1)], len(S)) == algo.convert(
            templates["first"]["S"]["S" + str(i + 1)], len(S)) else False

        templatesIN["first"]["Z"] = True if templatesIN["first"]["Z"] == templates["first"]["Z"] else False
    templates["first"]["result"] = Z.copy()
    if templatesIN["first"]["result"] != []:
        templatesIN["first"]["result"] = True if algo.convert(templatesIN["first"]["result"], len(Z)) == algo.convert(templates["first"]["result"], len(Z)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]


def no_tail_rest_Divider(ret_json, in_json):
    algo.bit_depth = 8

    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["second"]["X"]
    y = templatesIN["second"]["Y"]

    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    dopY = algo.dop(y, algo.bit_depth / 2 + 1)

    Z = []
    S = ['0' for j in range(len(X) * 2 - 1)]

    minYdop = algo.Fullreverse(dopY.copy())
    minYdop = algo.addition(minYdop, ['1'], code='dop', bits=len(minYdop))

    for i in range(len(Y) - 1):
        Y.insert(1, Y[0])
        if i == 0:
            S = algo.addition(X.copy(), minYdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
            if S[0] == '0':
                exit("Overflow")
            else:
                Z.append("0")
        minYdop.insert(1, minYdop[0])
        S.append("0")
        if S[0] == '1':
            S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)
            if S[0] == '0':
                Z.append('1')
            else:
                Z.append('0')
        else:
            S = algo.addition(S, minYdop.copy(), len(X) * 2 - 1, code="dop", kr=3)
            if S[0] == '0':
                Z.append('1')
            else:
                Z.append('0')

        templates["second"]["Z"].append(Z[-1])

        templates["second"]["S"]["S" + str(i + 1)] = S.copy()

        if templatesIN["second"]["S"]["S" + str(i + 1)] != "":
            templatesIN["second"]["S"]["S" + str(i + 1)] = True if algo.convert(
                templatesIN["second"]["S"]["S" + str(i + 1)], len(S)) == algo.convert(
                templates["second"]["S"]["S" + str(i + 1)], len(S)) else False

        templatesIN["second"]["Z"] = True if templatesIN["second"]["Z"] == templates["second"]["Z"] else False

    templates["second"]["result"] = Z.copy()
    if templatesIN["second"]["result"] != []:
        templatesIN["second"]["result"] = True if algo.convert(templatesIN["second"]["result"], len(Z)) == algo.convert(
            templates["second"]["result"], len(Z)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]

def tail_restore(ret_json, in_json):
    algo.bit_depth = 8
    count = 0

    with open(ret_json) as f1:
        templates = json.load(f1)
    templatesIN = in_json

    x = templatesIN["third"]["X"]
    y = templatesIN["third"]["Y"]


    X = algo.convert(x, algo.bit_depth / 2 + 1)
    Y = algo.convert(y, algo.bit_depth / 2 + 1)

    dopY = algo.dop(y, algo.bit_depth / 2 + 1)

    Z = []
    S = ['0' for j in range(len(X) * 2 - 1)]

    minYdop = algo.Fullreverse(dopY.copy())
    minYdop = algo.addition(minYdop, ['1'], code='dop', bits=len(minYdop))

    for i in range(len(Y) - 1):
        if i == 0:
            S = algo.addition(X.copy(), minYdop.copy(), len(X) * 2 - 1, code='dop', kr=3)
            if algo.convert(S.copy()) < 0:
                Z.append('0')
                S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)
            else:
                exit("Overflow")
        minYdop.insert(1, minYdop[0])
        S.append("0")
        S = algo.addition(S, minYdop.copy(), len(X) * 2 - 1, code="dop", kr=3)
        Y.insert(1, Y[0])
        if algo.convert(S.copy()) > 0:
            Z.append('1')
        else:
            Z.append("0")
            S = algo.addition(S, Y.copy(), len(X) * 2 - 1, code='dop', kr=3)

        templates["third"]["Z"].append(Z[-1])

        templates["third"]["S"]["S" + str(i + 1)] = S.copy()

        if templatesIN["third"]["S"]["S" + str(i + 1)] != "":
            templatesIN["third"]["S"]["S" + str(i + 1)] = True if algo.convert(
                templatesIN["third"]["S"]["S" + str(i + 1)], len(S)) == algo.convert(
                templates["third"]["S"]["S" + str(i + 1)], len(S)) else False

        templatesIN["third"]["Z"] = True if templatesIN["third"]["Z"] == templates["third"]["Z"] else False

    if Z[0] == '1':
        Z = algo.rev(algo.convert(Z, len(Z)), len(Z))

    templates["third"]["result"] = Z.copy()
    if templatesIN["third"]["result"] != []:
        templatesIN["third"]["result"] = True if algo.convert(templatesIN["third"]["result"], len(Z)) == algo.convert(
            templates["third"]["result"], len(Z)) else False

    with open(ret_json, 'w') as output:
        json.dump(templates, output)

    return [templates, templatesIN]

