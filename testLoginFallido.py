from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from credenciales import invalidPass, invalidEmail

#cargar el webdriver
driver = webdriver.Chrome()
driver.get("https://test-qa.inlaze.com/auth/sign-in")
time.sleep(2)
#ubicar campos del login
emailBox  = driver.find_element(By.ID, "email")
passwordBox =  driver.find_element(By.ID, "password")
signButton = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
#ingresar datos
emailBox.send_keys(invalidEmail)
actions = ActionChains(driver)
actions.move_to_element(passwordBox).click().send_keys(invalidPass).perform()
time.sleep(2)
signButton.click()
time.sleep(6)

if not signButton.is_enabled():
    print("Validación correcta: El botón de registro sigue deshabilitado al no estar los campos correctamente")
else:
    print("Error: El botón de registro NO debería activarse")

driver.quit()