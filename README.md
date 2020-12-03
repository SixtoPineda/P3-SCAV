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
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/vp8.png" width="350">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/VP9.png" width="350">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/H265.png" width="350">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/AV1.png" width="350">
</p>


<p align="justify">Como podemos ver, cada video corresponde con su respectiva resolución como se ha mencionado anteriormente al inicio del ejercicio.</p>
<p align="justify"><em>Resultado de cada video del ejercicio en EJERCICIO-1/FOTOS</em></p>

### EJERCICIO-2
#### ***Container of the 4 videos***

<p align="justify">En este apartado se nos pedía automatizar todos los pasos realizados en el ejercicio 1 en un solo script de python.<br>Para ello, decidí reutilizar código de prácticas anteriores. Creé un bucle de tipo <em>while</em> donde se le pide al usuario, tanto al iniciar la ejecución como al finalizarla, si éste quiere acabar con la ejecución o quiere seguir trabajando con el script con otro/s archivos más.<br><br>A partir de aquí, le pedimos al usuario que nos introduzca el nombre <strong>completo</strong> del video con en que realizar los pasos anteriores y crear un nuevo container. Una vez el usuario nos da el nombre de dicho archivo, procedemos a ejecutar cada uno de los comandos como he mencionad en el ejercicio 1, pero desde el fichero python con la función <em>subprocess.run</em>.<br><br>De igual forma que en anteriores prácticas, se pide al usuario que introduzca el nombre del archivo final, en este caso del container .mp4.<br>Cabe decir que al finalizar la ejecución del ejercicio borramos cada uno de los archivos generados para realizar el ejercicio y así solo dejar el resultado final en el container con extensión .mp4. </p>

##### **Pasos**

###### **1**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-2/FOTOS/1-screen.png" width="600"/>
</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P3-SCAV/blob/main/EJERCICIO-2/FOTOS/resultados.png" width="700"/>
</p>

<p align="justify">Como podemos ver, de igual forma que en ejercicio 1, obtenemos el container final con todos los componentes, el video que previamente extraíamos sin audio, los dos tracks de audio, mono y con bajo bitrate, y los subtítulos. </p>


### EJERCICIO-4
#### ***Python: The online streaming***

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



