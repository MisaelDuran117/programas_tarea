import pygame
import serial
import speech_recognition as sr
r = sr.Recognizer()
puerto_serial = 'COM3'
arduino = serial.Serial(puerto_serial, 9600, timeout=1)
pygame.mixer.init()
print("ALARMA")
while(True):
    try:
        mensaje = arduino.readline().decode('utf-8').strip()
        print(mensaje)
        if mensaje == "movimiento detectado":
            pygame.mixer.music.load("alarma.mp3")
            pygame.mixer.music.play(-1)

        print("Escuchando.......")
        with sr.Microphone() as source:
            audio = r.listen(source)

        print("Voz Aceptada")

        cadena = r.recognize_google(audio, language="es-MX")
        print("Mensaje: " + cadena)
        activar = "activar alarma" #DECIR
        desactivar = "desactivar alarma"
        cadena = cadena.lower()


        if cadena == activar:
            print("ALARMA ACTIVADA")
            arduino.write(b'1')
        if cadena == desactivar:
            print("ALARMA DESCATIVADA.")
            arduino.write(b'0')
            pygame.mixer.music.stop()



    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado. No se detectó voz.")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
    except sr.UnknownValueError:
        print("No se pudo reconocer la voz.")
    except Exception as ex:
        print(f"Error desconocido: {ex}")



