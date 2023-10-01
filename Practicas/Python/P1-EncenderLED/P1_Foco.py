import serial
import speech_recognition as sr
r = sr.Recognizer()
puerto_serial = 'COM3'
arduino = serial.Serial(puerto_serial, 9600, timeout=1)
print("ENCENDER FOCO")
while(True):
    try:
        print("Escuchando.......")
        with sr.Microphone() as source:
            audio = r.listen(source)

        print("Voz Aceptada")

        cadena = r.recognize_google(audio, language="es-MX")
        print("Mensaje: " + cadena)
        EncenderLED = "encender foco" #DECIR
        ApagarLED = "apagar foco"
        cadena = cadena.lower()

        if cadena == EncenderLED:
            print("Las cadenas son iguales.")
            print("LED ENCENDIDO")
            if arduino is not None:
                arduino.write("1".encode())
        if cadena == ApagarLED:
            print("Las cadenas son diferentes.")
            if arduino is not None:
                arduino.write("0".encode())

    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado. No se detectó voz.")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
    except sr.UnknownValueError:
        print("No se pudo reconocer la voz.")
    except Exception as ex:
        print(f"Error desconocido: {ex}")


