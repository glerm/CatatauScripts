#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
from string import ascii_lowercase


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


#convertendo para vetor para filtrar repitições
a = set(tokens)
# retornando para tipo lista
glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

# ordenado pelo reverso pra ficar de a até z
glossario.reverse()

# formatando separado por espaços e vírgulas
a=""

for letra in ascii_lowercase:
	for w in glossario:
		if bool(re.match('['+letra+'|'+letra.upper()+']',w)):
			a="<a href=\"http://localhost:5000/"+w+"\">"+w+"</a> "+a

	c="<html><head><title>ALFA:Ta:TAL</title><style>a:link{color:#000000; font-family: \"courier\";line-height: 20px; font-size: 13px; text-decoration: none} a:visited{#BBBBBB; font-family: \"courier\"; line-height: 20px; font-size: 13px; text-decoration: none} a:hover{background-color:yellow;font-size: 20px;font-family: \"courier\"}</style><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><body><a href=\"\"><img src=\"seta_esquerda.png\" height=\"40\">Volta</a></br></br>"
	t="</body></html>"

	a=c+a+t
	print "Gravando letra: "+letra+"\n"
	############# grava arquivo
	file = codecs.open('indice/'+letra+'_lexico.html', 'w', 'utf-8')
	file.write(a)
	file.close()
	a=""


