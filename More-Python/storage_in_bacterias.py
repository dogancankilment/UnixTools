def save_bacteria_dna():
    """
        0 = A,
        1 = T,
        2 = C,
        3 = G

        footnote:
        >>>ord('c')
        99
        >>>chr(97)
        'c'
        same unichr() command
    """

    char_list = []
    binary_list = []

    request_word = raw_input("Please enter the word,"
                             "you want to save in bacteria dna.")

    for i in request_word:
        char_list.append(ord(i))

    result = radix_changer(char_list, binary_list)
    print result


def radix_changer(char_list, binary_list):
    """
        10radix to 4radix number system
        for ex.:
            we've got only one character.
            And our character is c.

            'c' in ascii table;
                c=99

            function doing this;
                99 % 4 = 3 **
                99 / 4 = 24

            in this step:
                3 -> will be save value.
                24 -> in next process, value of c

            and every step doing this again.
            like;
                24 % 4 = 0 **
                24 / 4 = 6
                ----------
                6 % 4 = 2 **
                6 / 4 = 1 **
                   ...

            so our binary code in starred lines
                real character: c
                in_ascii_format: 99
                binary: 1203 :)
    """

    counter = 0
    while counter < len(char_list):
        number = char_list[counter]
        binary = ""

        while number >= 4:
            binary += str(number % 4)
            number /= 4

        binary += str(number)
        binary_list.append(binary[::-1])
        counter += 1

    # turn to genetic format
    # like 1203 -> TCAG
    result = recombinant_dna(binary_list)

    return result


def recombinant_dna(binary_list):
    """
        each binary_list value is 4base number
        its mean max_value for each character is 3
        for ex.:
            entering string: can
            by one by for chars;
                ascii: 1203 - 1201 - 1232
            and I will format this blocks
            for first char
                1 -> T
                2 -> C
                0 -> A
                3 -> G

            and finally c character saved 'TCAG' :)
    """

    counter = 0
    tmp_str, result_str = "", ""

    while counter < len(binary_list):
        tmp_str = binary_list[counter]

        for j in range(0, 4):
            if tmp_str[j] == '0':
                result_str += 'A'

            if tmp_str[j] == '1':
                result_str += 'T'

            if tmp_str[j] == '2':
                result_str += 'C'

            if tmp_str[j] == '3':
                result_str += 'G'

        result_str += chr(10)
        counter += 1

    return result_str


if __name__ == '__main__':
    save_bacteria_dna()