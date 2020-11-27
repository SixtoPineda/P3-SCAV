import subprocess

print("\n\n\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Realizar ejercicio (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0

    archivo = input("\n\nIntroduzca el nombre COMPLETO del video con el que trabajar: ")#pedimos el nombre del video con el que trabajar
    print("\nSe va a realizar lo siguiente:\n\n\t- Recortamos 1 minuto del video (solo video sin audio)\n\t- Extraemos en mono el track de audio del video\n\t- Extraemos el audio con bajo bitrate\n\n\tGeneraremos un nuevo container con ambos tracks de audio, el video y subtítulos para éste.\n")

    print("\nIntroduzca los codecs de cada uno de los componentes del container final:\n")#
    #damos al usuario la oportunidad de escoger que codecs tendrá el video y los dos audios en el container final
    video_codec = input("\tVideo:\n\t\t- h.264(h264)\n\t\t- h.265(hevc)\n\t\t- MPEG1(mpeg1video)\n\t\t- MPEG2(mpeg2video)\n\t\t- MPEG4(mpeg4)\n\n\t\t\tIntroduzca el codec (codec entre paréntesis): ")
    audio_codec1 = input("\tAudio 1:\n\t\t- AAC(aac)\n\t\t- MP3(mp3)\n\t\t- AC3(ac3)\n\t\t- MP2(mp2)\n\n\t\t\tIntroduzca el codec (codec entre paréntesis): ")
    audio_codec2 = input("\tAudio 2:\n\t\t- AAC(aac)\n\t\t- MP3(mp3)\n\t\t- AC3(ac3)\n\t\t- MP2(mp2)\n\n\t\t\tIntroduzca el codec (codec entre paréntesis): ")

    #damos de forma opcional que el usuario quiera añadir subtítulos al video o no
    subst = input("\nQuiere añadir subtítulos al container? (1=Sí, 0=No): ")
    if(int(subst) == 1):#en caso de que hayan subtitulos
        sub = input("\nIntroduzca el fichero .srt para los subtítulos del video (NOMBRE COMPLETO): ")#pedimos el nombre del fichero con los subtitulos

    outputUser = input("\nIntroduzca el nombre del 'Container' .mp4 (con extensión .mp4): ")#pedimos el nombre final del archivo


    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -c:v {video_codec} -t 00:01:00 -an step1.mp4", shell=True)#video de 1 minuto
    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -acodec {audio_codec1} -t 00:01:00 -ac 1 monoStep2.{audio_codec1}", shell=True)#autio track en mono
    subprocess.run(f"ffmpeg -ss 00:00:00 -i {archivo} -acodec {audio_codec2} -b:a 50k -t 00:01:00 lowBitrateStep3.{audio_codec2}", shell=True)#audio track low bitrate

    if(int(subst) == 1):#en caso de que hayan subtitulos
        subprocess.run(f"ffmpeg -i step1.mp4 -i {sub} -map 0 -map 1 -c copy -c:s mov_text step1Sub.mp4", shell=True)#añadimos los subtitulos
        subprocess.run(f"ffmpeg -i step1Sub.mp4 -i monoStep2.{audio_codec1} -i lowBitrateStep3.{audio_codec2} -map 0 -map 1 -map 2 -c copy {outputUser}", shell=True)#añadimos los tracks de los audios
    else:
        subprocess.run(f"ffmpeg -i step1.mp4 -i monoStep2.{audio_codec1} -i lowBitrateStep3.{audio_codec2} -map 0 -map 1 -map 2 -c copy {outputUser}", shell=True)#añadimos los tracks de los audios

    #borramos los ficheros creados para realizar los pasos
    subprocess.run(f"rm step1.mp4", shell=True)
    subprocess.run(f"rmmonoStep2.{audio_codec1}", shell=True)
    subprocess.run(f"rm lowBitrateStep3.{audio_codec2}", shell=True)
    if(int(subst) == 1):#en caso de que hayan subtitulos
        subprocess.run(f"rm step1Sub.mp4", shell=True)

###############################################EJERCICIO-3####################################################################
    print("\n\n\n")
    print("Estos son los codecs del video y audios resultante del container formado con el nombre ",outputUser,"\n")
    subprocess.run(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {outputUser}", shell=True)
    codecs = str(subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {outputUser}", shell=True))


    if( (str('avs') in codecs) or (str('cavs') in codecs)):#broadcast-DTMB
        if((str('dra') in codecs) or (str('aac') in codecs) or (str('ac3') in codecs) or (str('mp2') in codecs) or (str('mp3') in codecs)):
            print("\tBroadcast: DTMB\n\n")
        else:
            print("\n\t\tNone broadcasting standard fits\n\n\n")

    elif((str('mpeg2video') in codecs) or (str('h264') in codecs)):
        if( (str('dra') in codecs) or (str('mp2') in codecs)):
            if((str('aac') in codecs)):
                print("\tBroadcast: ISDB-DVB-DTMB\n\n")
            elif((str('ac3') in codecs)):
                print("\tBroadcast: ATSC-DVB-DTMB\n\n")
            elif((str('mp3') in codecs)):
                print("\tBroadcast: DVB-DTMB\n\n")
            else:
                print("\tBroadcast: DTMB\n\n")

        elif((str('aac') in codecs)):
            if((str('ac3') in codecs)):
                print("\tBroadcast: ISDB-ATSC-DVB-DTMB\n\n")
            else:
                print("\tBroadcast: ISDB-DVB-DTMB\n\n")

        elif((str('ac3') in codecs)):
            print("\tBroadcast: ATSC-DVB-DTMB\n\n")

        elif((str('mp3') in codecs)):
            print("\tBroadcast: DVB-DTMB\n\n")
        else:
            print("\n\t\tNone broadcasting standard fits\n\n\n")

    else:
        print("\n\t\tNone broadcasting standard fits\n\n\n")
##############################################################################################################################

    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\n\n\t\t- Realizar ejercicio (1)")
    print("\n\t\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
