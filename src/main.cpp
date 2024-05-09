

#include <Arduino.h>

#define green_pin_HAPPY 11
//#define blue_pin_SAD 7
//#define pin_ERROR 11

int data, flag;

// the setup function runs once when you press reset or power the board

void setup() {

  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(green_pin_HAPPY, OUTPUT);
  //pinMode(blue_pin_SAD, OUTPUT);
  //pinMode(pin_ERROR, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {

if (Serial.available()> 0) {
  data = Serial.read();

  if (data != 0) {
    digitalWrite(green_pin_HAPPY, LOW); // On
  }
  else {
    digitalWrite(green_pin_HAPPY, HIGH); // Off
  }
  
}
}
