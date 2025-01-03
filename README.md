# wlcm

# Interfaz Gráfica de Bienvenida con Tkinter

Esta aplicación de Python utiliza `tkinter` para mostrar una ventana gráfica que te da la bienvenida al iniciar tu sistema. Además, incluye una frase motivadora y reproduce un mensaje de bienvenida en voz alta.

## Características

- Ventana gráfica simple y estilizada creada con `tkinter`.
- Frases motivadoras seleccionadas al azar.
- Lectura en voz alta del mensaje de bienvenida utilizando `gTTS`.
- Configuración para ejecutarse automáticamente al iniciar el sistema, tanto en Linux como en Windows.

---

## Requisitos Previos

1. Python 3.8 o superior.
2. Entorno virtual (opcional pero recomendado).
3. Paquetes listados en `requirements.txt`.

---

## Instalación

1. **Clona este repositorio o descarga el código fuente:**
   ```bash
   git clone https://github.com/DavidOlmos03/wlcm.git

2. **Crea un entorno virtual e instálalo (opcional):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/MacOS
    .venv\Scripts\activate     # Windows

3. **Instala las despendencias:**
    ```bash
    pip install -r requirements.txt

## Configuración para el Inicio Automático

### Linux (Ubuntu o distribuciones basadas en GNOME)

1. **Compilar la aplicación a un archivo ejecutable:**
   Para que la aplicación se ejecute como un programa independiente, primero debes compilar el archivo `wlcm.py` a un ejecutable utilizando `pyinstaller`. Abre una terminal y ejecuta el siguiente comando:
   ```bash
   pyinstaller --onefile --noconsole wlcm.py

Esto generará un archivo ejecutable dentro de la carpeta dist/. El archivo ejecutable tendrá el nombre wlcm (sin extensión).

2. **Crear el archivo wlcm.desktop en el directorio ~/.config/autostart**
    agrega el siguiente contenido a wlcm.desktop
    ```bash
    [Desktop Entry]
    Type=Application
    Name=WelcomeApp
    Exec=/ruta/completa/al/ejecutable/dist/wlcm
    X-GNOME-Autostart-enabled=true
    Comment=Aplicación de bienvenida que muestra un mensaje y reproduce audio

Nota: Cambia /ruta/completa/al/ejecutable/dist/wlcm a la ruta completa de tu archivo ejecutable generado por pyinstaller en el paso 1.

3. **Hacer el archivo .desktop ejecutable:** Asegúrate de que el archivo .desktop tenga permisos de ejecución. Puedes hacerlo con el siguiente comando:
    ```bash
    chmod +x ~/.config/autostart/wlcm.desktop
4. **Reiniciar la sesión:** Para probar que la aplicación se ejecuta correctamente al iniciar sesión, simplemente cierra la sesión de tu usuario y vuelve a iniciar sesión, o reinicia tu sistema.

### Windows

1. **Compila la aplicación a un archivo ejecutable:**
    ```bash
    pyinstaller --onefile --noconsole wlcm.py
Esto generará un archivo ejecutable en la carpeta dist/ (por ejemplo, dist\wlcm.exe).

2. **Crea un acceso directo del archivo ejecutable:**
   - Haz clic derecho en el ejecutable (dist\wlcm.exe) y selecciona "Crear acceso directo".

3. Añade el acceso directo a la carpeta de inicio:
    - Presiona **Win + R**, escribe **shell:startup** y presiona Enter.
    - Copia el acceso directo generado en la carpeta que se abre.

4. Reinicia tu sistema para probar la aplicación.
