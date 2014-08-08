from optparse import OptionParser


def head():
    """
    Option parser for command line
    input variables in linux terminal.

    example to run code in terminal(command line)
    python Head_Command_Python.py -n 10 file

    """

    check = 0
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-n", "--number", type="int",
                      help="Duz metin belgelerinin ilk bir kac satirini goruntuler",
                      dest="head", default="10")
    (options, args) = parser.parse_args()

    how_many_lines = int(options.head)

    #with open(args[0], "r") as dosya:

    try:
        open_file=open(args[0],"r")

        for line in open_file:
            if check < how_many_lines:
                check = check+1
                print line.strip()
            else:
                break

    except:
        print "Valid user hasn't got read permission"
        print "File didn't open!"

    open_file.close()


if __name__ == '__main__':
    head()
