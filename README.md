# LABORATORIO 4 

Mediante el siguiente laboratorio se busca adquirir una señal ECG


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



