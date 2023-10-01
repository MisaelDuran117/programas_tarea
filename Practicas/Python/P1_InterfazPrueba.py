import sys
import serial as s
from PyQt5 import QtWidgets, QtCore, uic
import speech_recognition as sr

r = sr.Recognizer()

qtCreatorFile = "Conexion.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.splano)

    def accion(self):
        try:
            txt_btn = self.btn_accion.text()

            if txt_btn == "CONECTAR" or txt_btn == "RECONECTAR":
                if self.arduino is not None:
                    self.arduino.close()
                    self.arduino = None  # Establece la instancia del puerto COM a None

                self.btn_accion.setText("DESCONECTAR")
                puerto = "COM" + self.txt_puerto.text()
                self.arduino = s.Serial(puerto, baudrate=9600, timeout=1)
                self.segundoPlano.start(10)
                print("CONECTADO")

            elif txt_btn == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
                if self.arduino is not None:
                    self.arduino.close()
                    self.arduino = None  # Establece la instancia del puerto COM a None
                print("DESCONECTADO")

        except Exception as error:
            print(error)

    def splano(self):
        try:
            print("Escuchando.......")
            with sr.Microphone() as source:
                audio = r.listen(source)

            print("Voz Aceptada")

            cadena = r.recognize_google(audio, language="es-MX")
            print("Mensaje: " + cadena)
            EncenderLED = "encender foco"
            ApagarLED = "apagar foco"
            cadena = cadena.lower()

            if cadena == EncenderLED:
                print("Las cadenas son iguales.")
                print("LED ENCENDIDO")
                if self.arduino is not None:
                    self.arduino.write("1".encode())
            if cadena == ApagarLED:
                print("Las cadenas son diferentes.")
                if self.arduino is not None:
                    self.arduino.write("0".encode())

        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado. No se detectó voz.")
        except sr.RequestError as e:
            print(f"Error en la solicitud de reconocimiento de voz: {e}")
        except sr.UnknownValueError:
            print("No se pudo reconocer la voz.")
        except Exception as ex:
            print(f"Error desconocido: {ex}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())