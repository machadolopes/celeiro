from selenium import webdriver
from datetime import date
#cria driver para webscraping
driver = webdriver.Chrome()

#seleciona o dia atual do diário oficial
today = date.today()
dia = today.strftime("%d")
mes = today.strftime("%m") 
ano = today.strftime("%Y")
caderno = 'https://www.jusbrasil.com.br/diarios/documentos/DJRJ/'+ano+'/'+mes+'/'+dia+'/Iii-judicial-1a-instancia-capital/'
driver.get(caderno)
documentos = driver.find_elements_by_class_name('number')
ultima_pagina = int(documentos[-1].text)


driver.close()


