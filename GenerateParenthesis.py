from itertools import permutations


def valid_parenthesis(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def gen_parenthesis_naive(n):
    paren_set = set()
    for perm in permutations('()' * n):
        paren_str = ''.join(perm)
        if valid_parenthesis(paren_str):
            paren_set.add(paren_str)
    return sorted(list(paren_set))


def gen_parenthesis_recur(n):
    paren_str_list = []

    def _gen_parenthesis(paren_str, open_count, close_count):
        if open_count == 0 and close_count == 0:
            # print(paren_str)
            paren_str_list.append(paren_str)
        if open_count > 0:
            _gen_parenthesis(paren_str + '(', open_count - 1, close_count)
        if open_count != close_count:
            _gen_parenthesis(paren_str + ')', open_count, close_count - 1)

    _gen_parenthesis('', n, n)
    return paren_str_list


def gen_parenthesis_iter(n):
    stack = ['(']
    open_count = n - 1
    close_count = n
    paren_str_list = []
    while stack:
        if open_count == 0 and close_count == 0:
            paren_str_list.append(''.join(stack))
            while True:
                while stack.pop() == ')':
                    close_count += 1
                open_count += 1
                if open_count != close_count:
                    stack.append(')')
                    close_count -= 1
                    break
                elif open_count == n:
                    return paren_str_list
        if open_count > 0:
            stack.append('(')
            open_count -= 1
        elif open_count != close_count:
            stack.append(')')
            close_count -= 1


if __name__ == '__main__':

    print(gen_parenthesis_naive(4))
    # print(gen_parenthesis_recur(3))

    print('iter')
    print(gen_parenthesis_iter(4))
    # for item in gen_parenthesis_iter(2):
    #     print(item)

    print('recur')
    print(gen_parenthesis_recur(4))
    print(len(gen_parenthesis_recur(4)))
    # for item in gen_parenthesis_recur(2):
    #     print(item)

    # print(valid_parenthesis('('))
    # print(valid_parenthesis(')'))
    # print(valid_parenthesis(')('))
    # print(valid_parenthesis('()'))
    # print(valid_parenthesis('(())'))
    # print(valid_parenthesis('()()'))
