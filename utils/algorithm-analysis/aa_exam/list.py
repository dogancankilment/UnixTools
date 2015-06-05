import random


def function():
    size = int(raw_input("kac sayi girmek istiyorsunuz?"))
    array_list = resize(size)

    for i in range(0, size):
        array_list.append(random.randint(1))

    for i in range(size,0,-1):
        print array_list[i]


def resize(size):
    # mylist[size] in java List mylist = new ArrayList();
    # in c# List<int> mylist = new List<int>();
    mylist = [size]

    return mylist
