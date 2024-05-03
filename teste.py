from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Inicializar o driver do navegador (nesse caso, o Chrome)
driver = webdriver.Chrome()

# Abrir o Google
driver.get("https://www.google.com")

# Localizar o campo de pesquisa e enviar o termo de pesquisa
search_box = driver.find_element(By.NAME, "q")
search_term = "Inteligência Artificial"  # Termo de pesquisa desejado
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

# Aguardar um pouco para os resultados serem exibidos
driver.implicitly_wait(5)

# Obter todos os títulos dos resultados da pesquisa e imprimi-los
results = driver.find_elements(By.CSS_SELECTOR, "h3")
print("Resultados da pesquisa para:", search_term)
for result in results:
    print(result.text)

# Fechar o navegador
driver.quit()
