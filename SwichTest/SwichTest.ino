int pin = 14;

void setup() {
 Serial.begin(115200);
 pinMode(pin,INPUT_PULLUP);
}


void loop() {
  int reed = digitalRead(pin);
 Serial.println(reed);
 delay(500);
}