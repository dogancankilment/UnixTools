def match():
    i, j = 1, 1

    first = raw_input('first word: ')
    second = raw_input('second word: ')

    for c1 in first:
      j = 1

      for c2 in second:
        if i == j and c1 == c2:
          print c1

        j += 1
      i += 1


if __name__ == '__main__':
    match()