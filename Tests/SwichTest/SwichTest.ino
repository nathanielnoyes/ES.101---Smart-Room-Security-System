int butt = 12;
int pir = 14;
String str;
void setup() {
 // put your setup code here, to run once:
 Serial.begin(115200);
 pinMode(butt,INPUT_PULLUP);
 pinMode(pir,INPUT_PULLUP);
}


void loop() {
  str = digitalRead(butt)+digitalRead(pir);
 // put your main code here, to run repeatedly:
 Serial.println(str);
 delay(250);
}