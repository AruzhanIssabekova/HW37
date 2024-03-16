from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

chrome_o = Options()
chrome_o.add_argument("--headless")

s = Service(chrome_path)
s.start()
driver = webdriver.Chrome(service=s, options=chrome_o)

driver.get("https://uchet.kz/kursi_valut/")


time.sleep(5)


usd_e = driver.find_element(By.XPATH, "//td[text()='USD']/following-sibling::td")
eur_e = driver.find_element(By.XPATH, "//td[text()='EUR']/following-sibling::td")


usd = usd_e.text
eur = eur_e.text

print("Курс доллара:", usd)
print("Курс евро:", eur)


driver.quit()
