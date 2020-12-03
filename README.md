# ***SCAV: S3-Python & Video***

## **EJERCICIOS**

**IMPORTANTE: cuando ejecutamos los fichero python, dado que se pide al ususario cierta interacción, una vez puesto en ejecución el script, debemos presionar F5 para poder ver la pantalla emergente (cmd) donde poder introducir la información y trabajar con el script.**

### EJERCICIO-1
#### ***Create a new BBB container***

<p align="justify">En este ejercicio se nos pedía crear un container con las siguientes componentes: </p>

* Un corte de 1 minuto del video BBB, sin audio.
* Un audio mono de 1 minuto del video BBB (mismo fragmento que en el anterior paso).
* Un audio de 1 minuto del video BBB, pero al que le reducimos el bitrate (mismo fragmento que en los anteriores pasos).
* Subtítulos de ese minuto recortado del video BBB. 

<p align="center">(Para realizar cada uno de estos pasos, reutilicé código de prácticas anteriores)</p>
<p align="justify">Para el primer paso realizaremos el siguiente comando:</p>
<p align="center">ffmpeg -ss <strong>00:00:00</strong>< -i input.mp4  -c copy -t <strong>00:01:00</strong> <strong>-an</strong> output.mp4</p>
<p align="justify">como podemos ver, recortamos el primer minuto del video y con el comando -an eliminamos el audio de éste.<br>Para el segundo paso realizamos (1):</p>
<p align="center">ffmpeg -ss 00:00:00 -i input.mp4  -t 00:01:00 <strong>-ac 1</strong> monoTrack.mp3</p>
<p align="justify">nuevamente cortamos el primer minuto del video pero solo extraemos la parte de audio con -ac y con 1 obtenemos un audio de un solo canal, es decir mono. <br>A continuación ejecutaremos (2):</p>
<p align="center">ffmpeg -ss 00:00:00 -i input.mp4  <strong>-b:a 50k</strong> -t 00:01:00 lowBitrate.mp3</p>
<p align="justify">de igual forma que antes recortamos el primer minuto del video BBB, pero con <em>-b:a 50k</em> seleccionamos el bitrate del audio y se lo reducimos a 50kbps. Cabe decir que antes de realizar este paso, con el comando <em>ffmpeg -i NombreVideo </em>verifiqué que bitrate tenia el audio original para asegurarme que con 50kbps lo estaba reduciendo.<br>En el caso de los subtítulos (SUBTÍTULOS-BBB-VIDEO/sub.srt), los extraje de internet (3). Cabe decir que éstos no eran del todo precisos y los modifiqué un poco.<br>Con todos los componentes tan solo quedaba crear el container.<br>Para ello, busque los comandos que permitían añadir los subtítulos al video, pero que permitiese poder activarlos o no, puesto que hay comandos que añadían los subtítulos, pero no había forma de desactivarlos. Mediante la fuente (4) encontré el comando:</p>
<p align="center">ffmpeg -i input.mp4  -i subtitles.srt -map 0 -map 1 -c copy -c:s mov_text output.mp4</p>
<p align="justify">que nos añadía los subtítulos al video sin audio de tal forma que al ejecutar el video podíamos activar o desactivar éstos.<br>Por último busqué la forma de añadir dos tracks de audio del mismo modo que los subtítulos, mediante el menú de ejecución poder escoger entre un track u otro. Mediante la fuente (5) encontré el comando:</p>
<p align="center">ffmpeg -i input.mp4 -i audio1.mp3 -i audio2.mp3 -map 0 -map 1 -map 2 -codec copy output.mp4</p>
<p align="justify">que nos añadía ambos audios de igual forma que los subtítulos, pudiendo escoger al ejecutar el video final.</p>
<p align="left">Fuentes:<br>(1) https://superuser.com/questions/826669/ffmpeg-get-mono-wav-audio-8khz-16-bit-out-of-mp4-video <br>(2) https://stackoverflow.com/questions/42947957/how-convert-high-bitrate-mp3-to-lower-rate-using-ffmpeg-in-android <br>
(3) https://sites.google.com/site/chrisfoo/subtitles <br>
(4) https://www.enmimaquinafunciona.com/pregunta/120105/usar-ffmpeg-para-anadir-subtitulos-a-un-archivo-de-video-m4v <br>
(5) https://superuser.com/questions/508331/ffmpeg-add-two-audio-streams-to-video <br>
</p>

##### **Resultados**

<p align="justify">Para comprobar que el container se había creado correctamente, procedí a ejecutar el comando <em>ffmpeg -i VideoFinal.mp4</em> (VideoFinal = audios_subs_video.mp4) donde vi:</p>

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-1/FOTOS/resultContainer.png" width="700"/>
</p>

<p align="justify">Y como podemos ver contiene el video del fragmento de 1 minuto que recortamos en el paso 1, los dos audios, uno mono y el otro con un bajo bitrate, y los subtítulos. </p>
<p align="justify"><em>Resultado de cada Step del ejercicio en EJERCICIO-1/FOTOS</em></p>

### EJERCICIO-2
#### ***Python: Automatize the creation of MP4 container***

<p align="justify">En este apartado se nos pedía automatizar todos los pasos realizados en el ejercicio 1 en un solo script de python.<br>Para ello, decidí reutilizar código de prácticas anteriores. Creé un bucle de tipo <em>while</em> donde se le pide al usuario, tanto al iniciar la ejecución como al finalizarla, si éste quiere acabar con la ejecución o quiere seguir trabajando con el script con otro/s archivos más.<br><br>A partir de aquí, le pedimos al usuario que nos introduzca el nombre <strong>completo</strong> del video con en que realizar los pasos anteriores y crear un nuevo container. Una vez el usuario nos da el nombre de dicho archivo, procedemos a ejecutar cada uno de los comandos como he mencionad en el ejercicio 1, pero desde el fichero python con la función <em>subprocess.run</em>.<br><br>De igual forma que en anteriores prácticas, se pide al usuario que introduzca el nombre del archivo final, en este caso del container .mp4.<br>Cabe decir que al finalizar la ejecución del ejercicio borramos cada uno de los archivos generados para realizar el ejercicio y así solo dejar el resultado final en el container con extensión .mp4. </p>

##### **Pasos**

###### **1**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-2/FOTOS/1-screen.png" width="600"/>
</p>

###### **2**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-2/FOTOS/2-screen.png" width="600"/>
</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-2/FOTOS/resultados.png" width="700"/>
</p>

<p align="justify">Como podemos ver, de igual forma que en ejercicio 1, obtenemos el container final con todos los componentes, el video que previamente extraíamos sin audio, los dos tracks de audio, mono y con bajo bitrate, y los subtítulos. </p>

### EJERCICIO-3
#### ***Python: Which broadcasting standard would fit***

<p align="justify">A continuación se nos pedía que dado un video pasado a nuestro script, podamos retornar por pantalla los <em>broadcasting</em> que se adaptan a éste según los códecs de video y audio que tiene el archivo pasado.</p>
<p align="justify">Para ello, me basé en las slides T3 explicadas en clase, y partir de aquí realizar una combinación de condicionales donde según el codec de video y audio que tenga el fichero dado, podremos deducir qué <em>broadcasting</em> se adapta mejor.</p>
<p align="justify">Recordemos que:</p>

* DVB: Video (MPEG2 y h.264) y Audio (AAC, AC-3 y MP3)
* ISDB: Video (MPEG2 y h.264) y Audio (AAC)
* ATSC: Video (MPEG2 y h.264)  y Audio (AC-3)
* DTMB: Video (AVS, AVS+, MPEG2 y h.264)  y Audio (DRA, AAC, AC-3, MP2 y MP3)

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-3/FOTOS/VideoQLePasamos.png" width="600"/>
</p>

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-3/FOTOS/result-3.png" width="600"/>
</p>

<p align="justify">Como podemos ver, dado que el codec del video es h.264 y el del audio es AAC, tal y como se ve en las propiedades del video, los broadcasting que mejor se adaptan a este video son: DVB, ISDB y DTMB. </p>

### EJERCICIO-4
#### ***Python: Generate container to launch against exercise 3***

<p align="justify">En este ejercicio se nos pedía unificar dos funcionalidades: crear un container y saber que tipo de broadcasting mejor se adapta. Por lo tanto, junté ambos scripts de los dos ejercicios anteriores en uno.</p>
<p align="justify">La única diferencia respecto los códigos anteriores tiene que ver con el ejercicio 2. Dado que queremos crear un container y luego verificar que broadcasting mejor se adapta, decidí dar la opción al usuario de que pueda escoger qué codec poner al video de 1 minuto, al audio mono y al de bajo bitrate. De este modo, al pasar el container resultante de dicho proceso, podemos obtener diferentes combinaciones de broadcasting, según los códecs escogidos por el usuario.</p>
<p align="justify"></p>

##### **Video que le pasamos al Script**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/VideoQLePasamos.png" width="600"/>
</p>

##### **Resultados: Ejemplo-1**

###### **Input**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/ejemplo-1.png" width="700"/>
</p>

###### **Output**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/resultEjemplo-1.png" width="700"/>
</p>

<p align="justify">Como podemos ver, en el primer ejemplo, dado que nos encontramos con el codec de video h.265, éste no se ajusta con ningún tipo de broadcasting, por lo tanto, se nos muestra por pantalla que ninguno se ajusta.</p>

##### **Resultados: Ejemplo-2**

###### **Input**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/ejemplo-2.png" width="700"/>
</p>

###### **Output**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-4/FOTOS/resultEjemplo-2.png" width="700"/>
</p>

<p align="justify">En cambio para el segundo ejemplo, la combinación de codecs entre MPEG2 y AAC, y MPEG2 y AC-3, nos da lugar a que los broadcasting que se adaptan son: ISDB, DVB y DTMB para la primera combinación y ATSC, DVB y DTMB para la segunda. </p>


### EJERCICIO-5
#### ***Python: Integrate everything inside a class***



##### **Script en EJERCICIO-5 como ej_5.py**

<p align="justify">Realizados todos los ejercicios, únicamente nos quedaba unificarlos todos en un solo shader creando una clase en un script de python. </p>
<p align="justify">Para ello, creamos una clase llamada <em>Ejericio5</em> (1) donde definíamos 3 funciones, una para cada uno de los ejercicios anteriores implementados en python. Cabe decir que a cada una de las funciones debíamos pasarle como parámetros <em>self</em> (2) con la finalidad de realizar dichas funciones al ejecutarlas mediante la clase. </p>
<p align="justify">Creada la clase y utilizada como: <em>función = Ejercicio5()</em> (1), procedí a hacer el mismo proceso que en los ejercicios anteriores: crear un bucle de tipo <em>while</em> para que el usuario pueda ejecutar el script todas las veces que lo requiera sin tener que salir de la pantalla de ejecución del script. </p>

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-5/intro-ejericio-5.png" width="700"/>
</p>

<p align="justify">Dentro del bucle se le pregunta al usuario cuál de los ejercicios quiere realizar y según su respuesta se realiza con condicional y se procede a llamar a la función mediante la clase creada: <em>funcion.ejX()</em> (1).</p>

* X=1 (Ejercicio 2 de la práctica)
* X=2 (Ejercicio 3 de la práctica)
* X=3 (Ejercicio 4 de la práctica)).


<p align="justify">Fuentes:<br>(1) https://www.w3schools.com/python/python_classes.asp <br>(2) https://stackoverflow.com/questions/60461651/typeerror-takes-0-positional-arguments-but-1-was-given</p>
