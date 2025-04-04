## Programa que obtiene las muestras del audio mp4 y las pasa a un txt.
from pydub import AudioSegment
import numpy as np

frecuencia_muestreo = 5000
periodo_muestreo = 1/frecuencia_muestreo

audio = AudioSegment.from_file("audios/b_agudo.mp4",format="mp4")
audio = audio.set_frame_rate(frecuencia_muestreo)       #Establece la frec. de muestreo
samples = np.array(audio.get_array_of_samples())        #Guardo las muestras en un array

time = np.linspace(0,len(samples)*periodo_muestreo,len(samples))    #"eje x" del tiempo con cada salto equivalente a un periodo de muestreo


diccionario = dict(zip(time,samples))

with open("muestras/output.txt", "w") as f:
    f.write(f"# Frecuencia de muestreo: {frecuencia_muestreo}\n")
    for key, value in diccionario.items():
        f.write(f"{key}\t{value}\n")
