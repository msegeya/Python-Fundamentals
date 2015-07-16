from itertools import islice, count

__author__ = 'johanvergeer'


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range (2,x):
            if x%n == 0:
                return False
    return True


def main():
    sumislice = sum(islice((x for x in count() if is_prime(x)), 1000))
    return sumislice

if __name__ == '__main__':
    main()