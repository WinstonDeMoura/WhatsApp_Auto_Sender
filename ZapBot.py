import pandas as pd

contatos_df = pd.read_excel('enviar.xlsx')


from selenium import webdriver
import time
import urllib

navegador = webdriver.Chrome('chromedriver.exe')

for i, mensagem in enumerate(contatos_df['Mensagem']):
  pessoa = contatos_df.loc[i, "Nome"]
  numero = contatos_df.loc[i, "Número"]
  texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")

  link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
  navegador.get(link)
  time.sleep(15)
  sendmsg = navegador.find_element_by_xpath("//span[@data-icon='send']").click()
  time.sleep(5)