from itertools import product


def truth_table(*args, func=None, fdesc=None):
    truth_table = []
    truth_table.append(list(args) + [fdesc])
    for prod in product([False, True], repeat=(len(args))):
        truth_table.append(list(prod) + [func(args[0], args[1])])
    print(truth_table)


truth_table('p', 'q', func=lambda p, q: not (p and q), fdesc='not (p and q)')
