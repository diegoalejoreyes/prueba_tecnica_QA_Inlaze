import secrets
import string
from faker import Faker
import time

#se crean datos dinamicos para los campos de nombre, correo y contraseña
#mediante las funciones y librerias de faker, secrets y time
fake = Faker()
validName = fake.first_name() + " " + fake.last_name()
print(validName)

email = f"usuario{int(time.time())}@test.com"
print(email)

def generar_password(longitud = 8):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))
password = generar_password()
print(password)

invalidName = "pablo"
invalidEmail = "correo.com"
invalidPass = "abc"

