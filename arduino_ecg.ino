void setup() {
  Serial.begin(115200); // Comunicación serial a 115200 bps
  pinMode(A1, INPUT); // Pin para leer la señal analógica
}

void loop() {
  int emgValue = analogRead(A1); // Leer valor analógico del pin A1
  
  // Convertir emgValue a 2 bytes y enviarlo
  byte lowByte = emgValue & 0xFF;          // Byte bajo
  byte highByte = (emgValue >> 8) & 0xFF;  // Byte alto
  
  Serial.write(lowByte);  // Enviar byte bajo
  Serial.write(highByte); // Enviar byte alto
  
  delay(1); // Pequeña pausa para la adquisición
}