# 🛠️ Prueba Técnica QA - Inlaze

## 📌 Descripción
Este proyecto es una automatización de pruebas para el sistema de registro y autenticación de usuarios en la plataforma Inlaze, utilizando Selenium con Python.

Incluye pruebas automatizadas para:

✅ Registro de usuario

✅ Inicio de sesión

✅ Cierre de sesión

✅ Validaciones de campos

El objetivo es asegurar la calidad del sistema y detectar posibles errores en el flujo de autenticación.

---

## ⚙️ Tecnologías Utilizadas
- Python 3.x
- Selenium WebDriver
- WebDriver para Chrome
- Pytest (opcional para ejecutar múltiples pruebas)

---

## 📋 Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x** (Descargar: [https://www.python.org/downloads/](https://www.python.org/downloads/))
-  **Google Chrome**
-   *Instalar WebDriver** correspondiente a tu navegador:
     - [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
- **Instalar dependencias del proyecto**  

---

## 📦 Instalación

### 1️⃣ Clonar el repositorio
```
- git clone https://github.com/diegoalejoreyes/prueba_tecnica_QA_Inlaze.git
- cd prueba_tecnica_QA_Inlaze
```
### 2️⃣ Crear un Entorno Virtual
```
python -m venv venv
```
- En Windows:
```
venv\Scripts\activate
```
### 3️⃣ Instalar dependencias
```
pip install -r requirements.txt
```

## Ejecucion de las pruebas
### Ejecutar una prueba especifica (login, por ejemplo)
```
python testLoginExitoso.py
```
### Ejecutar Todas las Pruebas con Pytest (Opcional)
```
pytest -v
```

## 📌 Notas Finales
- El diseño de casos de prueba y los bugs encontrados se encuentran en la carpeta de Documentacion
- El archivo credenciales.py se encuentran toda la data para ejecutar las pruebas
- Si el WebDriver no funciona, revisa que su versión coincida con la de tu navegador.
- Si alguna prueba falla, revisa el XPath de los elementos porque la estructura de la página puede cambiar.

### 📌 Autor: Diego Alejandro Reyes 
