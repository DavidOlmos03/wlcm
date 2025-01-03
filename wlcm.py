import tkinter as tk
import random
import threading
from pydub import AudioSegment
from pydub.playback import play


# Función para leer variables del archivo
def load_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:  # Verifica si la línea contiene '='
                key, value = line.split('=', 1)
                config[key] = value
    return config

# Cargar configuración desde el archivo
config = load_config("assets/config.txt")

# Obtener el nombre del usuario
user_name = config.get("USER_NAME", "Usuario")

# Obtener y dividir las frases motivacionales
motivational_quotes = config.get("MOTIVATIONAL_QUOTES", "").split(";")

# configuración del audio 
def speak(text):
    from gtts import gTTS
    tts = gTTS(text, lang='en')
    audio_file = "assets/welcome.mp3"
    tts.save(audio_file)

    audio = AudioSegment.from_file(audio_file)
    play(audio)


def create_welcome_window():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Bienvenida")
    root.geometry("400x200")  # Tamaño de la ventana
    root.resizable(False, False)  # Evitar redimensionar la ventana

    # Estilo de la ventana
    root.configure(bg="#f7f7f7")

    # Etiqueta de bienvenida
    welcome_text = f"Welcome {user_name}, good code"  
    welcome_label = tk.Label(
        root,
        text=welcome_text,
        font=("Helvetica", 16, "bold"),
        bg="#f7f7f7",
        fg="#333"
    )
    welcome_label.pack(pady=10)

    # Frase motivadora
    quote = random.choice(motivational_quotes)
    quote_label = tk.Label(
        root,
        text=f"'{quote}'",
        font=("Helvetica", 12, "italic"),
        bg="#f7f7f7",
        fg="#555",
        wraplength=350,
        justify="center"
    )
    quote_label.pack(pady=10)

    # Iniciar la lectura en un hilo secundario
    threading.Thread(target=speak, args=(f"{welcome_text}",), daemon=True).start()

    # Botón de cierre
    close_button = tk.Button(
        root,
        text="Cerrar",
        font=("Helvetica", 10, "bold"),
        bg="#ff6666",
        fg="white",
        command=root.destroy
    )
    close_button.pack(pady=10)

    # Mostrar la ventana
    root.mainloop()

# Llamar a la función para mostrar la ventana
create_welcome_window()

