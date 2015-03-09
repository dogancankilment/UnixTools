import random


def get_val(array, val):
    """
    array: random array
    val: index number
    :return: 'val'. element of array
    """
    return array[val]


if __name__ == '__main__':
    array = []

    # created random array
    for i in range(0, 10):
        # array filled random numbers
        array.append(random.randint(1, 10))

    val = input("which index: ")
    index_val = get_val(array, val)