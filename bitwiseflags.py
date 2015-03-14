'''
Created on 14 Mar 2015

@author: aled
'''
import sys

bitflag={1:"template having multiple segments in sequencing", 2:"each segment properly aligned according to the aligner", 4:"segment unmapped",8:"next segment in the template unmapped", 10:"SEQ being reverse complemented", 20:"SEQ of the next segment in the template being reversed", 40:"the first segment in the template", 80:"the last segment in the template", 100:"secondary alignment", 200:"not passing quality control",400:"PCR or optical duplicate",800:"supplementary alignment"}


def printflag(bitno):
    print "bitflag="+str(bitno)+", "+'{0:012b}'.format(int(bitno))
    print bitflag [int(bitno)]

#printflag(2)
printflag(sys.argv[1])

