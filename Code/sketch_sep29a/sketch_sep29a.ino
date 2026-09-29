#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "BPstudent";
const char* pass = "student use";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  while(WiFi.status() != WL_CONNECTED){
    Serial.println(".");
  }

}

void loop() {
  if(WiFi.status() == WL_CONNECTED){
    Htt
  }
}
