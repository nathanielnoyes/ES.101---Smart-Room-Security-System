#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "BPstudent";
const char* pass = "studentuse";
const char* home = "http://10.30.1.16:5000";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  while(WiFi.status() != WL_CONNECTED){
    Serial.println("connecting");
    delay(1000);
  }
  Serial.println("connected");
}

void loop() {
  if(WiFi.status() == WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;

    http.begin(client,home);
    http.addHeader("Content-Type","application/json");

    String HttpRequestData = "{fish = 'tuff'}";
    int HttpResponceCode = http.POST(HttpRequestData);
    Serial.println(HttpResponceCode);
    http.end();
    
  }
  delay(10000);
}
