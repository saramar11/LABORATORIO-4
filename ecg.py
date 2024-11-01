import sys #permite usar comandos
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow,  QApplication, QVBoxLayout, QWidget
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import serial.tools.list_ports #pyserial
import serial
import numpy as np
import struct

import threading

import scipy.signal as signal
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class principal(QMainWindow):
    def __init__(self): #self = hereda todo lo que tenga esa clase
        super(principal,self).__init__() #permite manejar el resto de objetos
        uic.loadUi("ecginterfaz1.ui",self)
        self.puertos_disponibles()
        self.ser = None
        self.connect.clicked.connect(self.conectar) #cuando oprima el boton que se ejecute la funcion 

        self.x = np.linspace(0,2,2000)
        self.y = np.linspace(0,0,2000)

        self.fig = Figure() #creando un plot
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.senalEMG.setLayout(layout)

        self.datos_guardados = [] 


        self.figA = Figure()
        self.axA = self.figA.add_subplot(111)
        self.canvasA = FigureCanvas(self.figA)
        layoutA = QVBoxLayout()
        layoutA.addWidget(self.canvasA)
        self.senalFiltrada.setLayout(layoutA)

        self.fs = 1000.0  
        # Frecuencia de corte (Hz)
        self.fc = 10.0  # Ajusta esta frecuencia de corte según tus necesidades
        # Normalizar la frecuencia de corte
        self.w = self.fc / (self.fs / 2)
        # Crear un filtro Butterworth de orden 4
        self.b, self.a = signal.butter(4, self.w, 'low')
        
    def puertos_disponibles(self):
        p = serial.tools.list_ports.comports()
        for port in p:
            self.puertos.addItem(port.device) #pone la lista de item en los puertos

    def conectar(self):
        estado = self.connect.text()
        self.stop_event_ser= threading.Event()
        if estado == "CONECTAR":
            com = self.puertos.currentText()
            try:
                self.ser = serial.Serial(com,115200)
                self.hilo_ser = threading.Thread(target=self.periodic_thread)
                self.hilo_ser.start()
                print("Puerto serial conectado")
                self.connect.setText("DESCONECTAR")
            except serial.SerialException as e:
                print("Error en el puerto serial: ", e)
        else:
            if self.ser:
                self.ser.close()
            self.stop_event_ser.set()
            self.hilo_ser.join()
            
            # Guardar los datos crudos en un archivo al desconectar
            if hasattr(self, 'datos_guardados') and self.datos_guardados:
                try:
                    with open("datos_crudos_ecg2.txt", "w") as data_file:
                        for value in self.datos_guardados:
                            data_file.write(f"{value}\n")
                    print("Datos crudos guardados en archivo datos_crudos_ecg.txt")
                except Exception as e:
                    print("Error al guardar los datos crudos:", e)
            else:
                print("No hay datos crudos para guardar.")
            self.connect.setText("CONECTAR")
    
    def periodic_thread(self):
        if self.ser is not None and self.ser.is_open:
            data = self.ser.read(200)  # Leer 200 bytes para obtener 100 muestras (2 bytes por muestra)
            if len(data) == 200:
                data = struct.unpack('100H', data)  # 100 enteros de 16 bits sin signo
                for value in data:
                    self.datos_guardados.append(value)
                    self.y = np.roll(self.y, -1)
                    self.y[-1] = (value * 3.3) / 1023  # Escala según el voltaje de referencia de Arduino

                # Señal sin filtrar
                self.ax.clear()
                self.ax.plot(self.x, self.y)
                self.ax.grid(True)
                self.canvas.draw()

                # Señal filtrada
                self.y_filtrada = signal.filtfilt(self.b, self.a, self.y)
                self.axA.clear()
                self.axA.plot(self.x, self.y_filtrada)
                self.axA.grid(True)
                self.canvasA.draw()
        if not self.stop_event_ser.is_set():
            threading.Timer(0.01, self.periodic_thread).start()  # Ajusta el tiempo de muestreo a 10 ms

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = principal()
    ventana.show() #permite acceder a la ventana y graficarla, mostrar la interfaz
    sys.exit(app.exec())
    
        
