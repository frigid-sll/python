def xx():
    for x in range(1000):
        print(2)
import timeit
if __name__ == '__main__':
    t = timeit.Timer('xx()', 'from __main__ import xx')
    print(t.timeit(1))

