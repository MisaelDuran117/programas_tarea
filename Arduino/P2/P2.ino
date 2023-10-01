#include <NewPing.h>
#define TRIGGER_PIN 12
#define ECHO_PIN 11
#define MAX_DISTANCE 15

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

boolean sensor_activado = false;

void setup() {
  Serial.begin(9600);
  for (int i = 2; i <= 9; i++) {
    pinMode(i, OUTPUT);
  }
}

int control = 1;
void loop() {
  if (Serial.available() > 0) {
    char voz = Serial.read();
    if (voz == '1') {
      sensor_activado = true;
    }
    if (voz == '0') {
      sensor_activado = false;
    }
  }

  if (sensor_activado) {
  unsigned int distancia = sonar.ping_cm();
    if (distancia != 0) {
      if (control ==1){
                Serial.println("movimiento detectado");
                control++;
        }

        for (int i = 2; i <= 9; i++) {
          digitalWrite(i, HIGH); 
          delay(80);  
          digitalWrite(i, LOW);   
          delay(80); 
      }
  }
}
}
