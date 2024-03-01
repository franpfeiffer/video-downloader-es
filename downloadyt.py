import re
import os
from pytube import YouTube
from tkinter import Tk, filedialog, Label, Entry, Button, ttk

def download_video():
    link = input_link.get()

    youtube_link_pattern = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')

    if not youtube_link_pattern.match(link):
        result.config(text="Ingresa un link valido >:(", foreground="red")
    else:
        try:
            video = YouTube(link)

            root = Tk()
            root.withdraw()

            download_folder = filedialog.askdirectory(title="Selecciona una carpeta a la que ira el video")

            stream = video.streams.get_highest_resolution()
            if stream:
                download_path = os.path.join(download_folder, f"{video.title}.mp4")
                stream.download(output_path=download_folder, filename=video.title)
                result.config(text=f"Descargado correctamente! El video se envio a: {download_path}", foreground="green")
            else:
                result.config(text="No esta disponible en esa resolucion.", foreground="red")

        except Exception as e:
            result.config(text=f"Error: {e}", foreground="red")

if __name__ == "__main__":
    window = Tk()
    window.title("Download YT video")

    style = ttk.Style()
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("JetBrains Mono", 20))
    style.configure("TButton", padding=5, font=("JetBrains Mono", 10, "bold"), background="grey", foreground="green")
    style.configure("TEntry", font=("JetBrains Mono", 20))

    frame = ttk.Frame(window, style="TFrame")
    frame.grid(row=0, column=0, padx=30, pady=30)

    label_introduction = ttk.Label(frame, text="Por favor, ingresa tu link:", style="TLabel")
    input_link = ttk.Entry(frame, width=70, style="TEntry")
    button_download = ttk.Button(frame, text="Descargar", command=download_video, style="TButton")

    label_introduction.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    input_link.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
    button_download.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    result = ttk.Label(frame, text="", style="TLabel", foreground="black")
    result.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    window.mainloop()

