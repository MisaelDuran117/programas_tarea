int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char voz = Serial.read(); 
    if (voz == '1') {
      digitalWrite(ledPin, HIGH); 
    } else if (voz == '0') {
      digitalWrite(ledPin, LOW); 
    }
  }
}
