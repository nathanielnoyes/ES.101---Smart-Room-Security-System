#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>


const char* ssid = "BPstudent";
const char* password = "studentuse";

int butt = 12;
int pir = 14;
String str;
void setup() {
 Serial.begin(115200);
 delay(100);
 WiFi.begin(ssid, password);
 delay(100);
 while(WiFi.status() != WL_CONNECTED){
  delay(1000);
  Serial.println("connecting");
 }
 Serial.println("connected");
 Serial.println(WiFi.localIP());

 pinMode(0, OUTPUT);
 
 pinMode(butt,INPUT_PULLUP);
 pinMode(pir,INPUT_PULLUP);
}


void loop() {
  str = digitalRead(butt);
  digitalWrite(0,digitalRead(pir));
  //Serial.println(str);
  delay(2500);
  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;
  }

}