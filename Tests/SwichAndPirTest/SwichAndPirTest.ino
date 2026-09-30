



int butt = 12;
int pir = 14;
String str;
void setup() {
 Serial.begin(115200);

 pinMode(0, OUTPUT);
 
 pinMode(butt,INPUT_PULLUP);
 pinMode(pir,INPUT_PULLUP);
}


void loop() {
  str = digitalRead(butt);
  digitalWrite(0,digitalRead(pir));
  Serial.println(str);
  delay(100);


}