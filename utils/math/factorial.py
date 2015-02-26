def factorial():

    result = 1
    top = input("give me the number ")
    for i in range(1, top+1):
        result *= i
    print result


if __name__ == '__main__':
    factorial()