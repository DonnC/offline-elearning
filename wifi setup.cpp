#include <ESP8266WiFi.h>
#include <LiquidCrystal_I2C.h>

// Set AP credentials
#define AP_SSID "OfflineRMS"
#define AP_PASS "8HH3Hs&%_Passw8d9"

String IPAddress = "";

int lcdColumns = 16;
int lcdRows = 2;

LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  
 
void setup()
{
  // Setup serial port
  Serial.begin(115200);
  Serial.println();

  // initialize LCD
  lcd.init();

  // turn on LCD backlight                      
  lcd.backlight();

  lcd.setCursor(0, 0);
  
  lcd.print("AP init..");
 
  // Begin Access Point
  WiFi.mode(WIFI_AP_STA);
  
  // setup encrypted AP
  // WiFi.softAP(AP_SSID, AP_PASS);

  WiFi.softAP(AP_SSID);
 
  // AP created, print IP address
  Serial.print("IP address for network ");
  Serial.print(AP_SSID);
  Serial.print(" : ");
  Serial.print(WiFi.softAPIP());

  IPAddress = WiFi.softAPIP();

  lcd.setCursor(0, 1);

  lcd.print(WiFi.softAPIP());
  
  delay(1000);
}
 
void loop() {
  lcd.clear();

  lcd.setCursor(0, 0);

  lcd.print("connect to..");

  delay(2000);

  lcd.clear();

  lcd.setCursor(0, 0);

  lcd.print("Name: " + AP_SSID);

  lcd.setCursor(0, 1);

  lcd.print("IP: " + IPAddress);

  delay(1000);
}