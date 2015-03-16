'''
Created on 14 Mar 2015

@author: aled
'''
import sys

bitflag={11:"template having multiple segments in sequencing", 10:"each segment properly aligned according to the aligner", 9:"segment unmapped",8:"next segment in the template unmapped", 7:"SEQ being reverse complemented", 6:"SEQ of the next segment in the template being reversed", 5:"the first segment in the template", 4:"the last segment in the template", 3:"secondary alignment", 2:"not passing quality control",1:"PCR or optical duplicate",0:"supplementary alignment"}
#print bitflag[11]

def convert_to_bin(number):
    binary='{0:012b}'.format(int(number))
    #print binary
    printflag(number,binary)

def printflag(bitno,binary):
    print "bitflag="+str(bitno)+", "+binary
    #print bitflag [int(bitno)]
    for i in xrange (11,0,-1):
        if binary[i] == '1':
            #print i
            print bitflag[i]
             
        
        
        
#convert_to_bin(147)
convert_to_bin(sys.argv[1])

