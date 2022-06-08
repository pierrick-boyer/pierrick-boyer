# n! = n * (n-1) * (n-2) * ... *2 * 1


def factorial(nb):

    if nb == 0 or nb == 1:
        return 1

    product = 1
    for num in range(1, nb+1):
        product = product * num

    return product


def recursion_factorial(nb):
    if nb == 0 or nb == 1:
        return 1
    return nb * recursion_factorial(nb-1)
