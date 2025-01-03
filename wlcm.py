import tkinter as tk
import random
import pyttsx3
import threading

# Lista de frases motivadoras
motivational_quotes = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "La única manera de hacer un gran trabajo es amar lo que haces.",
    "No importa qué tan lento vayas, siempre y cuando no te detengas.",
    "El futuro pertenece a quienes creen en la belleza de sus sueños.",
    "La acción es la clave fundamental de todo éxito."
]

# Función para sintetizar voz
# def speak(text):

    # engine = pyttsx3.init()
    #
    # voices = engine.getProperty('voices')
    #
    # engine.setProperty('rate', 150)  # Velocidad de la voz
    # engine.setProperty('volume', 1.0)  # Volumen de la voz
    # engine.say(text)
    # engine.runAndWait()

from pydub import AudioSegment
from pydub.playback import play

def speak(text):
    from gtts import gTTS
    tts = gTTS(text, lang='en')
    audio_file = "welcome.mp3"
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
    welcome_text = "Welcome David, good code"  # Cambia tu nombre aquí
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

