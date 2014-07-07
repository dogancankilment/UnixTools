#!/usr/bin/python
from optparse import OptionParser

def tail():

    parser = OptionParser()
    usage = "usage: %prog [options] arg1 "

    parser.add_option("-c", "--continuous", type="int",
                      help="Duz metin belgelerinin son bir kac satirini surekli olarak goruntuler",
                      dest="tail", default="10")
    (options, args) = parser.parse_args()

    kac_satir = int(options.tail)

    #with open(args[0], "r") as dosya:
    try:
        i=0
        dosya=open(args[0],"r")
        satir_sayisi = sum(1 for line in dosya)
        dosya=open(args[0],"r")

        j = satir_sayisi - kac_satir
        #j burada kacinci satirdan itibaren gosterecegimizi
        #kaydedecegimiz degisken

        for satir in dosya:
            if i >= j:
                print satir.strip()
            i=i+1

        # for satir in reversed(dosya.readlines()): #satirlari terse cevirerek okumak

    except:
        print "Gecerli kullanicinin dosya okuma izni bulunmamaktadir"
        print "Dosya acilamiyor!"

    dosya.close()

#example to run code in terminal(command line)
#python Tail_Command_Python.py -c 10 text.txt

if __name__ == '__main__':
    tail()
