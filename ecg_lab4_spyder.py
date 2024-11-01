# -*- coding: utf-8 -*-
"""
PROCESAMIENTO DE SEÑAL EMG 

LABORATORIO 4

AUTORAS:
    
    MARIANA GARCIA T
    SARA MARIANA PINZON R
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, find_peaks, cwt, morlet
import pywt

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)  # Aplicar el filtro
    return y

def mostrar_parte_senal(tiempo, datos, datos_filtrados, fs):
    
    # Definir el rango de tiempo para la ventana rectangular
    start_time = 137.0  # tiempo inicial en segundos
    end_time = 140.0   # tiempo final en segundos
    
    start_index = int(start_time * fs)
    end_index = int(end_time * fs)

    # Graficar la señal original dentro de la ventana rectangular
    plt.figure(1)
    plt.plot(tiempo[start_index:end_index], datos[start_index:end_index], label='Señal EMG Original')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('mV')
    plt.title('Parte de señal ECG Original (sujeto 1)')
    plt.grid()

    # Graficar la señal filtrada dentro de la ventana rectangular
    plt.figure(2)
    plt.plot(tiempo[start_index:end_index], datos_filtrados[start_index:end_index], label='Señal EMG Filtrada', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('mV' )
    plt.title('Parte de señal ECG Filtrada (sujeto 1)')
    plt.grid()
    plt.tight_layout()
    plt.show()

def contar_picos_r(datos_filtrados, fs):
    # Umbral mínimo para picos 
    altura_minima = 150  
    picos, _ = find_peaks(datos_filtrados, height=altura_minima, distance=fs/2.5)
    return len(picos), picos 

def calcular_intervalo_rr(indices_picos, fs):
    # Calcular las diferencias entre índices de picos consecutivos
    intervalos_rr = np.diff(indices_picos) / fs  # Dividir por fs para obtener segundos
    return intervalos_rr

def calcular_parametros_HRV(intervalos_rr):
    media_rr = np.mean(intervalos_rr)
    desviacion_rr = np.std(intervalos_rr)
    return media_rr, desviacion_rr

 
def aplicar_transformada_wavelet(ecg_filtered, fs):
    # Definir parámetros
    dt = 1 / fs  # Intervalo de muestreo
    t = np.arange(len(ecg_filtered)) * dt  # Eje de tiempo

    scales = np.arange(1, 140)  # Ajusta este rango según sea necesario

    # Aplicar la transformada wavelet continua
    coeficientes_cwt = cwt(ecg_filtered, morlet, scales)

    # Generar el espectrograma
    plt.figure(figsize=(12, 6))
    plt.imshow(np.log1p(np.abs(coeficientes_cwt)), extent=[t[0], t[-1], scales[-1], scales[0]], aspect='auto',
               cmap='jet', interpolation='bilinear')
    plt.colorbar(label='Potencia (magnitud)')  # Cambié a log para mejorar visualización
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Escalas (correspondientes a Frecuencia en Hz)')
    plt.title('Espectrograma de la señal ECG utilizando Transformada Wavelet con Morlet')
    plt.ylim(1, 10)  # Ajustar según las escalas utilizadas
    plt.show()
    
    
    
def analisis_de_bandas(ecg_filtered, fs):

    frequencies = np.linspace(0.04, 0.4, num=100)
    scales = fs / frequencies
    scales = np.round(scales).astype(int)

    coeficientes_cwt = cwt(ecg_filtered, morlet, scales)

    lf_min, lf_max = 0.04, 0.15  # Banda de baja frecuencia
    hf_min, hf_max = 0.15, 0.4   # Banda de alta frecuencia

    frecuencias = fs / scales
    
    lf_indices = np.where((frecuencias >= lf_min) & (frecuencias <= lf_max))[0]
    hf_indices = np.where((frecuencias >= hf_min) & (frecuencias <= hf_max))[0]

    # Potencia en cada banda
    lf_power = np.sum(np.abs(coeficientes_cwt[lf_indices, :]), axis=0)
    hf_power = np.sum(np.abs(coeficientes_cwt[hf_indices, :]), axis=0)
    
    # Calcular el promedio de potencia para cada banda
    promedio_lf = np.mean(lf_power)
    promedio_hf = np.mean(hf_power)
    
    print(f"Promedio de potencia en banda LF: {promedio_lf}")
    print(f"Promedio de potencia en banda HF: {promedio_hf}")


    # Graficar la potencia en LF y HF a lo largo del tiempo
    plt.figure(figsize=(12, 6))
    plt.plot(np.arange(len(lf_power)) * (1/fs), lf_power, label='Banda de Baja Frecuencia', color='blue')
    plt.plot(np.arange(len(hf_power)) * (1/fs), hf_power, label='Banda de Alta Frecuencia', color='red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Potencia ')
    plt.legend()
    plt.title('Potencia en bandas de baja y alta frecuencia a lo largo del tiempo (Sujeto 2)')
    plt.grid()
    plt.show()

    
def main():
    ecg = open('datos_crudos_ecg2.txt')
    ecg_datas = ecg.read()
    ecg.close()
    
    ecg_data = []  
    for valor in ecg_datas.strip().split():
        ecg_data.append(float(valor))  
        
    fs = 1000.0
    lowcut = 5.0
    highcut = 50.0
    order = 3 

    # Filtrar la señal
    ecg_filtered = butter_bandpass_filter(ecg_data, lowcut, highcut, fs, order)

    # eje de tiempo
    tiempo = np.arange(len(ecg_data)) / fs

    mostrar_parte_senal(tiempo, ecg_data, ecg_filtered, fs)
    
    num_picos, indices_picos = contar_picos_r(ecg_filtered, fs)
    print(f"Número de picos R detectados: {num_picos}")
    
        # Calcular y mostrar los intervalos R-R
    intervalos_rr = calcular_intervalo_rr(indices_picos, fs)
    print(f"Intervalos R-R (en segundos): {intervalos_rr}")
    
    print(' ' )
    
    # Calcular y mostrar los parámetros de los intervalos R-R
    media_rr, desviacion_rr = calcular_parametros_HRV(intervalos_rr)
    print(f"Media de intervalos R-R: {media_rr:.4f} segundos")
    print(f"Desviación estándar de intervalos R-R: {desviacion_rr:.4f} segundos")
    
    print(' ')
    
    aplicar_transformada_wavelet(ecg_filtered, fs)
    analisis_de_bandas(ecg_filtered, fs)

if __name__ == "__main__":
    main()
