#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")


# arquivo analisado (no mesmo diretorio)

cola=''

for x in xrange(24):
	arq= 'corpustxt/iliada/canto'+str(x+1)+".txt"
	print "abrindo :"+ arq
	fileObj = codecs.open( arq, "r", "utf-8" )
	arqtxt = fileObj.read() 
	cola=cola+arqtxt




############# grava arquivo
file = codecs.open("TODAILIADA.txt", "w", "utf-8")
file.write(cola)
file.close()
