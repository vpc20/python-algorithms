# Finite Automaton String Matcher
from string import printable


def compute_transition_function(pattern, alphabet):
    transitions = {}
    m = len(pattern)
    for q in range(m + 1):
        for c in alphabet:
            k = min(m, q + 1)
            pqc = pattern[:q] + c
            while k > 0 and not pqc.endswith(pattern[:k]):
                k -= 1
            transitions[(q, c)] = k
    return transitions


def fa_string_matcher(text, transitions, m):
    state = 0
    for i in range(1, len(text)):
        state = transitions[(state, text[i])]
        if state == m:
            print(f'Pattern found at position {i - m + 1}')


transitions = {(0, 'a'): 1, (0, 'c'): 0, (0, 'g'): 0, (0, 't'): 0,
               (1, 'a'): 2, (1, 'c'): 0, (1, 'g'): 0, (1, 't'): 0,
               (2, 'a'): 2, (2, 'c'): 3, (2, 'g'): 0, (2, 't'): 0,
               (3, 'a'): 1, (3, 'c'): 0, (3, 'g'): 0, (3, 't'): 0}

fa_string_matcher('gtaacagtaaacg', transitions, 3)

x = compute_transition_function('aac', 'acgt')
print(x)
fa_string_matcher('gtaacagtaaacg', x, 3)

a = {(0, 'a'): 1, (0, 'c'): 0, (0, 'g'): 0, (0, 't'): 0,
     (1, 'a'): 2, (1, 'c'): 0, (1, 'g'): 0, (1, 't'): 0,
     (2, 'a'): 0, (2, 'c'): 3, (2, 'g'): 0, (2, 't'): 0,
     (3, 'a'): 0, (3, 'c'): 0, (3, 'g'): 0, (3, 't'): 0}

# x = compute_transition_function('fox', printable)
# fa_string_matcher('the quick brown fox jumps over the lazy dog', x, 3)
# for k, v in x.items():
#     print(k, v)
