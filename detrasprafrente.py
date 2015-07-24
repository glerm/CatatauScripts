#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")
arq="corpustxt/catatau_semlinebreaks.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(catatau) 

catalinhas.reverse()

txt=''
for linha in catalinhas:
	txt=txt+linha+' '



print catalinhas

############# grava arquivo
file = codecs.open("UATATAK.txt", "w", "utf-8")
file.write(txt)
file.close()
