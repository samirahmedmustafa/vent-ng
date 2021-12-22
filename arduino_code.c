#include <Wire.h>
#include <Adafruit_MLX90614.h>
#define SLAVE_ADDRESS 0x08
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

const int ledPin = 13; 

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  mlx.begin();  
}

void receiveData(int bytecount)
{

   while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}

void loop() {
  delay(500);
}
