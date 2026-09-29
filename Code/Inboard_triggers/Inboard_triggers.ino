#include <ESP8266WiFi.h>  // Use <WiFi.h> if it's the ESP32 Feather
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

const char* ssid = "BPstudent";
const char* password = "studentuse";

// Replace with your computer's local IP address and Flask port
const char* home = "http://10.30.1.16:5000";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  Serial.println("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected! IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    HTTPClient http;
    
    http.begin(client, home);
    http.addHeader("Content-Type", "application/json");
    
    // Sample JSON payload to send to Flask
    String httpRequestData = "{\"sensor\":\"temperature\",\"value\":25.5}";
    
    int httpResponseCode = http.POST(httpRequestData);
    
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }
  
  // Send data every 10 seconds
  delay(10000); 
}
