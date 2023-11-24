/*
   Author: Ashish Kumar
   Date: November 27, 2023
   Place: UAV Lab, IIT Kanpur

   This file is used to test motor movement of a ground robot.
*/

// grant permission to access the serial port
// sudo chmod 666 /dev/ttyACM0


// lot of pins, so creating an array
// enable pin (controls speed), 2 pins for direction
// 3,9 are enable pins, 4,5,11,10 are direction pins
// enable pins are analog, because speed (range 0 to 255), simulating using pwm
// direction pins are digital
int myPins[6] = {3, 4, 5, 11, 10, 9}; // configuration of h bridge


void setup() {
  
  // set all these pins to outputs
  for (int i = 0; i < 6; i++) {
    pinMode(myPins[i], OUTPUT);
  }

  Serial.begin(9600);

  // -------------- Testing Code ---------------------

  // Forward Motion
  
  // Motor A
  digitalWrite(myPins[1], 0);
  digitalWrite(myPins[2], 1);
  analogWrite(myPins[0],160);

  // Motor B
  digitalWrite(myPins[3], 0);
  digitalWrite(myPins[4], 1);
  analogWrite(myPins[5],160);

  // for stopping
  delay(3000);
  analogWrite(myPins[0],0);
  analogWrite(myPins[5],0);

}

void loop() {

  // Testing code not written in loop to prevent battery drainage, as will run repeatedly.

}
