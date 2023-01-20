""" IG : few.pz """
def is_multiple(n, m):
    """ Check is multiple function """
    value = n / m
    return value == int(value)

def is_even(k):
    """ Check is event number function """
    return (k & 1) == 0

def minmax(data):
    """ Find min & max function BEST way! """
    data.sort()
    return (data[0], data[-1])

def main():
    """ Main function """
    print(is_multiple(10, 3))
    print(is_even(22))
    print(minmax([22,54,7,87,12,9,63,55,48]))
main()