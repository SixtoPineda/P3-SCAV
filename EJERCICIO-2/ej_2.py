import subprocess

print("\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Realizar ejercicio (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0


    archivo = input("\n\nIntroduzca el nombre COMPLETO del video con el que trabajar: ")#pedmimos el nombre del video con el que trabajar
    print("\nSe va a realizar lo siguiente:\n\tRecortamos 1 minuto del video (solo video sin audio)\n\tExtraemos en mono el track de audio del video\n\tExtraemos el audio con bajo bitrate\n\n\tGeneraremos un nuevo container con ambos tracks de audio, el video y subtítulos para éste.\n")

    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -c copy -t 00:01:00 -an step1.mp4", shell=True)#video de 1 minuto
    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -t 00:01:00 -ac 1 monoStep2.mp3", shell=True)#autio track en mono
    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -b:a 50k -t 00:01:00 lowBitrateStep3.mp3", shell=True)#audio track low bitrate
    sub = input("\nIntroduzca el fichero .srt para los subtítulos del video (NOMBRE COMPLETO): ")#pedimos el nombre del fichero con los subtitulos

    outputUser = input("\nIntroduzca el nombre del archivo resultante .mp4 (con extensión): ")#pedimos el nombre final del archivo (output)

    subprocess.run(f"ffmpeg -i step1.mp4 -i {sub} -map 0 -map 1 -c copy -c:s mov_text step1Sub.mp4", shell=True)#añadimos los subtitulos
    subprocess.run(f"ffmpeg -i step1Sub.mp4 -i monoStep2.mp3 -i lowBitrateStep3.mp3 -map 0 -map 1 -map 2 -codec copy {outputUser}", shell=True)#añadimos los tracks de los audios

    #eliminamos los archivos creados para realizar cada uno de los pasos y crear el container
    subprocess.run(f"rm step1.mp4", shell=True)
    subprocess.run(f"rm monoStep2.mp3", shell=True)
    subprocess.run(f"rm lowBitrateStep3.mp3", shell=True)
    subprocess.run(f"rm step1Sub.mp4", shell=True)

    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\n\n\t\t- Realizar ejercicio (1)")
    print("\n\t\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
