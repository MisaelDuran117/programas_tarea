import serial
import speech_recognition as sr
r = sr.Recognizer()
puerto_serial = 'COM3'
arduino = serial.Serial(puerto_serial, 9600, timeout=1)

while(True):
    try:
        with sr.Microphone() as source:
            print("Di Bajo, Medio o Alto para controlar la Intensidad de LUZ:")
            audio = r.listen(source)

        rango = r.recognize_google(audio, language="es-MX")
        print("Palabra reconocida:", rango)
        rango=rango.lower()

        if rango == "bajo":
            arduino.write("1".encode())
        if rango == "medio":
            arduino.write("2".encode())
        if rango == "alto":
            arduino.write("3".encode())
    except sr.UnknownValueError:
        print("No se pudo reconocer la palabra.")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
    except Exception as ex:
        print(f"Error desconocido: {ex}")



