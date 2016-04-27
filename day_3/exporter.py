
people = [
    ("jane", 25),
    ("James", 27),
    ("Micheal", 63),
    ("Gary", 54)
]


def super_sum(*args):
    return sum(args)


def hello_again(name, age):
    return "I am {} and {} years old".format(name, age)


def max_min(A):
    '''
    returns max-value -min max-value
    '''
    # return max(A) - max(A)
    max_, min_ = A[0], A[0]
    for i in A:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    return max_ - min_
