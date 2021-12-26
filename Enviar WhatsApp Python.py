import pandas as pd

contatos_df = pd.read_excel(r'C:\Users\winst\OneDrive\Documentos\CODE\PYTHON\Projetos\Whatsapp_AutoBot\enviar.xlsx')



# In[20]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome('C:/Users/winst/OneDrive/Documentos/CODE/PYTHON/chromedriver')
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Nome"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    Enviar_Mensagem = navegador.find_element_by_xpath("//span[@data-icon='send']")
    Enviar_Mensagem.click()
    time.sleep(5)

