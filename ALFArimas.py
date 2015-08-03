#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")


# arquivo analisado (no mesmo diretorio)
arq="corpustxt/catatau_semlinebreaks.txt"
fileObj = codecs.open( arq, "r", "utf-8" )
mikrofesto = fileObj.read() 

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(mikrofesto) 



#separando pontuações do final de palavras e demais tokens
tokens = nltk.word_tokenize(mikrofesto)

# limpando conectivos
#cleanupDoc(tokens)

#formatando em estrutura de dados nltk para padronizar posteriormente
catacorpus=nltk.Text(nltk.word_tokenize(mikrofesto))


#convertendo para vetor para filtrar repetições
a = set(tokens)
# retornando para tipo lista
glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

# ordenado pelo reverso pra ficar de a até z
glossario.reverse()

# formatando separado por espaços e vírgulas
a=""
for w in glossario:
	a=w+", "+a

#formatando todas as terminações com 3
finais=[]
for w in glossario:
	finais.append(w[-3:])

#ordenado e filtrando repetições
finais = set(finais)
finais=list(finais)
finais=sorted(finais, key=c.sort_key)


#print finais
#print '\n\n\n'
#print 'total: '+str(len(finais))

rimas={}

for f in finais:
	l=[]
	for w in glossario:
		if w[-3:] == f:
			l.append(w)
			rimas[f]=l
	if len(rimas[f]) < 4:
		rimas.pop(f, None)


print rimas
print '\n\n\n'
print 'total: '+str(len(rimas))









############# grava arquivo
#file = codecs.open("AquiloLexico.txt", "w", "utf-8")
#file.write(a)
#file.close()
