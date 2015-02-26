def primeNumber_1():

    division_count = 0
    number = input("give me the number ")

    for i in range(2, number+1):
        if number/i*i == number:
            division_count += 1

    if division_count == 1:
        print "it's prime"

    else:
        print "it is not prime"


def primeNumber_2():

    i = 2
    number = input("give me the number: ")

    while i**2 <= number:
        if number/i*i == number:
            print "it is not prime"
            break

        i += 1

    if number/i*i != number:
        print "it's prime"


if __name__ == '__main__':
    primeNumber_1()
    primeNumber_2()