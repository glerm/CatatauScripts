#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")
arq="corpustxt/exclama.txt"


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

#frases.reverse()


# termina em interrogação.
txt=""
conta=0
for c in frases:
	c.replace(' ','\n')
	m = re.match("^.*\!$", c, re.MULTILINE)
	if m:
		#print(c)
		txt=txt+c+" \n\n"
		conta=conta+1
txt=txt+"\n total de linhas= "+str(conta)
	
frases.reverse()

print frases


############# grava arquivo
file = codecs.open("Exclamatau.txt", "w", "utf-8")
file.write(txt)
file.close()
