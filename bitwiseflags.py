'''
Created on 14 Mar 2015

@author: aled
'''
import sys

bitflag={1:"template having multiple segments in sequencing", 2:"each segment properly aligned according to the aligner", 4:"segment unmapped",8:"next segment in the template unmapped", 10:"SEQ being reverse complemented"}


def printflag(bitno):
    print "bitflag="+str(bitno)+", "+'{0:012b}'.format(bitno)
    print bitflag [bitno]

printflag(2)
#printflag(sys.argv[1])

