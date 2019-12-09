from selenium import webdriver
from datetime import date
#cria driver para webscraping
driver = webdriver.Chrome()

#seleciona o dia atual do diário oficial
today = date.today()
dia = today.strftime("%d")
mes = today.strftime("%m") 
ano = today.strftime("%Y")
#seleciona caderno com base no dia mês e ano atual
caderno = 'https://www.jusbrasil.com.br/diarios/documentos/DJRJ/'+ano+'/'+mes+'/'+dia+'/Iii-judicial-1a-instancia-capital/'
driver.get(caderno)
#conta total de páginas no caderno
total_paginas = driver.find_elements_by_class_name('number')
#calcula a última página do caderno
ultima_pagina = int(total_paginas[-1].text)
#seleciona documentos da página
documentos = driver.find_elements_by_class_name('journal-block-title')
lista_documentos = ()
for docs in documentos:
    docs.click()
    documento_completo = driver.find_element_by_class_name('DocumentView-content document-content fos-bottomref')
    documentos_info = driver.find_element_by_class_name('DocumentView-content-text')
    lista_documentos.append(documentos_info)
print (lista_documentos)
driver.close()


