__author__ = 'arvid'

# This is the Codecadamy code for functions handling even/odd numbers and "purifying" lists.

def is_even(x):
    if x % 2 == 0:
        return True, print ("True")
    else:
        return False, print ("False")

def purify(x):

    new_list = []

    for i in x:
        if i % 2 == 0:
            new_list.append(i)
    return new_list, print(new_list)

purify([1, 2, 3, 4, 5, 6, 7, 8, 9])