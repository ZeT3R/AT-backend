from algorithms import convert, rev, dop, shift, summator
from load_to_json import _2KR_load_to_json, clear_json

q = 47
w = -50

print("A:", convert(q), rev(q), dop(q), convert(convert(q)), '\n')

print("B:", convert(w), rev(w), dop(w), convert(convert(w)), '\n')

print("-A:", convert(-q), rev(-q), dop(-q), convert(convert(-q)), '\n')

print("-B:", convert(-w), rev(-w), dop(-w), convert(convert(-w)), '\n')

print('\n', '\n', '\n')

print("A*2^-2:", shift(convert(q), 'str', -2), shift(rev(q), 'rev', -2), shift(dop(q), 'dop', -2), convert(shift(convert(q), 'str', -2)), '\n')

print("A*2^-3:", shift(convert(q), 'str', -3), shift(rev(q), 'rev', -3), shift(dop(q), 'dop', -3), convert(shift(convert(q), 'str', -3)), '\n')

print("A*2^3:", shift(convert(q), 'str', 3), shift(rev(q), 'rev', 3), shift(dop(q), 'dop', 3), convert(shift(convert(q), 'str', 3)), '\n')

print("A*2^4:", shift(convert(q), 'str', 4), shift(rev(q), 'rev', 4), shift(dop(q), 'dop', 4), convert(shift(convert(q), 'str', 4)), '\n')

print('\n', '\n', '\n')

print("B*2^-2:", shift(convert(w), 'str', -2), shift(rev(w), 'rev', -2), shift(dop(w), 'dop', -2), convert(shift(convert(w), 'str', -2)), '\n')

print("B*2^-3:", shift(convert(w), 'str', -3), shift(rev(w), 'rev', -3), shift(dop(w), 'dop', -3), convert(shift(convert(w), 'str', -3)), '\n')

print("B*2^3:", shift(convert(w), 'str', 3), shift(rev(w), 'rev', 3), shift(dop(w), 'dop', 3), convert(shift(convert(w), 'str', 3)), '\n')

print("B*2^4:", shift(convert(w), 'str', 4), shift(rev(w), 'rev', 4), shift(dop(w), 'dop', 4), convert(shift(convert(w), 'str', 4)), '\n')

print('\n', '\n', '\n')

print("A + B:", q, w, summator(q, w), '\n')

print("A - B:", q, -w, summator(q, -w), '\n')

print("-A + B:", -q, w, summator(-q, w), '\n')

print("-A-B:", -q, -w, summator(-q, -w), '\n')

file = _2KR_load_to_json("kr2_json.json") # Insert into json file our results
print(file) # Print our Json
#file = clear_json("kr2_json.json") # Clear json, deleting results (except values for A and B)

