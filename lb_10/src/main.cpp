#include <Arduino.h>
#include "WiFi.h"
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

String serverName= "http://192.168.86.210/";
HTTPClient http;

StaticJsonDocument<200> doc;

void setup() {
  Serial.begin(9600);
  WiFi.begin(SSID, PASSWORD);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.println(WiFi.localIP());
}

void loop(){
  String ime= "Filip";
  doc ["ime"] = ime;

  String prezime= "Šijak";
  doc ["prezime"] = prezime;

  String ip= "192.168.86.211";
  doc ["ip"] = ip;

  String json;
  serializeJson(doc, json);

  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode= http.POST(json);

  Serial.print("Status code: ");
  Serial.println(httpResponseCode);
  Serial.println(http.getString());

  http.end();

  delay(1000);

}

