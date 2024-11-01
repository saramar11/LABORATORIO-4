Autoras: Mariana Garcia & Sara Mariana Pinzón


# LABORATORIO 4 

Mediante el siguiente laboratorio se busca adquirir una señal ECG y mediante la aplicaciones que se puede tener con la transformada wavelet, determinar la actividad de la activador del sistema autónomo en la que se encuentra la persona evaluada.

## Fundamentación teórica
 
Con el fin de cumplir con estos objetivos, inicialmente se realizó una exploración con respecto a algunos conceptos fundamentales que se deben de tener en cuenta para culminar este laboratorio. 

### Actividad simpática y parasimpática del sistema nervioso autónomo y su efecto en la frecuencia cardiaca 
En un principio, es necesario catalogar al sistema nervioso el cual es el encargado de realizar la conexión entre cerebro y cuerpo con dos subdivisiones, sistema nervioso central (SNC) y el periférico (SNP). Dentro del SNP se divide de igual forma en dos categorías el somático y el periférico. Para esta ocasión nos enfocaremos específicamente en el **sistema nervioso autónomo**  el cual es el encargado de controlar la *actividades inconscientes* es decir a la activador del músculo liso, cardiaco. Este cuenta con dos divisiones, **el sistema nervioso parasimpático** y **el sistema nervioso simpático**. El **Sistema nervoso parasimpatico** está relacionado con el reposo y el descanso, es decir con todas aquellas actividades cotidianas, por esta razón el efecto que tiene en la frecuencia cardiaca radica en que está la *retarda* así como también disminuye la presión arterial, además estimula el tubo digestivo con el fin de procesar los alimentos y eliminar los residuos [1]. Mientras que el **Sistema nervioso simpatico** Este por orto lado es de gran importancia para la preparación del cuerpo durante situaciones de emergencia “lucha o huida”, esto es gracias a la activación de diversas y complejas vías nerviosas provocando el aumento del ritmo cardiaco y respiratorio junto con el aumento de la presión sanguínea dilatación de pupilas vasoconstricción todo con el fin de dar la máxima capacidad al cuerpo para huir o reaccionar, mientras que ralentiza a procesos como digestión y micción (vaciamiento de vejiga) ya que no son relevantes para una situación de emergencia [2].   


### Variabilidad de la frecuencia cardiaca (HRV) medida como fluctuaciones en el intervalo R-R, y las frecuencias de interés en este análisis: 

**El HRV** representa el estado del sistema nervioso autónomo e interactúa con el sistema cardiovascular, la variabilidad cardiaca es aquella variación entre los intervalos de tiempo entre cada latido o también visto como el tiempo transcurrido entre cada intervalo R-R . Por tanto el HRV es el cambio en el tiempo que transcurre entre cada latido, este representa al sistema nervioso autónomo encargado de regular las funciones corporales involuntarias como la frecuencia cardiaca, la respiración, digestión y la temperatura corporal. Finalmente mediante los cambios del HRV se puede identificar las activaciones del sistema simpático en caso de aumento de la frecuencia cardiaca de forma elevada o parasimpático en los momentos de disminución de la frecuencia cardiaca en relajación.Es importante conoces que los vales de HRV son únicos para cada persona ya que hay diferentes factores que lo definen como las condiciones ambientales (altitud, temperatura humedad), el estilo de vida (saludable o sedentario), niveles de estrés diarios, estado de salud entre otros, aunque según estudios realizados se muestra que las mujeres tienden a presentar niveles de HRV  más elevados que los hombres en algunas situaciones. Con esto en mente el tiempo entre intervalos también es utilizado en el estudio y diagnóstico de enfermedades cardiovasculares. El analisis del HRV se divide dentro de diferentes banda de frecuencias que son:

** 1) Frecuencia muy baja (VLF):** desde los 0.003-0.04 Hz se ve influenciada por la regulación térmica, proporciona información sobre procesos de regulación a largo plazo.

** 2)  Frecuencia baja (LF):** 0.04-0.15Hz relaciona la actividad del sistema nervioso simpático y parasimpático junto con el control de la presión arterial.

**3) Frecuencias altas (HF):** 0.15-0.4 Hz  representa únicamente la actividad del sistema parasimpático siendo sensible a los cambios dentro del sistema respiratorio, ligando el ritmo respiratorio y la capacidad de relajación.[3]  

### Transformada Wavelet: definición, usos y tipos de wavelet utilizadas en señales biológicas. 
#### Definición
La transformada wavelet se puede considerar como una extensión del análisis de Fourier, en donde es una herramienta matemática para el análisis local de señales no estacionarias y de rápida transitoriedad la cual permite descomponer a una señal, a diferencia de Fourier, esta la puede descomponer en componentes de tiempo y frecuencia, de este modo es posible analizar la variabilidad de la frecuencia a lo largo del tiempo en una señal, permitiendo saber el donde y cuando ocurren algunas frecuencias que se encuentran dentro de la señal. Por lo tanto, esta transformada descompone una señal en una señal madre llamada Wavelet la cual es una versión desplazada y con un tiempo de duración establecido sin necesidad de tener que limitarse únicamente con las funciones armónicas.

Este análisis de la señal mediante la transformada wavelet es posible mediante una escala y desplazamiento que se le aplique a la señal, lo cual varía de acuerdo a la aplicación que se le desee dar. Ya que una escala baja implica ver más detalle, es decir frecuencias altas en donde se encuentran eventos rápidos y pequeños, mientras que una escala alta se analizan los eventos con frecuencias bajas, es decir para eventos lentos [5]. La transformada wavelet para señales continuas se puede expresar mediante la siguiente ecuación:

[![Captura-de-pantalla-2024-10-27-a-la-s-9-27-34-p-m.png](https://i.postimg.cc/Gm1CgpRV/Captura-de-pantalla-2024-10-27-a-la-s-9-27-34-p-m.png)](https://postimg.cc/qzQSz4zx)

A partir de esta ecuación donde se tiene en cuenta a la señal original comparado con la escala de una versión de la wavelet madre, se obtienen coeficientes los cuales son función de la escala y posición de la wavelet madre. Para obtener la extraccion de caracteristicas, internamente lo que se se llama como bancos de filtros, en donde se le aplican dos filtros a la señal original, uno pasa alto y otro pasa bajo a partir de los cuales se obtienen los coeficientes de salida y se producen nuevas señales (sub bandas). Los coeficientes obtenidos de los pasa altos son denotados con D y representan a los coeficientes de detalle, mientras que los obtenidos por ellos pasa bajos se denota con C y representan a los coeficientes de escala. Mediante estos coeficientes es que se puede obtener la descripción de la señal obtenida mediante esta transformada.

[![Captura-de-pantalla-2024-10-27-a-la-s-10-33-34-p-m.png](https://i.postimg.cc/vZMmgh44/Captura-de-pantalla-2024-10-27-a-la-s-10-33-34-p-m.png)](https://postimg.cc/SJT4HW74) [4]

#### Tipos


**- Morlet:** Este tipo de transformada es usada en el análisis de patrones variantes en la frecuencia y el tiempo, esto gracias a que combina una función sinusoidal con una función gaussiana siendo esencial en el análisis de patrones en frecuencias específicas de señales bioeléctricas.

**- Daubechies:** Es una de las mas utilizadas en el analisis de señales biológicas gracias a la buena resolución que ofrece dentro de la frecuencia y el tiempo estas son principalmente usadas para la descomposición de señales no estacionarias (señales con componentes de frecuencia variables en el tiempo) como lo son la señales cardiacas siendo efectivas a la hora de caracterizar los complejos QRS en el electrocardiograma.
 
**- Coiflets:** Estas ofrecen una buena simetría (asegura la forma de la señal) evitando el desplazamiento de los componentes importantes como los picos o transiciones durante el proceso de descomposición de la señal este tipo de transformada es esencial en el estudio de la forma de las distintas ondas que conforman la señal las cuales brindan información diagnóstica.

**- Biorthogonal:** Usada para la descomposición y construcción de la información sin pérdida de datos este tipo de transformada es muy útil ´para el análisis de imágenes diagnósticas 

**- Mexican hat:** Útil para detección de picos abruptos ya que tiende a la segunda derivada gaussiana, con el fin de detectar transiciones o cambios rápidos en la señal com lo son los potenciales evocados (respuestas eléctricas del sistema nervioso)

**- Symlets:** Es un tipo de versión simétrica de la transformada de daubechies que es usada cuando se requiere una transformada con una misma distorsión de fase (mejor alineación temporal) sin presentar adelantos o retrasos de la señal durante la descomposición o construcción de la señal


#### Aplicaciones
Teniendo en cuenta su definición, se puede concluir que la transformada wavelet puede ser de gran uso para todo aquello que involucre procesamiento de señales gracias a la gran cantidad de información que esta nos brinda de la frecuencia en torno al tiempo. Dentro de las aplicaciones de señales biológicas, alguna de ellas y la utilidad de esta transformada son:

##### - Análisis de señales de imagen
Específicamente para las IRM (Imágenes por resonancia magnética) y tomografía, se utiliza esta transformada para mejorar la calidad de la imagen y también como apoyo para la detección de características especiales dentro de la imagen [6].  

##### - Análisis de sonidos biológicos 
Esta transformada se puede aplicar al momento de realizar un análisis de un sonido biológico así como lo es la respiración con un estetoscopio digital, con el fin de detectar patrones anormales en la respiración [7]. 

##### - EMG (electromigrafía)
Mediante el análisis de la señal emg usando el transformada wavelet es posible identificar patrones de la actividad muscular en algunas tareas o movimientos específicos, siendo de gran ayuda en el área de rehabilitación [8].

##### - ECG (electrocardiografía)
Así como con la señal EMG, con la señal ECG se puede usar la transformada wavelet para detectar anomalías de la frecuencia cardiaca, así como pueden ser posibles arritmias mediante sus coeficientes o simplemente calcular la frecuencia cardiaca mediante el análisis del complejo QRS (picos) [9].

##### - EEG (electroencefalografía)
Dentro del procesamiento de señal de esta prueba se utiliza esta transformada con el fin de identificar los diferentes ritmos cerebrales que tiene el cerebro de acuerdo a sus frecuencias ya que cada una corresponde a diferentes estados mentales y varían de acuerdo a la actividad, por esta razón, es posible diagnosticar una epilepsia o incluso esquizofrenia. Además gracias al uso de esta transformada, es posible detectar los estados del sueño de una persona mediante sus bandas de frecuencia (delta, theta, gamma, alpha, gamma) [10].

## Diagrama de flujo

De acuerdo a lo investigado, y lo postulado en la guía del laboratorio se plantea el siguiente diagrama de flujo el cual contiene la información y pasos a seguir de forma general para este cuarto laboratorio de la asignatura “Procesamiento digital de señales”.

[![Captura-de-pantalla-2024-10-27-a-la-s-11-56-22-p-m.png](https://i.postimg.cc/Z5FCVgGP/Captura-de-pantalla-2024-10-27-a-la-s-11-56-22-p-m.png)](https://postimg.cc/jD2xj8dC)


## Código 

Para la realización del proyecto se cuentan con dos códigos uno correspondiente al sistema de adquisición en donde se tomarán las señales de dos personas de la cuales una será estimulada para un ritmo cardíaco acelerado y la otra recibirá estímulos para un ritmo cardíaco más lento en estado de relajación, se guardaran en y un archivo de texto el cual será procesado mediante el segundo código con el cual se trabajara la señal aplicando cada uno de los procesos correspondientes para el laboratorio. El archivo correspondiente al sistema de adquisición de datos se llama *ecg.py*, mediante este es posible conectar la tarjeta arduino MEGA configurada para obtener los datos de forma serial, conectado a la siguiente interfaz. Para mayor claridad, este sistema de adquisición fue presentado y explicado con mayor profundidad en el LABORATORIO 3 que se encuentra en este mismo perfil.

[![interfaz-captura-de-senal.png](https://i.postimg.cc/kXtPr77S/interfaz-captura-de-senal.png)](https://postimg.cc/bs8BkcDY)


Una vez desconectado, los datos serán guardados en un archivo de texto, el cual será usado en el segundo código llamado *ecg_lab4_spyder* el cual hace uso de las siguientes librerías:  

[![lib.png](https://i.postimg.cc/7LBqHXdJ/lib.png)](https://postimg.cc/FfJMGb9h)

Estas se usan para graficar la señal, operaciones numéricas, aplicación de filtros y finalmente la transformada wavelet . 


###Diseño del filtro
Seguido a esto se inicia con el diseño del filtro que se le aplicará a la señal:

[![diseno.png](https://i.postimg.cc/T3fxnZXW/diseno.png)](https://postimg.cc/1fCbQ7X9)

Con esto en mente, se diseña un filtro Butterworth pasa banda el para el filtrado de la señal del ECG  el cual realiza una transición suave entre la banda de paso y la banda de atenuación para evitar posibles distorsiones de la señal. Para el diseño de este filtro se deben tener en cuenta las frecuencia de corte omega up y omega low que corresponden a 5 y 50 Hz, sin embargo se deben definir dos frecuencias una anterior a la frecuencia de corte menor y una mayor a la frecuencia de corte mayor correspondientes a 1 y 100 Hz que se relacionarán a dos constantes A y B de la magnitud de las frecuencias del filtro. 

Para esto se implementó el diseño de un filtro pasa bajos para luego ser transformado en filtro pasa banda haciendo uso de la fórmula:

[![f1.png](https://i.postimg.cc/qvJfNy8s/f1.png)](https://postimg.cc/nCPS5sSr)

Donde la variable **s** representa la frecuencia en el dominio de laplace, y el ancho de banda está definido por ** Omega u   -  Omega l**  , con esto en mente se debe realizar el correspondiente reemplazo de la  variable **s** , esto gracia a que existe una  relación entre la variable **s** con la función de transferencia  la cual describe el comportamiento del sistema en el dominio de una frecuencia compleja:

[![s.png](https://i.postimg.cc/T1MFfDdW/s.png)](https://postimg.cc/DJ6Bcmb2)

Con esta equivalencia se procede a realizar la correspondiente sustitución, para esto es de gran importancia tener en cuenta que al utilizar un filtro pasa bajos se presenta una frecuencia de corte **Omega r** que definirá las dos constantes para la transformación del pasa bajos al pasabanda dado como resultado:

[![jo.png](https://i.postimg.cc/QC34RZmQ/jo.png)](https://postimg.cc/cgFBnjVC)

Con esta opresión se logra que todo quede igualado a **Omega r**  la cual se representa como la frecuencia crítica del filtro pasa bajos, este mismos proceso se repite con **Omega 2** , cada una de estas ecuaciones se igualada alas constantes A y B que corresponden al valor de **Omega r**, eligiendo finalmente el valor más restrictivo para el filtro que significa el de menor valor positivo, para este caso el valor de A al ser negativo no se utiliza dejando solo al valor de B. Conte valor se pasa a evaluar las dos ecuaciones de la potencia de energía de la cual se obtendrá el orden del filtro.

[![n.png](https://i.postimg.cc/y6yvk5nG/n.png)](https://postimg.cc/fkkxP8G7)

Dando como resultado un filtro pasa banda de orden 3.

	def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

	def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data) 
    return y

### Procesamiento de la señal

Teniendo en cuenta lo anterior se procede con la función del filtro pasabanda en donde se definirán los coeficientes del filtro y las respectivas frecuencias de corte y de muestreo haciendo uso de Nyquist. Seguido a esto se utiliza la función del filtro pasabanda el cual llevará la señal que se desea filtrar y aplicará los parámetros definidos anteriormente para el correcto filtrado de la señal.

 def mostrar_parte_senal(tiempo, datos, datos_filtrados, fs):
    
    # Rango de tiempo  ventana rectangular
    start_time = 137.0  # tiempo inicial 
    end_time = 140.0   # tiempo final 
    
    start_index = int(start_time * fs)
    end_index = int(end_time * fs)


    plt.figure(1)
    plt.plot(tiempo[start_index:end_index], datos[start_index:end_index], label='Señal EMG Original')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('mV')
    plt.title('Parte de señal ECG Original (sujeto 1)')
    plt.grid()

    plt.figure(2)
    plt.plot(tiempo[start_index:end_index], datos_filtrados[start_index:end_index], label='Señal EMG Filtrada', color='orange')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('mV' )
    plt.title('Parte de señal ECG Filtrada (sujeto 1)')
    plt.grid()
    plt.tight_layout()
    plt.show()

Una vez definido y aplicado el filtro se requiere visualizar la señal que se está filtrando junto con la señal original obtenida mediante el sistema de adquisición. Mediante la función ** mostrar parte de la señal** Se busca llegar a la gráfica de la señal original y la señal filtrada mostrando solamente una parte específica con el fin de facilitar la manipulación y análisis de la señal, se realizó mediante la implementación de una ventana rectangular. Para esto se utilizó un arreglo que contiene los valores de tiempo de cada muestra de la señal, siendo necesario ya que  el archivo de la señal contiene 300 segundos (5 minutos) de grabación.

Se inicia con la lectura de la señal original, la señal filtrada y la frecuencia de muestreo, se define el intervalo de tiempo que se debe analizar teniendo en cuenta que debe ser suficiente para el análisis de la señal para este caso se escogió el intervalo entre los 139 - 140 segundos.  Después de definir estos parámetros se procede con la creación de las dos gráficas señal original y señal filtrada. Con el objetivo principal de lograr una comparación más adelante de los resultados, se le realizó esta prueba a dos sujetos que estuvieron de acuerdo con procedimiento que se requería llevar a cabo con los electrodos y adquisición de señal.

**SUJETO 1**

*Señal cruda de sujeto 1:*: Para la primer evaluación de la muestra se metió al sujeto 1 a estímulos de relajación.

[![cruda1.png](https://i.postimg.cc/4d5VxCZb/cruda1.png)](https://postimg.cc/Q9FHfyFH)


**Señal filtrada sujeto 1:**

[![filt1.png](https://i.postimg.cc/PrNYTF7Y/filt1.png)](https://postimg.cc/dLPL9nwV)

**SUJETO 2**
*Señal cruda de sujeto 2:* El sujeto 2 fue sometido a estímulos que aumentaron el ritmo cardiaco.

[![cruda2.png](https://i.postimg.cc/wTtySRtk/cruda2.png)](https://postimg.cc/Tp63bwJy)

*Señal filtrada sujeto 2:*

[![filt2.png](https://i.postimg.cc/J0Sn1Ky5/filt2.png)](https://postimg.cc/64Lwcrf8)

 Al realizar el análisis de cada uno de los sujetos evaluados se denota que la cantidad de latidos dentro del intervalo de tiempo seleccionado presenta cambios significativos del sujeto 1 en estado de relajación al sujeto 2, esta diferencia también se podría observar en el análisis del intervalos R-R  de una forma más clara.  

### Intervalo R-R

	def contar_picos_r(datos_filtrados, fs):
    # Umbral mínimo para picos 
    altura_minima = 350  
    picos, _ = find_peaks(datos_filtrados, height=altura_minima, distance=fs/2.5)
    return len(picos), picos 

	def calcular_intervalo_rr(indices_picos, fs):
    # Calcular las diferencias entre índices de picos consecutivos
    intervalos_rr = np.diff(indices_picos) / fs  # Dividir por fs para obtener segundos
    return intervalos_rr

Para esto se inicia con la identificación de cada uno de los picos del  complejo QRS que representan cada latido, se llama a la señal filtrada junto con su frecuencia de muestreo, se define una altura de 350 lo que significa que si un pico  alcanza los 350 de altura es considerado como un pico R y se establece que solo estos van a ser considerados para el análisis, a su vez se define una distancia fs/2.5 la cual asegura que los picos no estes sobrepuesto evitando el conteo falso de picos.

Después de definir cada una de las características que deben tener los picos se procede con el cálculo R-R haciendo uso de la función **calcular intervalo R-R**, contiene los intervalos consecutivos mediante el cálculo de la diferencia de los índices de los picos para luego dividirse por la fs definida para convertir esa diferencia en segundos dando como resultado.

	def calcular_parametros_HRV(intervalos_rr):
	    media_rr = np.mean(intervalos_rr)
  	  desviacion_rr = np.std(intervalos_rr)
	    return media_rr, desviacion_rr

**Sujeto 1**

Media de intervalos R-R: 0.6922 segundos
Desviación estándar de intervalos R-R: 0.0424 segundos


**Sujeto 2**

Media de intervalos R-R: 0.6234 segundos
Desviación estándar de intervalos R-R: 0.0547 segundos


Con esto datos se puede denotar la diferencia entre el sujeto 1 y el sujeto 2 ya que como se explica anteriormente el sujeto 1 presenta un R-R mayo lo cual significa que hay más tiempo entre picos R lo cual finalmente se ve como un ritmo cardíaco más lento que el del sujeto 2, además se maestra la desviación estándar con la cual se conoce que entre mayor sea esta desviación más activo estará el sistema simpático.

### Transformada wavelet

	def aplicar_transformada_wavelet(ecg_filtered, fs):
		# Definir parámetros
		dt = 1 / fs 
		t = np.arange(len(ecg_filtered)) * dt 

		scales = np.arange(1, 140) 

		coeficientes_cwt = cwt(ecg_filtered, morlet, scales)

		#espectrograma
		plt.figure(figsize=(12, 6))
		plt.imshow(np.log1p(np.abs(coeficientes_cwt)), extent=[t[0], t[-1], scales[-1], scales[0]], aspect='auto',
				   cmap='jet', interpolation='bilinear')
		plt.colorbar(label='Potencia (magnitud)')  # Cambié a log para mejorar visualización
		plt.xlabel('Tiempo (s)')
		plt.ylabel('Escalas (correspondientes a Frecuencia en Hz)')
		plt.title('Espectrograma de la señal ECG utilizando Transformada Wavelet con Morlet')
		plt.ylim(1, 10)  # Ajustar según las escalas utilizadas
		plt.show()

Teniendo en cuenta lo anterior, para el analiza la señal correctamente se requiere que esta este en función del tiempo y la frecuencia para lo cual no es posible aplicar transformada de fourier ya que solo se analizaría la frecuencia y no el tiempo. Por esta razón se opta por la transformada wavelet de morlet continua ya que esta es la que más se adapta la señal de ECG. Para esto se inicia llamando a la señal filtrada con su frecuencia de muestreo para iniciar con la definición del intervalo de muestreo o tiempo de muestreo que es igual a 1/fs, se crea un arreglo **t** que representa el tiempo en segundos para cada muestra de la señal multiplicada por el tiempo de muestreo. Después se ajustan las escalas de frecuencia que son los rangos de valores que en este caso es de 1 a 40, se define el tipo de transformada a utilizar en este caso la de morlet. Se da inicio con el espectrograma se usó de plt.imshow para mostrar el espectrograma de los coeficientes tomando el valor absoluto de los coeficientes para obtener la magnitud para después aplicar el logaritmo natural de 1 más su valor correspondiente esto debido a que realiza una mejor distribución en torno a la señal obtenida, y así también se puede observar mejor los cambios que tiene la amplitud de los picos resultantes para así hacer la comparación con los cambios de colores el valor de la potencia.

*Espectrograma sujeto 1:*

[![esp1.png](https://i.postimg.cc/cJ6L8VQB/esp1.png)](https://postimg.cc/B890r77j)

*Espectrograma sujeto 2:*

[![esp2.png](https://i.postimg.cc/QCg83s3h/esp2.png)](https://postimg.cc/9wM5d60n)

#### Variación de frecuencias 

Como se ha venido mencionando, gracias a la transformada wavelet fue posible obtener un espectrograma de la señal adquirida ECG en donde fue posible comparar a la frecuencia de la señal durante el tiempo de su adquisición. Mediante estas gráficas obtenidas para ambos sujetos fue posible observar cómo las frecuencias que fueron obtenidas a lo largo de la adquisición oscilaban entre 1 a 5 Hz lo cual indica una aproximación cercana a los que se hace referencia de la frecuencia cardiaca normal de un adulto con corazón sano que es entre 60 a 100 LPM. Debido a que no hubo un mayor estímulo externo que impactará significativamente  los resultados, es posible decir que no hubo una variación importante durante las frecuencias con respecto al tiempo en el que duró la adquisición.

### Análisis de banda de frecuencia baja y alta

**Banda de baja frecuencia**: va de 0.04 a 0.15 Hz y refleja mayormente la actividad simpática del sistema nervioso autónomo

**Banda de alta frecuencia**: va de 0.15 a 0.4 Hz, y refleja la actividad parasimpática del sistema nervioso autónomo.

*Sujeto 1:*

[![pot1.png](https://i.postimg.cc/fLcn3Kgv/pot1.png)](https://postimg.cc/HckPRQmJ)

Promedio de potencia en banda LF: 29.403017910210608
Promedio de potencia en banda HF: 42.11858374127289

Mediante esta gráfica es posible evidenciar que durante la adquisición de la señal de electrocardiografía, el sujeto 1 refleja mayormente la actividad parasimpática del sistema nervioso autónomo, lo que según el inicio del informe indica que estuvo en un estado de relajación y calma durante la adquisición de datos.

*Sujeto 2:*

[![pot2.png](https://i.postimg.cc/KzZQND8f/pot2.png)](https://postimg.cc/xk4KjHHN)

Promedio de potencia en banda LF: 28.13682412070105
Promedio de potencia en banda HF: 33.74928082683117

Mediante el promedio de las bandas que se obtuvo con respecto al sujeto 2, hay una clara evidencia en que el promedio de la banda de alta frecuencia fue mayor que el de la baja frecuencia indicando una presencia dominante de una actividad parasimpática, por lo que se encontraba en un estado de relajación y de calama durante esta adquisición.


### Comparación entre los resultados obtenidos de las bandas de frecuencias

Al observar no solo las gráficas sino que también interpretar los valores promedios de las potencias entre los dos sujetos, se denota que hay un cambio significativo que indica que el sujeto 1 presentaba una mayor actividad parasimpática en comparación con el sujeto 2. Esto es posible decirlo debido a que existe una mayor aproximación al balance de las dos actividades nerviosas en el sujeto 2 que en el primero.

También, individualmente es posible observar que hay de los dos tipos de actividades nerviosas presentes en la señal procesada, sin embargo una siempre se muestra más dominante que la otra, y eso se evidencia en ambos casos de los sujetos. En estas gráficas postuladas, también fue posible evidenciar la forma en la que la potencia que indica la actividad de este sistema evaluado fue variando durante el tiempo de adquisición de datos, lo que indica que no siempre fue constante un estado de actividad parasimpática durante los cinco minutos de toma de datos, sino que mediante varios estímulos externos se lograba disminuir esta actividad y a su vez la de la actividad simpática.


## Conclusión

Mediante el procesamiento de esta señal fisiológica correspondiente al ECG, fue posible observar y denotar las diferencias significativas que tiene analizar una señal únicamente con respecto al dominio del tiempo en comparación con la frecuencia con respecto al tiempo de adquisición de la señal mediante la transformada wavelet. Realmente en el espectrograma que se obtuvo a partir de esta, como se mencionó anteriormente no se evidenció una mayor distribución de sus frecuencias con respecto al tiempo debido a que el estado de relajación de los sujetos no fue estimulado de forma significativa como para mostrar una mayor distribución en las frecuencias que se muestran en esta gráfica.

Finalmente, los valores obtenidos durante todo el laboratorio se puede correlacionar desde los datos como la desviación estándar calculada al inicio con el HRV en el dominio del tiempo junto con el análisis de las bandas de frecuencias con el fin de justificar la actividad parasimpática en la que se encontraban los sujetos. Entre más alto fuera el valor de la desviación estándar obtenido a partir de los intervalos R-R de la señal en el dominio del tiempo indicaba una mayor actividad del sistema simpático, por lo que inversamente un valor menor de este indicaría una mayor actividad del sistema parasimpático, en el caso de ambos sujetos se evidencia una desviación estándar reducida entre 0.04 y 0.05 segundos, indicando una mayor actividad parasimpática. Esto como ya se mencionó es sustentado mediante la dominancia de la banda con frecuencia alta en su análisis. Adicionalmente, teniendo en cuenta que durante este laboratorio se estuvo haciendo la comparación entre dos sujetos constantemente, es posible evidenciar que el sujeto 2 obtuvo una mayor actividad simpática que el sujeto 1 no solo mediante el análisis de bandas de frecuencia sino que también gracias a la diferencia de su desviación estándar, ya que el sujeto dos cuenta con 0.05 segundos mientras que el sujeto 1 con 0.04 segundos, indicando y confirmando que el sujeto 2 presenta una mayor actividad simpática con respecto al sujeto 1.



## BIBLIOGRAFIA
[1] Coon E. (2023) *Introducción al Sistema Nervioso Autonomo* Mayo Clinic. https://www.msdmanuals.com/es/hogar/enfermedades-cerebrales-medulares-y-nerviosas/trastornos-del-sistema-nervioso-autónomo/introducción-al-sistema-nervioso-autónomo

[2] Sistema nervioso simpático. (2023, October 30). Kenhub. https://www.kenhub.com/es/library/anatomia-es/sistema-nervioso-simpatico 

[3] Veloza, L., Jiménez, C., Quiñones, D., Polanía, F., Pachón-Valero, L. C., & Rodríguez-Triviño, C. Y. (2019). Variabilidad de la frecuencia cardiaca como factor predictor de las enfermedades cardiovasculares. Revista Colombiana De Cardiología, 26(4), 205–210. https://doi.org/10.1016/j.rccar.2019.01.006 

[4] UNAM. (2018). *Transformada Wavelet*. UNAM. https://virtual.cuautitlan.unam.mx/intar/?page_id=1108#:~:text=Existen%20distintos%20tipos%20de%20transformada,y%20la%20transformada%20wavelet%20packet.

[5] Universidad Tecnologica de Pereira. (2007). *Del analisis de fourier a las wavelets - Transfromada continua wavelet (CWT)*  Universidad Tecnologica de Pereira. https://revistas.utp.edu.co/index.php/revistaciencia/article/view/4017/2273

[6] Abdulazeez A, Zeebaree Q & Abdulwader D. (2020). *Wavelet applications in medical images: a review*. TEST: Engineering & management. https://www.researchgate.net/publication/341977072_Wavelet_Applications_in_Medical_Images_A_Review

[7] Pouyani M F, Vali M, Ghasemi M A. (2022) *Lung sound signal denoising using discrete wavelet transform and artificial neural network*, Volume 72, Part B, ISSN 1746-8094,
https://www.sciencedirect.com/science/article/pii/S1746809421009265

[8] Gulshan, Thukral R, Singh M. (2015). *Analysis of EMG signals based on wavelet transform - a review*. Sant Longowal Institute of Engineering and Technology. https://www.researchgate.net/publication/331099870_Analysis_of_EMG_Signals_Based_on_Wavelet_Transform-A_Review

[9] Paul S Addison. (2005) *Wavelet transforms and the ECG: a review*. Institute od Physics Publishing. https://www.researchgate.net/publication/7672339_Wavelet_transforms_and_the_ECG_A_review

[10] Gosala B, Kapgate P D, Jain P, Chaurasia R N, Gupta M. (2023).*Wavelet transforms for feature engineering in EEG data processing: An application on Schizophrenia*,
Volume 85, ISSN 1746-8094, https://www.sciencedirect.com/science/article/pii/S1746809423002446



