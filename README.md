# Laboratorio 02: Flujo de trabajo en Django

**Institución:** Tecsup  
**Curso:** Desarrollo de Aplicaciones Web  
**Tema:** Definir controladores. Pasar datos a los objetos de visualización.  
**Docente:** Hector Manrique Morante  
**Alumno:** Quispe Vila Christopher Mael  

---

## 📌 Descripción del Proyecto

Este repositorio contiene la solución completa del **Laboratorio N° 02**, donde se profundiza en la arquitectura MVT (Model-View-Template) de Django, el flujo de petición-respuesta (Request-Response), el manejo de formularios HTML con tokens CSRF, y el paso de datos dinámicos mediante el objeto `context`.

---

## 🚀 Contenido y Funcionalidades

1. **Actividad 2: Aplicación de Encuesta (`/encuesta/`)**
   - Formulario completo con inputs de texto, contraseña, selección simple, radio buttons y checkboxes múltiples.
   - Envío de datos por método `POST` con protección `{% csrf_token %}`.
   - Vista controladora que procesa los datos y renderiza la plantilla de respuesta (`respuesta.html`) usando bucles `{% for %}`.

2. **Actividad 3 / Tarea 1: Operaciones Matemáticas (`/encuesta/operaciones/`)**
   - Formulario que solicita dos datos numéricos.
   - Lista desplegable `<select>` para elegir la operación: Suma, Resta o Multiplicación.
   - Vista de respuesta dinámica que presenta el cálculo exacto (ejemplo: `La suma de 18 + 19 = 37`).

3. **Actividad 3 / Tarea 2: Cálculo del Volumen de un Cilindro (`/encuesta/cilindro/`)**
   - Formulario que solicita diámetro y altura en metros.
   - Implementación de la fórmula física:
     $$V = \pi \cdot r^2 \cdot h = \pi \cdot \left(\frac{d}{2}\right)^2 \cdot h$$
   - Salida formateada (ejemplo: `El volumen del cilindro es de 6.35338096859 metros cúbicos`).

---

## 🛠️ Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/QuispeVilaChristopherMael/Lab_02.git
   cd Lab_02
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv myvenv
   # En Windows:
   myvenv\Scripts\activate
   # En Linux/Mac:
   source myvenv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones del sistema:**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Acceder en el navegador:**
   - **Inicio / Encuesta:** [http://localhost:8000/encuesta/](http://localhost:8000/encuesta/)
   - **Operaciones Matemáticas:** [http://localhost:8000/encuesta/operaciones/](http://localhost:8000/encuesta/operaciones/)
   - **Volumen de Cilindro:** [http://localhost:8000/encuesta/cilindro/](http://localhost:8000/encuesta/cilindro/)

---

## 🧪 Pruebas Unitarias Automatizadas

El proyecto incluye 8 pruebas unitarias automatizadas que validan todas las vistas y cálculos:
```bash
python manage.py test encuesta
```
Resultado:
```text
Ran 8 tests in 0.026s
OK
```

---

## 🔒 Seguridad y Privacidad

- Se implementó un `.gitignore` estricto que previene la subida de entornos virtuales (`myvenv/`), bases de datos SQLite (`*.sqlite3`), archivos compilados (`__pycache__/`) y credenciales o variables de entorno (`.env`).
- Las variables sensibles del proyecto (`SECRET_KEY`, `DEBUG`) están configuradas para cargarse de variables de entorno con valores seguros por defecto para desarrollo.
