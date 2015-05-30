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



# filtra repetições
a = set(catalinhas)
frases=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
frases=sorted(frases, key=c.sort_key)

#frases.reverse()


# termina em interrogação.
txt=""
conta=0

#perguntas curtas
perguntas=[]
for c in frases:
	c.replace(' ','\n')
	m = re.match("^.*\?$", c, re.MULTILINE)
	if m:
		perguntas.append(c)

#afirmações curtas
afirma=[]
for c in frases:
	c.replace(' ','\n')
	m = re.match("^.*\.$", c, re.MULTILINE)
	if m:
		afirma.append(c)

#exclamações curtas
exclama=[]
for c in frases:
	c.replace(' ','\n')
	m = re.match("^.*\!$", c, re.MULTILINE)
	if m:
		exclama.append(c)


#Perguntas com:
#inicia com como
comos=[]
for f in perguntas:
	if f.startswith("Como"):
		comos.append(f)
#inicia com quem
quems=[]
for f in perguntas:
	if f.startswith("Quem"):
		quems.append(f)
#inicia com quando
quandos=[]
for f in perguntas:
	if f.startswith("Por que"):
		quandos.append(f)
# inicia com porque
pq=[]
for f in perguntas:
	if f.startswith("Por que"):
		pq.append(f)




print comos
print quandos
print quems
print pq







############# grava arquivo
#file = codecs.open("Perguntau.txt", "w", "utf-8")
#file.write(txt)
#file.close()
