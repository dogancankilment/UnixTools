#!/usr/bin/python
from optparse import OptionParser

def head():

    kontrol = 0
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-n", "--number", type="int",
                      help="Duz metin belgelerinin ilk bir kac satirini goruntuler",
                      dest="head", default="10")
    (options, args) = parser.parse_args()

    kac_satir = int(options.head)

    #with open(args[0], "r") as dosya:
    try:
        dosya=open(args[0],"r")

        for satir in dosya:
            if( kontrol < kac_satir):
                kontrol=kontrol+1
                print satir.strip()
            else:
                break

    except:
        print "Gecerli kullanicinin dosya okuma izni bulunmamaktadir"
        print "Dosya acilamiyor!"

    dosya.close()

#example to run code in terminal(command line)
#python Head_Command_Python.py -n 10 text.txt
if __name__ == '__main__':
    head()
