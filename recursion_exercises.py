import sys


def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def init(lst):
    return lst[:-1]


def last(lst):
    return lst[-1]


def multiply(m, n):
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)


def exponent(base, exp):
    if exp == 0:
        return 1
    else:
        return base * exponent(base, exp - 1)


def print_n_to_0(n):
    if n >= 0:
        print(n, end=' ')
        # print 'print_n_to_0(' + str(n - 1) + ')'
        print_n_to_0(n - 1)


def print_0_to_n(n):
    if n >= 0:
        # print 'print_0_to_n(' + str(n - 1) + ')'
        print_0_to_n(n - 1)
        print(n, end=' ')


# def print_0_to_n(n, i=0):
#     if i <= n:
#         print(i, end=' ')
#         print_0_to_n(n, i+1)


def print_n_to_0_to_n(n):
    if n == 0:
        print(0, end=' ')
    else:
        print(n, end=' ')
        print_n_to_0_to_n(n - 1)
        print(n, end=' ')


def same_num(n):
    if n == 0:
        return 0
    else:
        return 1 + same_num(n - 1)


def sum_0_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_0_to_n(n - 1)


def sum_list(lst):
    if lst:
        return head(lst) + sum_list(tail(lst))
    else:
        return 0


def product_list(lst):
    if lst:
        if len(lst) == 1:
            return lst[0]
        else:
            return head(lst) * product_list(tail(lst))
    else:
        return 0


def size(lst):
    if lst:
        return 1 + size(tail(lst))
    else:
        return 0


def number_of_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + number_of_digits(n / 10)


def get_minx(lst, n):  # n is size of array
    if n - 1 == 0:
        return lst[0]
    else:
        if lst[n - 1] < lst[0]:
            lst[0] = lst[n - 1]
        return get_minx(lst, n - 1)


def get_min(lst):
    if len(lst) == 1:
        return lst[-1]
    else:
        if head(lst) < lst[-1]:
            lst[-1] = head(lst)
        return get_min(tail(lst))


def duplicate_char(ch, n):
    if n == 0:
        return ''
    else:
        return ch + duplicate_char(ch, n - 1)


def draw_triangle_aux(n):
    if n == 0:
        return ''
    else:
        return '#' + draw_triangle_aux(n - 1)


def draw_triangle(n):
    if n > 0:
        draw_triangle(n - 1)
        print(draw_triangle_aux(n))


def print_num_dots_aux(n):
    if n == 0:
        return ''
    else:
        return '.' + print_num_dots_aux(n - 1)


def print_num_dots(n):
    if n > 0:
        print_num_dots(n - 1)
        print(str(n) + print_num_dots_aux(n), end=' ')


def appears_in(s, ch):
    if s:
        if head(s) == ch:
            return True
        else:
            return appears_in(tail(s), ch)
    else:
        return False


def is_an_element_of(e, lst):
    if lst:
        if head(lst) == e:
            return True
        else:
            return is_an_element_of(e, tail(lst))
    else:
        return False


def same_string(s):
    if s:
        return head(s) + same_string(tail(s))
    else:
        return ''


def underscore(s):
    if s:
        if head(s) == ' ':
            return '_' + underscore(tail(s))
        else:
            return head(s) + underscore(tail(s))
    else:
        return ''


def remove_vowels(s):
    if s:
        if head(s) in ['a', 'e', 'i', 'o', 'u']:
            return remove_vowels(tail(s))
        else:
            return head(s) + remove_vowels(tail(s))
    else:
        return ''


# def is_palindrome(s, n):  # n is string length
#     if len(s) < 2:
#         return True
#     else:
#         if s[0] == s[-1]:
#             s = s[1:-1]
#             return is_palindrome(s, n - 1)
#         else:
#             return False

def is_palindrome(s):
    if len(s) < 2:
        return True
    else:
        if s[0] == s[-1]:
            s = s[1:-1]
            return is_palindrome(s)
        else:
            return False


def binary_search(needle, haystack):
    if haystack:
        mid = len(haystack) / 2
        if needle == haystack[mid]:
            return True
        elif needle < haystack[mid]:
            haystack = haystack[0:mid]
        else:
            haystack = haystack[mid + 1:]

        if haystack:
            return binary_search(needle, haystack)
        else:
            return False
    else:
        return False


# def take(n, lst):
#     if lst:
#         if n >= len(lst):
#             return lst
#         else:
#             return take(n, init(lst))
#     else:
#         return []

def take(n, lst):
    if n == 0 or not lst:
        return []
    else:
        return [lst[0]] + take(n - 1, tail(lst))


# def drop(n, lst):
#     if lst:
#         if n == 0:
#             return lst
#         else:
#             return drop(n - 1, tail(lst))
#     else:
#         return []

def drop(n, lst):
    if n == 0:
        return lst
    else:
        return drop(n - 1, tail(lst))


def maximum(arr, m=-sys.maxsize):
    if arr:
        if arr[0] > m:
            m = arr[0]
        return maximum(arr[1:], m)
    else:
        return m


def conv_to_int(s):
    return conv_to_int_aux(s, len(s) - 1)


def conv_to_int_aux(s, n):
    if len(s) > 0:
        return (ord(s[0]) - 48) * pow(10, n) + conv_to_int_aux(s[1:], n - 1)
    return 0

# print multiply(5,0)
# print multiply(5,1)
# print multiply(5,2)
# print multiply(5,3)

# print exponent(2, 0)
# print exponent(2, 1)
# print exponent(2, 2)
# print exponent(2, 3)
# print exponent(2, 4)
# print exponent(2, 5)

# print_n_to_0(0)
# print_n_to_0(1)
# print_n_to_0(2)
# print_n_to_0(5)
# print ''

# print_0_to_n(0)
# print_0_to_n(5)
# print ''

# draw_triangle(5)

# print_num_dots(5)

# print duplicate_char('*', 5)

# print_n_to_0_to_n(5)

# print sum_0_to_n(0)
# print sum_0_to_n(1)
# print sum_0_to_n(2)
# print sum_0_to_n(3)
# print sum_0_to_n(4)
# print sum_0_to_n(5)

# print sum_list([1, 4, 5])
# print product_list([])
# print product_list([5])
# print product_list([1, 2, 3, 4, 5])

# print get_min([5, 1, 3], 3)
# print get_min([2, 3, 1])

# print size([])
# print size([5])
# print size([5, 10])
# print size([5, 10, 15])

# print binary_search(5, [])
# print binary_search(5, [1])
# print binary_search(5, [10])
#
# print binary_search(5, [2, 2])
# print binary_search(5, [1, 10])
# print binary_search(5, [10, 15])
#
# print binary_search(5, [1, 2, 3])
# print binary_search(5, [6, 7, 8])
# print binary_search(5, [4, 6, 7])
# print binary_search(5, [3, 4, 6])

# print binary_search(5, [1, 2, 3, 4])
# print binary_search(5, [6, 7, 8, 9])
# print binary_search(5, [4, 6, 7, 8])
# print binary_search(5, [3, 4, 6, 7])
# print binary_search(5, [2, 3, 4, 6])


# print binary_search(5, [5])
# print binary_search(5, [4, 5])
# print binary_search(5, [5, 6])
#
# print binary_search(5, [5, 6, 7])
# print binary_search(5, [4, 5, 6])
# print binary_search(5, [3, 4, 5])

# print binary_search(5, [2, 3, 4, 5])
# print binary_search(5, [3, 4, 5, 6])
# print binary_search(5, [4, 5, 6, 7])
# print binary_search(5, [5, 6, 7, 8])

# print is_palindrome('a', 1)
# print is_palindrome('abcba', 1)
# print is_palindrome('a')
# print is_palindrome('abaca')

# print number_of_digits(1)
# print number_of_digits(12)
# print number_of_digits(987)

# print init([1,2,3,4,5])
# print last([1,2,3,4,5])

# print appears_in('pippo', 'i')
# print appears_in('pippo', 'x')

# print same_string('pippo and topolino')
#
# print underscore('pippo and topolino')
#
# print remove_vowels('pippo')
# print remove_vowels('pippo and topolino')

print(take(3, []))
print(take(0, [1, 2, 3, 4, 5]))
print(take(1, [1, 2, 3, 4, 5]))
print(take(2, [1, 2, 3, 4, 5]))
print(take(3, [1, 2, 3, 4, 5]))
print(take(4, [1, 2, 3, 4, 5]))
print(take(5, [1, 2, 3, 4, 5]))
print(take(6, [1, 2, 3, 4, 5]))

# print(drop(3, []))
# print(drop(0, [1, 2, 3, 4, 5]))
# print(drop(1, [1, 2, 3, 4, 5]))
# print(drop(2, [1, 2, 3, 4, 5]))
# print(drop(3, [1, 2, 3, 4, 5]))
# print(drop(4, [1, 2, 3, 4, 5]))
# print(drop(5, [1, 2, 3, 4, 5]))
# print(drop(6, [1, 2, 3, 4, 5]))

# print is_an_element_of(1, [])
# print is_an_element_of(1, [1,2,3,4,5])
# print is_an_element_of(2, [1,2,3,4,5])
# print is_an_element_of(3, [1,2,3,4,5])
# print is_an_element_of(4, [1,2,3,4,5])
# print is_an_element_of(5, [1,2,3,4,5])
# print is_an_element_of(6, [1,2,3,4,5])

print_0_to_n(5)
