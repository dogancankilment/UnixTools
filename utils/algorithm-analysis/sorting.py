import random
    
def bubbleSort(array):
    bubblecountkar=0
    bubblecountis=0
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            bubblecountkar=bubblecountkar+1
            if array[i]>array[i+1]:
                bubblecountis=bubblecountis+1
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    print "bubblecountkar", bubblecountkar
    print "bubblecountis", bubblecountis
 
    
    
def selectionSort(array):
    selectkar=0
    selectis=0
    for fillslot in range(len(array)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            selectkar=selectkar+1
            if array[location]>array[positionOfMax]:
                positionOfMax = location
                selectis=selectis+1
        temp = array[fillslot]
        array[fillslot] = array[positionOfMax]
        array[positionOfMax] = temp
    print "selectkar", selectkar
    print "selectis", selectis
    

def insertionSort(array):
   insertkar=0
   insertis=0
   for index in range(1,len(array)):
     insertkar=insertkar+1
     currentvalue = array[index]
     position = index

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1
         insertis=insertis+1
         insertkar=insertkar+1
     array[position]=currentvalue
   print "insertkar", insertkar
   print "insertis", insertis

def shellSort(array):
    shellkar=0
    shellis=0

    sublistcount = len(array)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(array,startposition,sublistcount,shellis,shellkar)

      sublistcount = sublistcount // 2

def gapInsertionSort(array,start,gap,shellis,shellkar):
    for i in range(start+gap,len(array),gap):

        currentvalue = array[i]
        position = i

        while position>=gap and array[position-gap]>currentvalue:
            array[position]=array[position-gap]
            position = position-gap
            shellis += 1
            shellkar += 1

        shellkar += 1
        dizi_is.append(shellis)
        dizi_kar.append(shellkar)
        array[position]=currentvalue
        

array1=[]
array2=[]
array3=[]
array4=[]
dizi_is=[]
dizi_kar=[]
    
for i in range(0,150):
        x= random.randint(1,10)
        array1.append(x)
        array2.append(x)
        array3.append(x)
        array4.append(x)
        
print "shellsort"
shellSort(array1)
print array1
print dizi_is
print dizi_kar
            
print "selectionsort"
selectionSort(array2)
print array2
    
print "bubblesort"
bubbleSort(array3)
print array3
    
print "insertionsort"
insertionSort(array4)
print array4
