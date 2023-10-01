
String cadena, texto;
int i, c, j, b, numero;
char n;
int leds[] = {2, 3, 4, 5, 6, 7, 8, 9}; 
void setup() {
  Serial.begin(9600);  
  Serial.setTimeout(100);  
  
  for (i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {  
    cadena = Serial.readStringUntil('\n');  
    int numero = cadena.toInt();  // Convierte la cadena de texto a un número entero
    int Bin[] = {0, 0, 0, 0, 0, 0, 0, 0};  // Arreglo para almacenar los bits binarios
    j = -1;  

    Serial.println(String(numero));  
    
    // Convierte el número a su representación binaria
    for (i = numero; i > 0;) {
      j++;
      b = i % 2;
      Bin[j] = b;
      i = i / 2;
    }

    int o = 7;

    // Enciende o apaga los LEDs según los bits binarios
    for (int m = 0; m < 8; m++) {
      digitalWrite(leds[m], Bin[o]);
      Serial.println(Bin[o]);
      o--;
    }
    
    delay(3000);  // Espera 3 segundos
    c++;  // Incrementa la variable c
  }
  
  // Apaga todos los LEDs
  for (int m = 0; m < 8; m++) {
    digitalWrite(leds[m], 0);
  }
}
