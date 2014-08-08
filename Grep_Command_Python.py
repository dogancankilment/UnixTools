from optparse import OptionParser


def grep():
    """
    Option parser for command line
    input variables in linux terminal.

    example to run code in terminal(command line)
    python Grep_Command_Python.py -w <word> file_name.txt

    """

    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-c", "--count", type="string",
                      help="print lines matching a pattern",
                      dest="grep_c", default=" ")

    parser.add_option("-w", "--word", type="string",
                      help="Select  only  those lines"
                           "containing matches that "
                           "form whole words.",
                      dest="grep_w", default=" ")

    (options, args) = parser.parse_args()

    sending_str = str(options.grep_w)
    open_file = open(args[0], "r")

    for line in open_file:
        if sending_str in line.split():
            print line


if __name__ == '__main__':
    grep()
