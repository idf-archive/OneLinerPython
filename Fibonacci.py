__author__ = 'Danyang'
fib = lambda n : reduce(lambda x, n: [x[1], x[0]+x[1]], xrange(n), [0, 1])[0]