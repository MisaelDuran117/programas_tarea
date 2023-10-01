int ledPins[] = {5, 6};
int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char voz = Serial.read();
    switch (voz) {
          case '1':
            analogWrite(ledPins[0], 15); 
            analogWrite(ledPins[1], 15); 
            break;
          case '2':
            analogWrite(ledPins[0], 100); 
            analogWrite(ledPins[1], 100); 
            break;
          case '3':
            analogWrite(ledPins[0], 255); 
            analogWrite(ledPins[1], 255); 
            break;
      }
}


}
