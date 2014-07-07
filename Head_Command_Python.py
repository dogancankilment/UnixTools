#!/usr/bin/python
#__author__ = 'markafonistajyer'

import os, sys
from optparse import OptionParser

def head():
    kontrol = 0
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-n", "--number", type="string",
                      help="Print Lines",
                      dest="tail", default="10")
    (options, args) = parser.parse_args()

    kac_satir = int(options.tail)

    #with open(args[0], "r") as dosya:
    try:
        dosya=open(args[0],"r")

        for satir in dosya:
            kontrol=kontrol+1
            print satir.strip()
            if kontrol >= kac_satir:
                break
    except:
        print "Gecerli kullanicinin dosya okuma izni bulunmamaktadir"
        print "Dosya acilamiyor!"

#example to run code in terminal(command line)
#python LinuxCommands.py -n 10 text.txt
if __name__ == '__main__':
    head()
