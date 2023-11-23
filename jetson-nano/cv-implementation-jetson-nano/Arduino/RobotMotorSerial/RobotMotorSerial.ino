/*
   Control brightness of multiple LEDs
   Author: Ashish Kumar
   Date: Nov 20, 2023
   Venue: UAV Lab, IIT Kanpur
*/


#define numOfValsRec 2                                        // The number of values we are receiving, to define array       
#define digitsPerValRec 4


int valsRec[numOfValsRec];                                     // array to store the values received
int stringLength = numOfValsRec * digitsPerValRec + 1;         // 1 is for dollar sign, example string '$055255'
int counter = 0;                                              // for reading the elements of array string
bool counterStart = false;                                    // to check if counter started
String receivedString;

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
 


void receiveData() {
  /*
     Creating receivedString variable,
     reading one element at a time from serial.
     Directly changing the receivedString, so no return required.
  */
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '$') {
      counterStart = true;
    }
    if (counterStart) {

      // read the data till the number of characters read is less than stringlength
      if (counter < stringLength) {
        receivedString = String(receivedString + c);
        counter++;
      }

      // parse the read data and convert them to ints
      if (counter >= stringLength) {
        for (int i = 0; i < numOfValsRec; i++) {
          int num = i * digitsPerValRec + 1;
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();                       // start at 2nd index, break at 5th index
        }

        // reset the params
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}


void setup() {

  for (int i = 0; i < 6; i++) {
    pinMode(myPins[i], OUTPUT);
  }
  
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);                                        // here using only 1 LED, but receiving vals for 2 LEDs
  Serial.begin(9600);                                         // This calue should match the python script
} 

void loop() {
  // put your main code here, to run repeatedly:

  receiveData();
  moveRobot(valsRec[0], valsRec[1]);
}
