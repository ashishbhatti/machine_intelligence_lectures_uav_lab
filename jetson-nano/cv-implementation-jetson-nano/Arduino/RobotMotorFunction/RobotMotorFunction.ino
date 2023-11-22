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


void moveRobot (int mySpeed, int myTurn, int maxSpeed = 255) {
  /*
   * 
     Args:
        mySpeed: Expecting values between -100,100, +ve value forwards, -ve backward
        myTurn: Expacting values between -100,100, +ve value left, -ve right
        
  */

  // mapping values to actual range of -255,255
  mySpeed = map(mySpeed, -100, 100, -maxSpeed, maxSpeed);
  myTurn = map(myTurn, -100, 100, -maxSpeed, maxSpeed);

  int leftSpeed = mySpeed - myTurn;
  int rightSpeed = mySpeed + myTurn;

  leftSpeed = constrain(leftSpeed, -maxSpeed, maxSpeed);
  rightSpeed = constrain(rightSpeed, -maxSpeed, maxSpeed);

  if (rightSpeed > 0) {
    // Motor B
    digitalWrite(myPins[1], 0);
    digitalWrite(myPins[2], 1);
  }
  else {
    digitalWrite(myPins[1], 1);
    digitalWrite(myPins[2], 0);
  }

  if (leftSpeed > 0) {
    // Motor B
    digitalWrite(myPins[3], 0);
    digitalWrite(myPins[4], 1);
  }
  else {
    digitalWrite(myPins[3], 1);
    digitalWrite(myPins[4], 0);
  }

  analogWrite(myPins[0], abs(rightSpeed));
  analogWrite(myPins[5], abs(leftSpeed));
}


void setup() {

  // set all these pins to outputs
  for (int i = 0; i < 6; i++) {
    pinMode(myPins[i], OUTPUT);
  }

  Serial.begin(9600);

  // -------------- Testing Code ---------------------

  moveRobot(30,0);

  // for stopping
  delay(3000);
  moveRobot(0,0);

}

void loop() {

  // Testing code not written in loop to prevent battery drainage, as will run repeatedly.

}
