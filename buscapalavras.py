#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")
arq="corpustxt/todasfrases.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(catatau) 



# filtra repetições
a = set(catalinhas)
frases=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
frases=sorted(frases, key=c.sort_key)

#palavra=sys.argv[1]
palavra=u'dízima'

busca = re.compile("\\b"+palavra+"\\b", re.IGNORECASE)

vezes=0

for f in frases:
	achou = re.search(busca, f)
	if achou:
		print f
		#vezes=vezes+1

print "\n"+str(vezes)+"vezes."


		


