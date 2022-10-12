import time


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s -> %r' % (elapsed, name, result))
        return result

    return clocked


class Calculator:
    @memoize
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n + 1):
            yield a
            a, b = b, a + b

    @memoize
    @clock
    def n_fib(self, n):
        if n < 2:
            return n
        return self.n_fib(n - 2) + self.n_fib(n - 1)

    @memoize
    def fact(self, n):
        if n < 1:
            return 1
        return n * self.fact(n - 1)


if __name__ == '__main__':
    c = Calculator()
    n = int(input('Введите целое число:'))
    print(f'Fibonacci sequence of {n}: ', *c.fib(n))
    print(f'Fibonacci number of {n}: ', c.n_fib(n))
    print(f'Factorial of {n}: ', c.fact(n))
