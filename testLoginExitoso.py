from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#cargar el webdriver
driver = webdriver.Chrome()
driver.get("https://test-qa.inlaze.com/auth/sign-in")
time.sleep(2)

#ubicar campos del login
emailBox  = driver.find_element(By.ID, "email")
passwordBox =  driver.find_element(By.ID, "password")
signButton = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")

#ingresar datos
emailBox.send_keys("diego22@gmail.com")
actions = ActionChains(driver)
actions.move_to_element(passwordBox).click().send_keys("Diego1510").perform()
time.sleep(2)
signButton.click()
time.sleep(6)

#validar login
#se valida por medio de un condicional que luego del login la url haya cambiado y que aparezca el campo con el nombre del usuario logueado
urlWelcome = "https://test-qa.inlaze.com/panel"
try:
    if urlWelcome in driver.current_url:
        print("URL correcta luego del login")
    else:
        print("URL incorrecta luego del login")

    nombreUsuario = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'font-bold')]"))
    )
    print(f" Login exitoso, Usuario: {nombreUsuario.text}")

except Exception as e:
    print("login fallido")

#cerrar sesion
#se localiza el div que contiene el menu desplegable, luego se localiza y clickea la opcion de Logout y se valida el cierre de sesion
try:
    usuarioMenuButton = driver.find_element(By.XPATH, "//app-navbar//div[2]//label")
    usuarioMenuButton.click()
    WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul"))
    )
    logOutButton = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Logout')]"))
    )
    time.sleep(3)
    logOutButton.click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://test-qa.inlaze.com/auth/sign-in"))
    print("log out exitoso")

except Exception as e:
    print("log out fallido")

driver.quit()

