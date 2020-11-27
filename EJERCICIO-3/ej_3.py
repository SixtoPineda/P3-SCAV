import subprocess

print("\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Realizar ejercicio (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0

    archivo = input("\n\nIntroduzca el nombre COMPLETO del video con el que trabajar: ")#pedimos el nombre del archivo
    print("\n\t")
    subprocess.run(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {archivo}", shell=True)#printamos por pantalla el codec del video/s y el audio/s
    print("\n")
    codecs = str(subprocess.check_output(f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1 {archivo}", shell=True))#guardamos el codec del video/s y el audio/s

    #haremos varios condicionales según el que combinación de codecs de audio y video dan lugar a un broadcasting u otro
    #en el caso de que no coincida con ninguno, diremos que ningún broadcasting se adapta

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


    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\t\t- Realizar ejercicio (1)")
    print("\n\t\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
