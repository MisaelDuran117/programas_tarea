import serial
import speech_recognition as sr
r = sr.Recognizer()
puerto_serial = 'COM3'
arduino = serial.Serial(puerto_serial, 9600, timeout=1)

while(True):
    try:
        with sr.Microphone() as source:
            print("Prender Color de Foco RGB")
            audio = r.listen(source)

        rango = r.recognize_google(audio, language="es-MX")
        print("Palabra reconocida:", rango)
        rango=rango.lower()

        if rango == "enciende foco rojo":
            arduino.write("1".encode())
        if rango == "enciende foco verde":
            arduino.write("2".encode())
        if rango == "enciende foco azul":
            arduino.write("3".encode())
        if rango == "apagar foco":
            arduino.write("0".encode())
    except sr.UnknownValueError:
        print("No se pudo reconocer la palabra.")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
    except Exception as ex:
        print(f"Error desconocido: {ex}")
