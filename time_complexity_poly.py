from math import log, factorial
import pylab


def time_complexity(n):
    pylab.title('Order of Growth of Running Time')
    pylab.xlabel('n')
    pylab.ylabel('time')

    pylab.xlim(0, n)
    pylab.ylim(0, n)

    # pylab.plot([factorial(i) for i in range(1, n + 1)], linestyle='-', color='g', label='Factorial - O(n!)')
    # pylab.plot([2 ** i for i in range(1, n + 1)], linestyle=':', color='b', label='Exponential - O(2^n)')
    pylab.plot([i ** 5 for i in range(1, n + 1)], linestyle='--', color='g', label='Quintic - O(n^5)')
    pylab.plot([i ** 4 for i in range(1, n + 1)], linestyle='-.', color='b', label='Quartic - O(n^4)')
    pylab.plot([i ** 3 for i in range(1, n + 1)], linestyle=':', color='r', label='Cubic - O(n^3)')
    pylab.plot([i ** 2 for i in range(1, n + 1)], linestyle='--', color='y', label='Quadratic - O(n^2)')
    # pylab.plot([i * log(i, 2) for i in range(1, n + 1)], linestyle='--', color='y', label='Linearithmic - O(n lg n)')
    pylab.plot([i for i in range(1, n + 1)], linestyle='-', color='k', label='Linear - O(n^1)')
    pylab.plot([i ** 0 for i in range(1, n + 1)], linestyle=':', color='g', label='Constant - O(n^0)')
    # pylab.plot([log(i, 2) for i in range(1, n + 1)], linestyle='--', color='m', label='Logarithmic - O(lg n)')
    # pylab.plot([1 for i in range(1, n + 1)], linestyle=':', color='c', label='Constant - O(k)')

    pylab.legend()
    pylab.show()


time_complexity(128)
