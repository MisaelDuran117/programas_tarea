int pinRojo = 3;   
int pinVerde = 5; 
int pinAzul = 6;  

void setup() {
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char voz = Serial.read();
    
    if (voz == '1') {
      // Encender color rojo
      analogWrite(pinRojo, 255);  
      analogWrite(pinVerde, 0);
      analogWrite(pinAzul, 0);
    } else if (voz == '2') {
      // Encender color verde
      analogWrite(pinRojo, 0);
      analogWrite(pinVerde, 255);  
      analogWrite(pinAzul, 0);
    } else if (voz == '3') {
      // Encender color azul
      analogWrite(pinRojo, 0);
      analogWrite(pinVerde, 0);
      analogWrite(pinAzul, 255);  
    } else if (voz == '0') {
      // Apagar el LED RGB
      analogWrite(pinRojo, 0);
      analogWrite(pinVerde, 0);
      analogWrite(pinAzul, 0);
    }
  }
}
