def perfect_number():
    sum, count, number = 0, 0, 1
    top = input("enter a top value: ")

    while number < top:
        for i in range(1, number/2+1):
            if number/i*i == number:
                sum += i
        if sum == number:
            count += 1
            print count, ".perfect number: ", number

        number += 1
        sum = 0

    if count == 0:
        print "any perfect number in this range"


if __name__ == '__main__':
    perfect_number()