#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
int butt = 12;
int pir = 14;
String str;
const char* ssid = "BPstudent";
const char* pass = "studentuse";
const char* home = "http://10.30.1.16:5000/api/data";

void send_info( String message){
  WiFiClient client;
  HTTPClient http;

  http.begin(client,home);
  int httpCode = http.GET();
  Serial.println(httpCode);
  http.addHeader("Content-Type","application/json");
  String HttpRequestData = message;
  int HttpResponceCode = http.POST(HttpRequestData);
  Serial.println(HttpResponceCode);
  String paload = http.getString();
  Serial.println(paload);
  http.end();
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  pinMode(0, OUTPUT);
 
  pinMode(12,INPUT_PULLUP);
  pinMode(14,INPUT_PULLUP);
  bool butt;
  bool pir;
  
  while(WiFi.status() != WL_CONNECTED){
    Serial.println("connecting");
    delay(1000);
  }
  Serial.println("connected");

}

void loop() {
  butt = digitalRead(12);
  pir = digitalRead(14);
  String str = "{\"Button\" : " + "butt" + ",\"Pir\" : \" " + "pir"+ "\"}";
  send_info(str);
  delay(250);
}

