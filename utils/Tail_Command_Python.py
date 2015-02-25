from optparse import OptionParser


def tail():
    """
    Option parser for command line
    input variables in linux terminal.

    example to run code in terminal(command line)
    python Tail_Command_Python.py -c 10 file

    """

    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-c", "--continuous", type="int",
                      help="output  the  last  K bytes",
                      dest="tail", default="10")
    (options, args) = parser.parse_args()

    how_many_lines = int(options.tail)

    #with open(args[0], "r") as open_file:
    try:
        i = 0
        open_file = open(args[0],"r")
        lines_count = sum(1 for line in open_file)

        open_file = open(args[0],"r")
        j = lines_count - how_many_lines
        # j: starting which line to save

        for line in open_file:
            if i >= j:
                print line.strip()
            i += 1

        # reverse lines
        # for satir in reversed(dosya.readlines()):
    except:
        print "Gecerli kullanicinin dosya okuma izni bulunmamaktadir"
        print "Dosya acilamiyor!"

    open_file.close()


if __name__ == '__main__':
    tail()
