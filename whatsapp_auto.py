import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from numpy import random
import time
from time import sleep
import urllib

contatos_df = pd.read_excel(r'C:\Users\winst\OneDrive\Documentos\CODE\PYTHON\Projetos\Whatsapp_AutoBot\enviar.xlsx')

navegador = webdriver.Chrome('C:/Users/winst/OneDrive/Documentos/CODE/chromedriver')
navegador.get("https://web.whatsapp.com")

while len(navegador.find_elements_by_id("side")) < 1:
  time.sleep(1)

#Login já feito

for i, mensagem in enumerate(contatos_df['Mensagem']):
  pessoa = contatos_df.loc[i, "Nome"]
  numero = contatos_df.loc [i, "Número"]
  texto = urllib.parse.quote(f"Oi, {pessoa}! {mensagem}")
  link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
  navegador.get(link)
  while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)
  barra = navegador.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
  barra.send_keys(link)
  barra.send_keys(Keys.RETURN)
  time.sleep(5)