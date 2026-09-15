void Setup() {
   pinMode(0, OUTPUT);
   Serial.begin(115200);

}

void Loop() {
   digitalWrite(0, HIGH);
   Serial.println("phi");

   delay(1000);
   digitalWrite(0, LOW);
   Serial.println("hi");

   delay(1000);
}
