# a = True
# b = True
# print(not(a and b))
# print(not a and not b)
#
# a = True
# b = False
# print(not(a and b))
# print(not a and not b)
#
# a = False
# b = True
# print(not(a and b))
# print(not a and not b)
#
# a = False
# b = False
# print(not(a and b))
# print(not a and not b)
#
# print('-----------------------')

a = True
b = True
print(not(a or b))
print(not a or not b)

a = True
b = False
print(not(a or b))
print(not a or not b)

a = False
b = True
print(not(a or b))
print(not a or not b)

a = False
b = False
print(not(a or b))
print(not a or not b)

print('-----------------------')

# equivalent = True
# for a in [True, False]:
#     for b in [True, False]:
#         if not (a and b) != (not a and not b):
#             equivalent = False
#             break
#     if not equivalent:
#         break
# print(equivalent)
#
# equivalent = True
# for a in [True, False]:
#     for b in [True, False]:
#         if not (a or b) != (not a or not b):
#             equivalent = False
#             break
#     if not equivalent:
#         break
# print(equivalent)


def equivalent(f1, f2):
    equivalent = True
    for a in [True, False]:
        for b in [True, False]:
            print(f1(a, b))
            print(f2(a, b))
            if f1(a, b) != f2(a, b):
                equivalent = False
                # break
        # if not equivalent:
        #     break
    return equivalent


# print(equivalent(lambda a, b: not (a and b),
#                  lambda a, b: not a and not b))
print(equivalent(lambda a, b: not (a or b),
                 lambda a, b: not a or not b))
