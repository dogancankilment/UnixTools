import random


def get_max(array):
    """
    Find max value of random array
    with using bubble sort algorithm
    Algorithm Complexity: O(n**2)
    """

    for k in range(1, len(array)-1):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                tmp = array[j+1]
                array[j+1] = array[j]
                array[j] = tmp

    return array[len(array)-1]

if __name__ == '__main__':
    array = []

    # created random array
    for i in range(0, 10):
        # array filled random numbers
        array.append(random.randint(1, 10))

    max_val = get_max(array)