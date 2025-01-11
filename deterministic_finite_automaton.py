transitions = {('s1', '0'): 's2',
               ('s1', '1'): 's1',
               ('s2', '0'): 's1',
               ('s2', '1'): 's2'}
final_state = 's1'


def dfa(s):
    curr_state = 's1'
    for c in s:
        curr_state = transitions[(curr_state, c)]

    return curr_state == final_state


s = '101010'
print(dfa(s))
