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
    min_val = data[0]
    max_val = data[0]
    
    for i in range(len(data)):
        if data[i] < min_val:
            min_val = data[i]
        if data[i] > max_val:
            max_val = data[i]
    return (min_val, max_val)

def main():
    """ Main function """
    print(is_multiple(10, 3))
    print(is_even(22))
    print(minmax([22,54,7,87,12,9,63,55,48]))
main()