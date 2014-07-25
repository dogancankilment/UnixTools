#!/usr/bin/python
from optparse import OptionParser


def grep():
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-c", "--count", type="string",
                      help="Eslesen ifadenin dosya icerisinde toplamda kac defa gectigini soyler",
                      dest="grep_c", default=" ")

    parser.add_option("-w", "--word", type="string",
                      help="Satirlardaki kelime eslesmesi",
                      dest="grep_w", default=" ")

    (options, args) = parser.parse_args()

    gonderilen_str = str(options.grep_w)
    dosya=open(args[0],"r")

    for satir in dosya:
        if gonderilen_str in satir.split():
            print satir

#example to run code in terminal(command line)
#python Head_Command_Python.py -n 10 text.txt

if __name__ == '__main__':
    grep()
