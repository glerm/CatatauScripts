#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
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

frases.reverse()


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/<var1>')
def busca(var1):
	b = re.compile("\\b"+var1+"\\b", re.IGNORECASE)
	txt=''
	for f in frases:
		achou = re.search(b, f)
		if achou:
			txt='<p>'+f+'</h3></p>'+txt
	return txt



if __name__ == "__main__":
	app.run()
