# def compute_prefix_function(p):
#     m = len(p)
#     prefix_table = [0] * m
#     prefix_table[0] = 0
#     k = 0
#     for q in range(1, m):
#         while k > 0 and p[k] != p[q]:
#             k = prefix_table[k - 1]
#         if p[k] == p[q]:
#             k += 1
#         prefix_table[q] = k
#     return prefix_table


def compute_prefix_function(pattern):
    prefix_table = [0] * len(pattern)
    prefix_table[0] = 0
    k = 0
    for i in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_table[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix_table[i] = k
    return prefix_table


def gen_prefix_table(pattern):
    prefix_table, prefval, j = [0], 0, -1
    for i in range(1, len(pattern)):
        j += 1
        if pattern[i] == pattern[j]:
            prefval += 1
        else:
            prefval = 0
            j = -1
        prefix_table.append(prefval)
    return prefix_table


def gen_prefix_table1(s):
    prefix_table = [0]
    for i in range(1, len(s)):
        pref, suff = proper_prefix_suffix(s[:i + 1])
        longest_str = get_longest_common_str(pref, suff)
        prefix_table.append(len(longest_str))
    return prefix_table


def gen_prefix_table2(s):
    prefix_table = [0]
    for i in range(1, len(s)):
        s1 = s[:i + 1]
        pref = [s1[:i + 1] for i in range(len(s1) - 1)]
        suff = [s1[i:] for i in range(1, len(s1))]

        maxlen = 0
        for item in pref:
            if item in suff and len(item) > maxlen:
                maxlen = len(item)
        prefix_table.append(maxlen)
    return prefix_table


def proper_prefix_suffix(s):
    return [s[:i + 1] for i in range(len(s) - 1)], [s[i:] for i in range(1, len(s))]


def get_longest_common_str(arr1, arr2):
    s = ''
    for item1 in arr1:
        if item1 in arr2 and len(item1) > len(s):
            s = item1
    return s


print(gen_prefix_table('ababaca'))
print(gen_prefix_table1('ababaca'))
print(gen_prefix_table2('ababaca'))
print(gen_prefix_table2('abcdefabcdef'))

# print compute_prefix_function('acacagt')
# print gen_prefix_table('acacagt')
# print gen_prefix_table1('acacagt')

# p, s = proper_prefix_suffix('asdfasdf')
# print(p)
# print(s)

# print(compute_prefix_function('ababaca'))
# print(gen_prefix_table('ababaca'))
# print compute_prefix_function('abcabc')
# print gen_prefix_table('abcabc')
# print compute_prefix_function('xyxy')
# print gen_prefix_table('xyxy')

# print gen_prefix_table('aa')
# tab = [0]
# print tab
# tab.append(1)
# print tab
