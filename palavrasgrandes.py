#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("allkeys.txt")




arq="catatau.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(catatau) 


tokens = nltk.word_tokenize(catatau)

#catacorpus=nltk.Text(nltk.word_tokenize(catatau))


# ordenar
tokens.sort()



a = set(tokens)

glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

glossario.reverse()

a=""

for w in glossario:
	if len(w) >= 13:
		a=w+"               "+a


print a


############# grava arquivo
file = codecs.open("Neotatau.txt", "w", "utf-8")
file.write(a)
file.close()
