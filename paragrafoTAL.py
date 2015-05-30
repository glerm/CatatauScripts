#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
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



def encontra_palavra(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE| re.UNICODE).search


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

#contem com que
que=[]
for f in perguntas:
	if encontra_palavra('que')(f):
		que.append(f)

#inicia com quando
quandos=[]
for f in perguntas:
	if f.startswith("Quando"):
		quandos.append(f)
# inicia com porque
pq=[]
for f in perguntas:
	if f.startswith("Por que"):
		pq.append(f)

# inicia com onde
onde=[]
for f in perguntas:
	if f.startswith("Onde"):
		onde.append(f)


#P={'como':comos, 'quem':quems, 'quando':quandos, "pq":pq, "onde":onde}

#print P

#afirma

# contem nada
nada=[]
for f in afirma:
	if encontra_palavra('nada')(f):
		nada.append(f)

# contem tudo
tudo=[]
for f in afirma:
	if encontra_palavra('tudo')(f):
		tudo.append(f)

# afirma eu
eu=[]
for f in afirma:
	if encontra_palavra('eu')(f):
		eu.append(f)

# afirma eu
EU=[]
for f in exclama:
	if encontra_palavra('eu')(f):
		EU.append(f)

# exclama aqui
aqui=[]
for f in exclama:
	if encontra_palavra('aqui')(f):
		aqui.append(f)

# afirma mundo
mundo=[]
for f in afirma:
	if encontra_palavra('mundo')(f):
		mundo.append(f)

# afirma sempre
sempre=[]
for f in afirma:
	if encontra_palavra('sempre')(f):
		sempre.append(f)

# exclama curto
curto=[]
for f in exclama:
	if len(f) <= 13:
		curto.append(f)


#sorteia paragrafo
def sorteia_paragrafo():
	PARAGRAFO=random.choice(quems)+" "+random.choice(eu)+" "+random.choice(onde)+" "+random.choice(aqui)+" "+random.choice(quandos)+" "+random.choice(sempre)+" "+random.choice(comos)+" "+random.choice(nada)+" "+random.choice(que)+" "+random.choice(EU)+" "+random.choice(mundo)+" "+random.choice(tudo)+" "+random.choice(curto)
	return PARAGRAFO

txt=''
for x in xrange(3141):	
	txt=txt+"\n\n"+sorteia_paragrafo()



############# grava arquivo
file = codecs.open("ParagrafoTAL.txt", "w", "utf-8")
file.write(txt)
file.close()
