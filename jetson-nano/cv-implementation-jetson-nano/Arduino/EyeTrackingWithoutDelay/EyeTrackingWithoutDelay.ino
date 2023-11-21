/*
   Eye Tracking 
   Author: Ashish Kumar
   Date: Nov 23, 2023
   Venue: UAV Lab, IIT Kanpur
*/

#include <Servo.h>


#define numOfValsRec 2                                        // The number of values we are receiving, to define array       
#define digitsPerValRec 3


Servo myservoLR;                                              // create servo object to control a servo
Servo myservoUD;


int valsRec[numOfValsRec];                                    // array to store the values received
int stringLength = numOfValsRec * digitsPerValRec + 1;        // 1 is for dollar sign, example string '$055255'
int counter = 0;                                              // for reading the elements of array string
bool counterStart = false;                                    // to check if counter started
String receivedString;


void setup() {
  Serial.begin(9600);                                         // This value should match the python script
  myservoLR.attach(9);                                        // attaches the servo on pin 9 to the servo object
  myservoUD.attach(10);

  // Go to the middle at the start, 90 degree
  myservoLR.write(90);
  myservoUD.write(90);
//  delay(1000);
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
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();               // start at 2nd index, break at 5th index
        }

        // reset the params
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  receiveData();
  myservoLR.write(valsRec[0]);
  Serial.println(valsRec[0]);
 
  myservoUD.write(valsRec[1]);
  Serial.println(valsRec[1]);
}
