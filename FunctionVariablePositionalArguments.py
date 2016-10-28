# write a function called product which accepts a variable number of arguments
# and returns the product of all of its args. With no args, product() should return 1

from __future__ import print_function

def product(*args):
    result = 1
    if len(args) == 0:
        return 1
    else:
        for arg in args:
            result = result * arg
    return result

print(product())
print(product(1,2,3))
print(product(6,10))
