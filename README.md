# ***SCAV: P3-Python & Video***

## **EJERCICIOS**

**IMPORTANTE: cuando ejecutamos los fichero python, dado que se pide al ususario cierta interacción, una vez puesto en ejecución el script, debemos presionar F5 para poder ver la pantalla emergente (cmd) donde poder introducir la información y trabajar con el script.**

### EJERCICIO-1
#### ***Create a new BBB container***

<p align="justify">En este ejercicio se nos pedía crear un container con las siguientes componentes: </p>


* 
    * Un corte de 1 minuto del video BBB, sin audio.
    * Un audio mono de 1 minuto del video BBB (mismo fragmento que en el anterior paso).
    * Un audio de 1 minuto del video BBB, pero al que le reducimos el bitrate (mismo fragmento que en los anteriores pasos).
    * Subtítulos de ese minuto recortado del video BBB. 
* 


##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-1/result_ej_1.png" width="600"/>
</p>

<p align="justify">Como podemos ver en la captura, se nos muestra el tipo de codec del video: h.264, el codec del audio: AAC, la duración: 10.6s, y el bitRate: 6737785 bps. </p>

### EJERCICIO-2
#### ***Python: Automatize the creation of MP4 container***

<p align="justify">Para este ejercicio reciclé código del <em>Seminario 2</em>:</p><p align="center"><em>ffmpeg -i {name_video}.mp4 -vf scale={scaleValue[i]} {nameVideo[i]}.mp4 </em></p><p align="justify">Donde <em>name_video</em> hace referencia al nombre del video con el que quiere trabajar el usuario y <em>nameVideo[i]</em> representa la array contenedora de todos los nombres dados por el usuario para cada uno de los videos con distinta resolución.</p><p align="justify">Fuente: <em>Seminario 2</em></p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-2/result_ej_2.png" width="600"/>
</p>

<p align="justify">Como podemos ver en la captura se nos guardan cada uno de los videos reducidos en calidad con su respectivo nombre según haya sido asignado por el usuario. </p>

### EJERCICIO-3
#### ***Python: Which broadcasting standard would fit***

<p align="justify">Igual que en la práctica 1 y el seminario 2 escalando el input (video o imagen) podemos cambiar la resolución de éstos. Por ello, con el siguiente comando podemos redimensionar cualquier archivo de entrada: </p><p align="center"><em>ffmpeg -i {in_file} -vf <strong>scale={width}:{height}</strong> {width}x{height}-{in_file}</em></p><p align="justify">Observamos que <em>in_file</em> hace referencia al archivo de entrada del usuario y, <em>width y height</em> son la nueva resolución del archivo <em>WIDTHxHEIGHT</em>. </p><p align="justify">Fuente: <em>Práctica 1 y Seminario 2</em></p>

##### **Resultados**

###### **IMAGEN**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-3/result_img_ej_3.png" width="600"/>
</p>

###### **VIDEO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-3/result_video_ej_3.png" width="600"/>
</p>




<p align="justify">Como podemos ver en ambas captura, según los datos dados por el usuario, obtenemos la salida reescalada correspondiente.</p>

### EJERCICIO-4
#### ***Python: Generate container to launch against exercise 3***

<p align="justify">Con el fin de dar la posibilidad de cambiar el tipo de codec del archivo del usuario, daremos la posibilidad de que éste introduzca un video con audio, un audio o un video sin audio. A partir de aquí, crearemos condicionales según el tipo de archivo introducido. Con el fin de poder saber que tipo de archivo ha sido introducido, usaremos una función de <em>subprocess</em> llamada <em>check_output</em>, que nos devuelve la salida del comando realizado. Por esta razón ejecutaremos el comando:<br><em>ffprobe -v error -show_entries stream=codec_type -of default=noprint_wrappers=1 {in_file}</em><br> y de esta forma saber de que tipo de codec se trata. Si la salida de este archivo es que tenemos un codec de tipo audio solo, el archivo es un audio, si se trata de video solo, se tratará de un video sin audio, pero si nos devuelve dos tipos de codec, audio y video, significará que se nos pasó un video con canal de audio también.<br>A partir de aquí ya sabemos con que tipo de archivo nos encontramos, por lo tanto, podemos empezar a mostrar las opciones para cada caso:</p>

<p align="justify">&nbsp;- Video (video y audio): en este caso daremos la posibilidad de cambiar el codec del video únicamente, el audio o de ambos.<br>&nbsp;&nbsp;&nbsp;·Codec video: Damos la opción de cambiar entre MPEG-1, MPEG-2, MPEG4 y h.264. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>new_codec</strong> MPEG1_{in_file}</p>

<p align="justify">&nbsp;&nbsp;&nbsp;·Codec audio:  Damos la opción de cambiar entre MP3 y AAC. Realicaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -acodec <strong>new_codec</strong> -vcodec copy MP3_{in_file}</p>

<p align="justify">&nbsp;&nbsp;&nbsp;·Codec video y audio:  Damos la opción de cambiar entre todas las posibilidades anteriores. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>video_codec</strong> -c:a <strong>audio_codec</strong> MPEG1_MP3_{in_file}</p>

<p align="justify">&nbsp;- Audio: en este caso daremos la posibilidad de cambiar el codec del audio únicamente. <br>&nbsp;&nbsp;&nbsp;·Codec audio: Damos la opción de cambiar entre MP3 y AAC. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:a <strong>new_codec</strong> output.mp3</p>

<p align="justify">&nbsp;- Video sin audio: en este caso daremos la posibilidad de cambiar el codec del video únicamente. <br>&nbsp;&nbsp;&nbsp;·Codec video: Damos la opción de cambiar entre MPEG-1, MPEG-2, MPEG4 y h.264. Realizaremos el cambio con el comando:</p><p align="center">ffmpeg -i {in_file} -c:v <strong>new_codec</strong> MPEG1_{in_file}</p>


##### **Resultados**

###### **VIDEO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_video_ej_4.png" width="900"/>
</p>

###### **AUDIO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_audio_ej_4.png" width="400"/>
</p>

###### **VIDEO SIN AUDIO**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P2-SCAV/blob/main/EJERCICIO-4/result_videosinAudio_ej_4.png" width="500"/>
</p>

<p align="justify">Como podemos ver en las capturas, el archivo final corresponde con la solicitud de cambio de codec por parte del usuario. </p>


### EJERCICIO-5
#### ***Python: Integrate everything inside a class***

<p align="justify">Con la finalidad de integrar todos los ejercicios anteriores realizamos lo siguiente:</p>
<p align="justify">Haremos un menú. En éste le pedimos que el usuario nos de una archivo con el que trabajar. Comprobamos si se trata de un video con audio o sin, una imagen o un audio. A partir de aquí le mostramos por pantalla la información que consideramos importante según el archivo: Audio (codec), Video con audio (codecs y resolución), Video sin audio (codec y resolución) e imagen (resolución).<br>Hecho esto le preguntamos al usuario que quiere realizar según el archivo dado. En el caso de ser un video, podemos modificar su/s codec/s o cambiar la resolucón, en el audio cambiar únicamente el codec o en el caso de la imagen cambiar la resolución. A partir de aquí integramos los comandos anteriormente mencionados según las opciones escogidas por el usuario.<br>Cabe decir que todo esto se integra dentro de un bucle de tipo <em>while</em> donde el usuario pude escoger salir del menú o contiunar pasando archivos y modificándolos.<br><br>Dentro de la carpeta <em>EJERCICIO-5</em> he añadido el video BBB.mp4 que hace referencia al video original de 10 segundos, el video bbb.mp4 que representa el video sin audio, una imagen img.jpg con la que también poder probar el código, y un audio audio.wav con el que poder trabajar. </p>

##### **Script en EJERCICIO-5 COMO ej_5.py**


