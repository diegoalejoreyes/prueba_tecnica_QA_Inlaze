from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from credenciales import invalidPass, invalidName, invalidEmail

#cargar el webdriver
driver = webdriver.Chrome()
driver.get("https://test-qa.inlaze.com/auth/sign-in")
time.sleep(3)

registerLink = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/span/a")
registerLink.click()
time.sleep(3)

#localizar campos del formulario
nameBox = driver.find_element(By.ID, "full-name")
emailBoxRegister = driver.find_element(By.ID, "email")
# passBoxRegister = driver.find_element(By.ID, "password")
passBoxRegister = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password")))
confirmPassBoxRegister = driver.find_element(By.ID, "confirm-password")
registerButton = driver.find_element(By.XPATH,
                                     "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button")

#ingresar datos
nameBox.send_keys(invalidName)
emailBoxRegister.send_keys(invalidEmail)
# se crea un objeto tipo ActionChains que permite simular acciones de un usuario real, dado que el campo 'password'
# tiene el atributo autocomplete="password" lo cual puede bloquear el ingreso de texto
actions = ActionChains(driver)
actions.move_to_element(passBoxRegister).click().send_keys(invalidPass).perform()
actions.move_to_element(confirmPassBoxRegister).click().send_keys(invalidPass).perform()
time.sleep(2)
registerButton.click()
time.sleep(5)

if not registerButton.is_enabled():
    print("Validación correcta: El botón de registro sigue deshabilitado al no estar los campos correctamente")
else:
    print("Error: El botón de registro NO debería activarse")

driver.quit()