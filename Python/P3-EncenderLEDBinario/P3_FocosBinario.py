import serial
import speech_recognition as sr
from word2number import w2n
r = sr.Recognizer()
puerto_serial = 'COM3'
arduino = serial.Serial(puerto_serial, 9600, timeout=1)

print("Encender Numero Binario en Focos")
while(True):
    with sr.Microphone() as source:
        print("Di un número:")
        audio = r.listen(source)
    try:
        palabra_numero = r.recognize_google(audio, language="es-MX")
        print("Palabra reconocida:", palabra_numero)

        numero_entero = w2n.word_to_num(palabra_numero)
        numero_entero=str(numero_entero)
        arduino.write(numero_entero.encode())

        print("Número entero:", numero_entero)
    except sr.UnknownValueError:
        print("No se pudo reconocer la palabra.")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
    except Exception as ex:
        print(f"Error desconocido: {ex}")



