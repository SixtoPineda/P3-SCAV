# ***SCAV: P3-Streaming and final exercises***

## **EJERCICIOS**

**IMPORTANTE: cuando ejecutamos los fichero python, dado que se pide al ususario cierta interacción, una vez puesto en ejecución el script, debemos presionar F5 para poder ver la pantalla emergente (cmd) donde poder introducir la información y trabajar con el script.**

### EJERCICIO-1
#### ***Python: BBB video converted***

<p align="justify">En este ejercicio se nos pedía crear 4 videos con las siguientes características: </p>

* Video 1: Codec: vp8 y resolución: 1280x720
* Video 2: Codec: vp9 y resolución: 640x480
* Video 3: Codec: h.265 y resolución: 360x240
* Video 4: Codec: AV1 y resolución: 160x120

<p align="center">(Para realizar cada uno de estos pasos, reutilicé código de prácticas anteriores)</p>
<p align="justify">Reutilicé el código siguiente: </p>
<p align="center">ffmpeg -i <strong>{inputVideo}</strong> -vf scale=<strong>{width:high}</strong> -c:v <strong>{CodecType}</strong> <strong>{nameVideo}</strong>.mkv</p>
<p align="justify">Donde le pedimos al usuario que nos introduzca el nombre del video con el que trabajar y realizo un bucle en python donde vamos creando cada uno de los videos mencionados anteriormente. Con este fin creé una lista con cada una de las resoluciones y sus respectivos códecs.</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/vp8.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/VP9.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/H265.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/AV1.png" width="400">
</p>


<p align="justify">Como podemos ver, cada video corresponde con su respectiva resolución como se ha mencionado anteriormente al inicio del ejercicio.</p>
<p align="justify"><em>Resultado de cada video del ejercicio en EJERCICIO-1/FOTOS</em></p>

### EJERCICIO-2
#### ***Container of the 4 videos***

<p align="justify">Con el fin de crear un container con los cuatro videos, reutilicé el código de la práctica 3 donde creábamos un container con varios audios. Por ello el comando es: </p>

<p align="center">ffmpeg -i {nameVideo[0]}.mkv -i {nameVideo[1]}.mkv -i {nameVideo[2]}.mkv -i {nameVideo[3]}.mkv -c copy -map 0 -map 1 -map 2 -map 3 4x1Container.mkv</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-2/result.png" />
</p>

<p align="justify">Como podemos ver, el container final tiene los 4 videos, y con sus respectivos audios y codecs. </p>
<p align="justify">EXPLICAICÓN DE BITRATE Y ESO</p>

### EJERCICIO-4
#### ***Python: The online streaming***

<p align="justify">En este ejercicio se nos pedía unificar dos funcionalidades: crear un container y saber que tipo de broadcasting mejor se adapta. Por lo tanto, junté ambos scripts de los dos ejercicios anteriores en uno.</p>




##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/ejemplo-1.png" width="700"/>
</p>


<p align="justify">Como podemos ver, en el primer ejemplo, dado que nos encontramos con el codec de video h.265, éste no se ajusta con ningún tipo de broadcasting, por lo tanto, se nos muestra por pantalla que ninguno se ajusta.</p>



