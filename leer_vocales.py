import numpy as np
import matplotlib.pyplot as plt

file = r"muestras/output.txt"

data = np.loadtxt(file,comments='#', delimiter='\t')
t = data[:,0]
audio_signal = data[:,1]

lines = None

with open(file,'r') as file:
    lines = file.readlines()

fs_line = None
for line in lines:
    if'Frecuencia de muestreo' in line:
        fs_line = line

fs = None
if fs_line is not None:
    fs_value = fs_line.split(":")[1].strip()
    fs=int(fs_value)
else:
    raise ValueError("No se encontró la fruecuencia de muestreo")




#Graficar forma de onda del audio
plt.figure(figsize=(10,4))
plt.plot(t,audio_signal,label='Forma de onda audio')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Vocal')
plt.legend()
plt.grid(True)
plt.show()

#FFT
n = len(audio_signal)
frecuencia = np.fft.fftfreq(n,d=1/fs)
fft_signal = np.fft.fft(audio_signal)

positive_freqs = frecuencia[:n // 2]
positive_fft = np.abs(fft_signal[:n // 2])

plt.figure(figsize=(10, 4))
plt.plot(positive_freqs, positive_fft)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de Frecuencia')
plt.grid(True)
# Limitar el rango de frecuencias a mostrar, por ejemplo de 0 a 500 Hz
plt.xlim(-10, 1500)
plt.show()